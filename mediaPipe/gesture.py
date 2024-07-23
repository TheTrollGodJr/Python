from mediapipe.tasks.python import vision
from mediapipe.tasks import python

class GestureDetectorLogger:

    def __init__(self, video_mode: bool = False):
        self._video_mode = video_mode

        base_options = python.BaseOptions(
            model_asset_path='gesture_recognizer.task'
        )
        options = vision.GestureRecognizerOptions(
            base_options=base_options,
            running_mode=mp.tasks.vision.RunningMode.VIDEO if self._video_mode else mp.tasks.vision.RunningMode.IMAGE
        )
        self.recognizer = vision.GestureRecognizer.create_from_options(options)


    def detect(self, image: npt.NDArray[np.uint8]) -> None:
          image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
  
          # Get results from Gesture Detection model
          recognition_result = self.recognizer.recognize(image)
  
          for i, gesture in enumerate(recognition_result.gestures):
              # Get the top gesture from the recognition result
              print("Top Gesture Result: ", gesture[0].category_name)
  
          if recognition_result.hand_landmarks:
              # Obtain hand landmarks from MediaPipe
              hand_landmarks = recognition_result.hand_landmarks
              print("Hand Landmarks: " + str(hand_landmarks))
  
              # Obtain hand connections from MediaPipe
              mp_hands_connections = mp.solutions.hands.HAND_CONNECTIONS
              print("Hand Connections: " + str(mp_hands_connections))