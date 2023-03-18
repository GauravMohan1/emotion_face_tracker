# Emotion Tracker

This workflow splits a video into frames, detects faces using the MediaPipe face recognition module, detects emotions using DeepFace on the detected face images, and tracks the objects using the SORT algorithm.

## Deploying
Follow the [getting started guide](https://www.sievedata.com/dashboard/welcome) to get your Sieve API key and install the Sieve Python client.

1. Export API keys & install Python client
```
export SIEVE_API_KEY={YOUR_API_KEY}
pip install https://mango.sievedata.com/v1/client_package/sievedata-0.0.1.1.2-py3-none-any.whl
```

2. Deploy the workflow to Sieve
```
git clone 
cd emotion_face_tracker
sieve deploy
```
