# AI-Gym-Tracker

This repository contains a Python script that uses the `mediapipe` library along with `opencv` and `streamlit` to provide real-time feedback on the form of various exercises based on body posture detected from a video input.

## Features

- Provides feedback on the form of four different exercises: Push Ups, Squats, Lat Raises, and Bicep Curls.
- Uses Pose Estimation to track key points on the body and calculates angles to assess exercise form.
- Counts the number of correctly performed exercises and provides feedback on the same.
- Interactive user interface built with Streamlit for easy usage and visualization.

## Setup and Usage

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/DiyaMariaAbraham/AI-Gym-Tracker.git

2. Install the required Python packages using 'pip':
   ```sh
   pip install mediapipe streamlit opencv-python
3. Run the script:
   ```sh
   streamlit run app.py
4. Choose the exercise from the drop-down menu and upload a video file of the exercise. The application will process the video, track body posture, and provide real-time feedback on exercise form.

## Supported Exercises
### Push Ups

Tracks arm angles to determine correct push-up form.
Provides feedback on the position of hips.

### Squats
Tracks leg angles to assess squat form.
Provides corrective messages on hip position.

### Lat Raises
Tracks arm angles to evaluate lat raise form.
Offers corrective feedback on arm position.

### Bicep Curls
Monitors arm angles to assess bicep curl form.

## Acknowledgements
This project utilizes the mediapipe library for pose estimation.
The application is built using streamlit for the user interface.
OpenCV (opencv-python) is used for video processing and visualization.

## Future Improvements
Currently, the code only provides accurate results if the angle of video feed is directly at the level of the camera. This can be improved by tweaking the logic of the angles needed to evaluate the individual exercises.


<img width="745" alt="Screenshot 2023-08-09 at 4 49 13 PM" src="https://github.com/DiyaMariaAbraham/AI-Gym-Tracker/assets/93218556/b051ea04-c77c-4028-b3e4-5828547d3dc2">
<img width="649" alt="Screenshot 2023-08-09 at 5 23 05 PM" src="https://github.com/DiyaMariaAbraham/AI-Gym-Tracker/assets/93218556/95fa8b19-300f-4814-b115-05dd8fed96c3">

