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
git clone git@github.com:GauravMohan1/emotion_face_tracker.git
cd emotion_face_tracker
sieve deploy
```

3. Example Input and Output:

Input: http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4

Output:
[
  {
    "2d76f41b-a13c-48e4-a012-f405852140a3": [
      {
        "frame_number": 85,
        "box": [
          367,
          367,
          674,
          122
        ],
        "class": "face",
        "emotion": "surprise"
      }
    ],
    "c40a7eea-f1be-4101-b526-1fc10a623781": [
      {
        "frame_number": 91,
        "box": [
          284,
          284,
          665,
          175
        ],
        "class": "face",
        "emotion": "surprise"
      }
    ],
    "5b74854d-6e76-495c-abc3-b114a9c6c1a2": [
      {
        "frame_number": 110,
        "box": [
          327,
          54,
          424,
          424
        ],
        "class": "face",
        "emotion": "surprise"
      }
    ],
    "2c558d83-80b8-42ca-a5f1-3ecc3b0ff1d6": [
      {
        "frame_number": 86,
        "box": [
          265,
          265,
          570,
          197
        ],
        "class": "face",
        "emotion": "neutral"
      }
    ],
    "a479eb79-2044-4be2-af51-10e17695dae2": [
      {
        "frame_number": 88,
        "box": [
          261,
          261,
          566,
          259
        ],
        "class": "face",
        "emotion": "neutral"
      }
    ],
    "787b71b9-6a56-4762-b2f2-401b3a2358e4": [
      {
        "frame_number": 90,
        "box": [
          238,
          238,
          567,
          314
        ],
        "class": "face",
        "emotion": "neutral"
      }
    ],
    "a06ee0cb-c43b-487e-9ae6-f313663bccbd": [
      {
        "frame_number": 87,
        "box": [
          251,
          251,
          558,
          239
        ],
        "class": "face",
        "emotion": "sad"
      }
    ],
    "31afd343-9eb6-426a-945c-6eaea6ea8041": [
      {
        "frame_number": 92,
        "box": [
          435,
          435,
          495,
          93
        ],
        "class": "face",
        "emotion": "sad"
      }
    ],
    "5e322e32-3ec2-46f5-9cfe-3feccdadd3c3": [
      {
        "frame_number": 117,
        "box": [
          454,
          165,
          528,
          528
        ],
        "class": "face",
        "emotion": "sad"
      }
    ],
    "f8f90a75-9ae3-48d9-8b1b-25b4571b88ef": [
      {
        "frame_number": 89,
        "box": [
          254,
          254,
          563,
          278
        ],
        "class": "face",
        "emotion": "happy"
      }
    ],
    "6a66d659-fdad-40ee-87ca-4e0f88fb8352": [
      {
        "frame_number": 105,
        "box": [
          234,
          234,
          735,
          362
        ],
        "class": "face",
        "emotion": "happy"
      }
    ],
    "5d9dfdbf-c2be-4df5-9da8-2cf7e0054dcc": [
      {
        "frame_number": 140,
        "box": [
          249,
          249,
          661,
          258
        ],
        "class": "face",
        "emotion": "happy"
      }
    ],
    "590ccf73-38a5-4818-a9f0-ce88fde2ced7": [
      {
        "frame_number": 110,
        "box": [
          213,
          213,
          979,
          132
        ],
        "class": "face",
        "emotion": "fear"
      }
    ],
    "ef5f42f6-463c-4dd0-aea3-c7c6bb2ef6e0": [
      {
        "frame_number": 120,
        "box": [
          405,
          405,
          567,
          82
        ],
        "class": "face",
        "emotion": "fear"
      }
    ],
    "d9b55b34-53f3-4c29-b8c3-2bc68e73214f": [
      {
        "frame_number": 135,
        "box": [
          319,
          319,
          552,
          203
        ],
        "class": "face",
        "emotion": "fear"
      }
    ],
    "761ff415-5042-41ad-8c80-2ed559e6df1c": [
      {
        "frame_number": 126,
        "box": [
          235,
          6,
          572,
          572
        ],
        "class": "face",
        "emotion": "angry"
      }
    ],
    "9aff9472-512c-4cf8-9ba6-e379c609a196": [
      {
        "frame_number": 221,
        "box": [
          516,
          257,
          619,
          619
        ],
        "class": "face",
        "emotion": "angry"
      }
    ]
  }
]
