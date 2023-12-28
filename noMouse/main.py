import cv2
import mediapipe as mp
from pynput.mouse import Controller

wrist = [0,0,0,0,0,0]
dpi = 1

#Create a mouse controller
mouse = Controller()

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open the camera
cap = cv2.VideoCapture(0)  # 0 is typically the default camera, you can change it if needed

# Initialize the Hand model
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw the hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the coordinates of specific landmarks
                wristLandmark = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

                # Convert landmark coordinates from relative to absolute
                image_height, image_width, _ = frame.shape
                wrist[2] = wrist[0]
                wrist[3] = wrist[4]
                wrist[0] = int(wristLandmark.x * image_width)
                wrist[1] = int(wristLandmark.y * image_height)
                #'''
                if abs(wrist[3] - wrist[1]) > 15:
                    mouse.move(0, mouse.position[1] + ((wrist[3] - wrist[1]) * dpi))
                if abs(wrist[2] - wrist[0]) > 15:
                    mouse.move(mouse.position[0] + ((wrist[2] - wrist[0]) * dpi), 0)
                #'''

                # Print the coordinates of the index and middle finger tips
                #print("Wrist (x, y):", wristX, wristY)

        # Display the frame with hand landmarks
        cv2.imshow('Hand Tracking', frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
