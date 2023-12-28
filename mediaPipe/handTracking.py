import cv2
import mediapipe as mp

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

        blackScreen = cv2.imread(r"C:\Users\thetr\Documents\Python\noMouse\640x480BlackScreen.jpg")

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw the hand landmarks on the frame
                mp_drawing.draw_landmarks(blackScreen, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the frame with hand landmarks
        cv2.imshow('Hand Tracking', blackScreen)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
