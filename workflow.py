import sieve
from typing import Dict,List
import os
from dotenv import load_dotenv
from main import EmotionDetector
from tracker import SORT

load_dotenv()
api_key = os.environ.get('SIEVE_API_KEY')  
sieve.SIEVE_API_KEY = os.getenv('SIEVE_API_KEY')
sieve.SIEVE_API_URL = os.getenv('SIEVE_API_URL')

@sieve.workflow(name="facial-tracking")
def EmotionTracker(video: sieve.Video) -> List:
    video_splitter = sieve.reference("sieve-developer/video-splitter")
    frames = video_splitter(video)
    emotions = EmotionDetector()(frames)
    tracked_emotions = SORT(emotions)

    return tracked_emotions

