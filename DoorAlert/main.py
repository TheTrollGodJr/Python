from plyer import notification
import cv2
import mediapipe as mp
import keyboard
import time

def sendNotif(message=str, title=str):
    notification.notify(
        title=title,
        message=message,
        app_icon='DoorAlert/jackblack.ico',
        timeout=5,  # seconds
    )

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
sameCount = 0
lastCoord = [0,0,0,0]
notifSent = True

# Initialize the Face Mesh model
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    
    # Get camera
    cap = cv2.VideoCapture(0)

    sendNotif('The program is now running', 'Program Started')

    while cap.isOpened():
        time.sleep(.1)
        try:
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the image
            results = face_mesh.process(frame_rgb)
            
            if results.multi_face_landmarks:
                # Face detected
                for landmarks in results.multi_face_landmarks:
                    leftEye = (int((landmarks.landmark[130].x * frame.shape[1] + landmarks.landmark[243].x * frame.shape[1]) / 2), int((landmarks.landmark[130].y * frame.shape[0] + landmarks.landmark[243].y * frame.shape[0]) / 2))
                    rightEye = (int((landmarks.landmark[463].x * frame.shape[1] + landmarks.landmark[359].x * frame.shape[1]) / 2), int((landmarks.landmark[463].y * frame.shape[0] + landmarks.landmark[359].y * frame.shape[0]) / 2))
            
            if (leftEye[0] == lastCoord[0]) and (leftEye[1] == lastCoord[1]) and (rightEye[0] == lastCoord[2]) and (rightEye[1] == lastCoord[3]):
                sameCount += 1
            else:
                sameCount = 0
            #print(sameCount)
            if sameCount >= 5:
                notifSent = False
            else:
                if notifSent == False:
                    sendNotif('There is somebody in your room >:3', 'Person Detected')
                    notifSent = True
                lastCoord[0] = leftEye[0]
                lastCoord[1] = leftEye[1]
                lastCoord[2] = rightEye[0]
                lastCoord[3] = rightEye[1]
            #print(notifSent)

        except Exception:
            #print(f"ERROR:\n{Exception}")
            pass

        if keyboard.is_pressed('ctrl+q'):
            sendNotif('The program has stopped', 'Program Ended')
            break

cap.release()
cv2.destroyAllWindows()

