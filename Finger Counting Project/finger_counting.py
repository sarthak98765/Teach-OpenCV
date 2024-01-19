import cv2
import mediapipe as mp  # download mediapipe package (pip install mediapipe)
import time

# Create an alias for the drawing utilities module within the mediapipe library
mp_draw = mp.solutions.drawing_utils
# Create an alias for the hands module within the mediapipe library
mp_hand = mp.solutions.hands
tipIds = [4, 8, 12, 16, 20]

# Open a connection to the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Set up the hands module with specified confidence thresholds
with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        # Convert the frame from BGR to RGB color format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False

        # Process the frame to detect and track hand landmarks
        results = hands.process(frame)

        # Make the frame writable again and convert it back to BGR for display
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # List to store hand landmark information
        lmList = []

        # Check if hand landmarks are detected
        if results.multi_hand_landmarks:
            # Iterate through each detected hand landmark
            for hand_landmark in results.multi_hand_landmarks:
                # Extract the landmarks of the first detected hand
                myHands = results.multi_hand_landmarks[0]

                # Enumerate through each landmark and store its information
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])

                # Draw landmarks and connections on the frame
                mp_draw.draw_landmarks(frame, hand_landmark, mp_hand.HAND_CONNECTIONS)

        # List to store finger states (extended or not)
        fingers = []

        # Check if there is any hand landmark information
        if len(lmList) != 0:
            # Check if the thumb is extended based on landmark positions
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Check if each of the other four fingers is extended
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # Count the total number of extended fingers
            total = fingers.count(1)

            # Display the finger count on the frame
            if total == 0:
                cv2.putText(frame, "No Finger", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
            else:
                cv2.putText(frame, f"{total} Finger", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Check for the 'q' key press to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

# Release the video capture object
cap.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
