# Finger Counting Model with OpenCV and Mediapipe
This OpenCV application utilizes the Mediapipe library to enable real-time finger counting using a webcam.

### **Prerequisites:**
Ensure you have the following dependencies installed:

1. Python
2. OpenCV
3. Mediapipe

### **How to Use:**
1. Clone or download the repository.

2. Open the terminal and navigate to the project directory.

3. Run the following command to start the finger counting application:
`python finger_count.py`
4. The webcam will activate, and the application will display the video feed with finger counting information.
### **Understanding the Code:**
- finger_count.py: This script is the main application. It captures the webcam feed, processes hand landmarks using Mediapipe, and counts the extended fingers.

- mediapipe: The application utilizes the mediapipe library for hand tracking and landmark detection

### **Tips:**
1. Hand Placement: Ensure your hand is well-lit and positioned properly in the webcam frame for accurate finger counting.

2. Finger Detection: The model counts fingers based on the positions of specific landmarks. Make sure your fingers are adequately separated for accurate counting.

3. Environment: Consider the lighting conditions and background to enhance the model's performance.

**Acknowledgments:**
This application is built using OpenCV and Mediapipe, which are powerful tools for computer vision and hand tracking.

Feel free to customize this README further based on additional details or specific instructions for your application.