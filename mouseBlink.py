import cv2
import mediapipe as mp
import pyautogui
import random

'''
Moves the mouse to a random place on the screen every time you blink
'''

def moveMouse(run=bool):
  if run:
    screenWidth, screenHeight = pyautogui.size()
    rX = random.randint(0, screenWidth-1)
    rY = random.randint(0, screenHeight-1)
    pyautogui.moveTo(rX, rY)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
run = True

def get_eye_aspect_ratio(landmarks, eye_indices):
    # Calculate the distances between the vertical landmarks
    vertical_1 = ((landmarks[eye_indices[1]].x - landmarks[eye_indices[5]].x) ** 2 +
                  (landmarks[eye_indices[1]].y - landmarks[eye_indices[5]].y) ** 2) ** 0.5
    vertical_2 = ((landmarks[eye_indices[2]].x - landmarks[eye_indices[4]].x) ** 2 +
                  (landmarks[eye_indices[2]].y - landmarks[eye_indices[4]].y) ** 2) ** 0.5
    # Calculate the distance between the horizontal landmarks
    horizontal = ((landmarks[eye_indices[0]].x - landmarks[eye_indices[3]].x) ** 2 +
                  (landmarks[eye_indices[0]].y - landmarks[eye_indices[3]].y) ** 2) ** 0.5
    # Eye Aspect Ratio (EAR)
    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)
    return ear

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark
            # Eye indices for left and right eyes from Mediapipe face mesh
            left_eye_indices = [33, 160, 158, 133, 153, 144]
            right_eye_indices = [362, 385, 387, 263, 373, 380]

            left_ear = get_eye_aspect_ratio(landmarks, left_eye_indices)
            right_ear = get_eye_aspect_ratio(landmarks, right_eye_indices)

            # Threshold for detecting closed eyes
            EAR_THRESHOLD = 0.33
            if left_ear < EAR_THRESHOLD and right_ear < EAR_THRESHOLD:
                cv2.putText(frame, "Eyes Closed", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                moveMouse(run)
                run = False
            else:
                cv2.putText(frame, "Eyes Open", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                run = True

    #cv2.imshow('Eye Closure Detection', frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
