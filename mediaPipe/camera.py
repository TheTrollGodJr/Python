import cv2
import mediapipe as mp

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Initialize the Face Mesh model
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

    # Open the camera
    cap = cv2.VideoCapture(0)  # 0 is typically the default camera, you can change it if needed

    while cap.isOpened():
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                # Draw the face mesh on the frame
                mp_drawing.draw_landmarks(frame, landmarks, mp_face_mesh.FACEMESH_TESSELATION)
                mp_drawing.draw_landmarks(frame, landmarks, mp_face_mesh.FACEMESH_CONTOURS)

        # Display the frame with the face mesh
        cv2.imshow('Face Mesh', frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
