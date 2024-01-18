# OpenCV Face Recognition
This OpenCV application enables real-time face detection and recognition using a webcam.

**Prerequisites:**
Ensure you have the following dependencies installed:

- Python
- opencv-python
- opencv-contrib-python
- datetime
- NumPy 


**Dataset Creation**:
1. Open create_data.py. 
2. Change the path of "haar_file" and "datasets" below to the location where these files are on your machine
3. Change the "name" variable to the name of the person whose face you want to store.
Run create_data.py and follow on-screen instructions. Ensure good lighting and multiple face angles for better results.
Face Recognition 
4. Run face_detection.py.
Look into the camera in the same position as during dataset creation.
The application will detect and recognize your face in real-time.


**Tips**:

1. Create multiple sub-datasets with different lighting, angles, etc., to increase recognition accuracy.

2. Ensure your face recognition environment matches the conditions during dataset creation.

3. Adjust the number of pictures per name in create_data.py for better recognition.