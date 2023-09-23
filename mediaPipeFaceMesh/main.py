import cv2
import mediapipe as mp

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Load an image
imgPath = ""
image = cv2.imread(imgPath)

# Convert the image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Initialize the Face Mesh model
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    # Process the image
    results = face_mesh.process(image_rgb)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            # Draw the face mesh on the image
            mp_drawing.draw_landmarks(image, landmarks, mp_face_mesh.FACEMESH_TESSELATION)
            mp_drawing.draw_landmarks(image, landmarks, mp_face_mesh.FACEMESH_CONTOURS)

# Display the image with the face mesh
cv2.imwrite("img.png", image)