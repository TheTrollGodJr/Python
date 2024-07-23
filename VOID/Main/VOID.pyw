from PIL import Image, ImageChops
import cv2
import keyboard
import soundfile as sf
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import os
import threading

def recognize_speech_from_mic(recognizer, microphone):
    global listening
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    listening = True
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    listening = False
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def average_brightness(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = int(gray.mean())
    return brightness

def play_audio_file(file_path, device_id, shutdown=False):
    global audioPlaying
    if audioPlaying:
        return
    audioPlaying = True

    data, samplerate = sf.read(file_path)
    sd.play(data, samplerate=samplerate, device=device_id, blocking=True) # Blocking = false means that audio CAN be overriden
    sd.wait()

    if shutdown:
        os.system("shutdown /s /t 1")

    audioPlaying = False

def crop_center(image, crop_width, crop_height):
    width, height = image.size
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = (width + crop_width) // 2
    bottom = (height + crop_height) // 2
    return image.crop((left, top, right, bottom))

def image_difference(img1, img2):
    diff = ImageChops.difference(img1, img2)
    diff = diff.convert('L')  # Convert to grayscale
    return diff

def calculate_difference_percentage(diff_img, threshold=10):
    pixels = diff_img.getdata()
    different_pixels = sum(1 for pixel in pixels if pixel > threshold)
    total_pixels = diff_img.width * diff_img.height
    percentage = (different_pixels / total_pixels) * 100
    return percentage

def video():
    global threadsRunning
    if threadsRunning:
        notifSent = False
        detectionOn = True
        waitCount = 0

        cap = cv2.VideoCapture(0)  # Open webcam, change 0 to the appropriate camera index if needed

        _, prev_frame = cap.read()
        prev_frame = Image.fromarray(cv2.cvtColor(prev_frame, cv2.COLOR_BGR2RGB))

        crop_width = 480
        crop_height = 480

        threshold_percentage = 1  # Adjust this threshold based on your requirements
        consecutive_frames_with_movement = 5  # Number of consecutive frames with movement to trigger detection

        frames_with_movement = 0

        play_audio_file(f"{audioPath}/start.wav", 25)

        while True:
            _, frame = cap.read()

            if detectionOn: 
                if notifSent:
                    if waitCount >= 150:
                        notifSent = False
                        waitCount = 0
                    else:
                        waitCount += 1

                current_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                current_frame = crop_center(current_frame, crop_width, crop_height)

                diff_image = image_difference(prev_frame, current_frame)
                diff_percentage = calculate_difference_percentage(diff_image)

                #print(f"Difference Percentage: {diff_percentage:.2f}%")

                if diff_percentage > threshold_percentage:
                    frames_with_movement += 1
                else:
                    frames_with_movement = 0

                if frames_with_movement >= consecutive_frames_with_movement and notifSent == False:
                    #print("Movement detected!")
                    play_audio_file(f"{audioPath}/detection.wav", 25)
                    notifSent = True

                prev_frame = current_frame

            #print(average_brightness(frame))
            if average_brightness(frame) >= 200:
                play_audio_file(f"{audioPath}/welcome.wav", 25)
            elif average_brightness(frame) <= 10:
                #put sound for leaving/turning light off here
                pass
            
            if keyboard.is_pressed('ctrl+p'):
                if detectionOn:
                    detectionOn = False
                    play_audio_file(f"{audioPath}/stop.wav", 25)
                else:
                    detectionOn = True
                    play_audio_file(f"{audioPath}/start.wav", 25)

            if keyboard.is_pressed('ctrl+q'):
                play_audio_file(f"{audioPath}/stop.wav", 25)
                cap.release()
                cv2.destroyAllWindows()
                threadsRunning = False
                break
            
            if listening == True:
                cv2.circle(frame, (50,50), 20, (0,255,0), -1)
            else:
                cv2.circle(frame, (50,50), 20, (255,0,0), -1)

            cv2.imshow("Survalience", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            cv2.waitKey(1)

def audioListening():
    while True:
        if threadsRunning == False:
            break

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        recog = recognize_speech_from_mic(recognizer, microphone)

        #if recog["error"]:
        #    print("ERROR: {}".format(recog["error"]))
            
        word = "{}".format(recog["transcription"]).lower()
        print(word)

        if "void event horizon protocol" in word:
            os.system("shutdown /s /t 1")
            break
        elif "company" in word:
            play_audio_file(f"{audioPath}/company.wav", 25)
        elif "there is nothing we can do" in word:
            play_audio_file(f"{audioPath}/nothing.wav", 25)
        elif "void protocol 505" in word:
            play_audio_file(f"{audioPath}/abandonship.wav", 25, True)
            # Nothing here will run until audio is finished


if __name__ == "__main__":
    listening = False
    audioPlaying = False
    threadsRunning = True

    audioPath = 'E:/Kieran Python Codes/MotionDetection/audioFiles'

    t1 = threading.Thread(target=video)
    t2 = threading.Thread(target=audioListening)

    t1.start()
    t2.start()

    t1.join()
    t2.join()