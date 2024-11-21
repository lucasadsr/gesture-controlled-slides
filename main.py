import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

cap = cv2.VideoCapture(0)

last_action_time = time.time()
action_interval = 1.0

def count_raised_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    finger_dips = [6, 10, 14, 18]
    raised_fingers = 0

    for tip, dip in zip(finger_tips, finger_dips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            raised_fingers += 1

    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    if thumb_tip.x < thumb_ip.x:
        raised_fingers += 1

    return raised_fingers

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_up = count_raised_fingers(hand_landmarks)

            current_time = time.time()
            if current_time - last_action_time > action_interval:
                if fingers_up == 5:
                    pyautogui.press('right')
                    last_action_time = current_time
                elif fingers_up == 0:
                    pyautogui.press('left')
                    last_action_time = current_time

    cv2.imshow('Gesture-Controlled Slides', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
