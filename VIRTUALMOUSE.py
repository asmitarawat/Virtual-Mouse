import cv2
import mediapipe as mp
import pyautogui
from math import sqrt
drawing_utils = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

prev_left_click = False
prev_right_click = False

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        continue
    
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(rgb_image)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            drawing_utils.draw_landmarks(frame, hand_landmarks)
            
            index_finger_x = int(hand_landmarks.landmark[8].x * frame.shape[1])
            index_finger_y = int(hand_landmarks.landmark[8].y * frame.shape[0])
            thumb_x = int(hand_landmarks.landmark[4].x * frame.shape[1])
            thumb_y = int(hand_landmarks.landmark[4].y * frame.shape[0]) 
            
            screen_width, screen_height = pyautogui.size()
            mouse_x = int(index_finger_x * screen_width / frame.shape[1])
            mouse_y = int(index_finger_y * screen_height / frame.shape[0])
            
            distance = sqrt((thumb_x - index_finger_x)**2 + (thumb_y - index_finger_y)**2)
            if distance < 30:
                if not prev_left_click:
                    pyautogui.click(button='left')
                    prev_left_click = True
            else:
                prev_left_click = False
            
            if thumb_x > index_finger_x and distance > 100:
                if not prev_right_click:
                    pyautogui.click(button='right')
                    prev_right_click = True
            else:
                prev_right_click = False
            
            pyautogui.moveTo(mouse_x, mouse_y)
            
            cv2.circle(img=frame, center=(index_finger_x,index_finger_y), radius=10, color=(0, 255, 255))
            cv2.circle(img=frame, center=(thumb_x,thumb_y), radius=10, color=(0, 255, 255))
    
    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

