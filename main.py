import sieve
from typing import Dict, List
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get('SIEVE_API_KEY')  
sieve.SIEVE_API_KEY = os.getenv('SIEVE_API_KEY')
sieve.SIEVE_API_URL = os.getenv('SIEVE_API_URL')

@sieve.Model(
  name="deepface-emotion-detector",
  gpu = True,
  python_packages=[
    "opencv-python==4.6.0.66",
    "tensorflow==2.11.0",
    "pandas==1.5.3",
    "numpy==1.24.2",
    "deepface==0.0.79",
    'mediapipe==0.9.0'
  ],
  python_version="3.8",
)
class EmotionDetector:
    def __setup__(self):
        from deepface import DeepFace
        self.model = DeepFace.build_model('Emotion')
        # Load the weights from the saved H5 file
        self.emotion_labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}
        import mediapipe as mp
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=0.7)

    def detect_faces(self, img: sieve.Image):
        import cv2
        import numpy as np
        results = self.face_detection.process(cv2.cvtColor(img.array, cv2.COLOR_BGR2RGB))
        faces = []
        if results.detections:
            for detection in results.detections:
                bounding_box = detection.location_data.relative_bounding_box
                x = int(bounding_box.xmin * img.width)
                w = int(bounding_box.width * img.width)
                y = int(bounding_box.ymin * img.height)
                h = int(bounding_box.height * img.height)
                
                detected_face = img.array[y : y + h, x : x + w]
                face_array = np.array(detected_face)
                bbox = [x, y, w, h]

                faces.append({
                    "array": face_array,
                    "box": bbox,
                    "class_name": "face",
                    "score": detection.score[0],
                    "frame_number": None if not hasattr(img, "frame_number") else img.frame_number
                })
                
        return faces

    def __predict__(self, img: sieve.Image) -> List:
        import tensorflow as tf
        import numpy as np
        from deepface import DeepFace
        import cv2
        outputs = []
        faces = self.detect_faces(img)
        for face in faces:
            face_img = face['array']
            #preprocess the face image
            if face_img is not None and np.any(face_img):

                gray_face = cv2.cvtColor(face_img, cv2.COLOR_RGB2GRAY)
                resized_face = cv2.resize(gray_face, (48, 48))
                preprocessed_face = tf.keras.applications.resnet50.preprocess_input(resized_face)
                preprocessed_face = np.expand_dims(preprocessed_face, axis=0)

                #predict the emotion of the face image
                emotions = self.model.predict(preprocessed_face)[0]
                labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
                dominant_emotion = np.argmax(emotions)
                emotion_label = self.emotion_labels[dominant_emotion]
                confidence = emotions[dominant_emotion]

                outputs.append({
                    "frame_number": face['frame_number'],
                    "class_name": "face",
                    "box": face["box"],
                    "score": face["score"],
                    "emotion": emotion_label,
                    "confidence": confidence
                })
        
        return outputs



