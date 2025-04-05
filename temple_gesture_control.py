import cv2
import mediapipe as mp
import pyautogui
import pygetwindow as gw
import time

# Initialize webcam and MediaPipe
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

# Previous hand coordinates
prev_x, prev_y = 0, 0
last_gesture_time = time.time()

# Function to focus the emulator window
def focus_emulator():
    for window in gw.getWindowsWithTitle('BlueStacks'):  # Change to 'Nox' if you're using NoxPlayer
        try:
            window.activate()
            break
        except:
            pass  # If window is minimized or can't be activated

# Detect direction of hand movement with better sensitivity
def detect_gesture(dx, dy):
    if abs(dx) > abs(dy):
        if dx > 0.05:
            return 'right'
        elif dx < -0.05:
            return 'left'
    else:
        if dy < -0.05:
            return 'up'
        elif dy > 0.05:
            return 'down'
    return 'none'

# Simulate key press
def send_key(gesture):
    focus_emulator()
    if gesture == 'left':
        pyautogui.press('left')
    elif gesture == 'right':
        pyautogui.press('right')
    elif gesture == 'up':
        pyautogui.press('up')
    elif gesture == 'down':
        pyautogui.press('down')

# Main loop
while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            x = hand.landmark[9].x
            y = hand.landmark[9].y

            dx = x - prev_x
            dy = y - prev_y

            gesture = detect_gesture(dx, dy)

            if gesture != 'none' and (time.time() - last_gesture_time > 1):
                print(f"Gesture: {gesture}")
                send_key(gesture)
                last_gesture_time = time.time()

            prev_x, prev_y = x, y

            # Visual feedback on screen
            cv2.putText(frame, f"Gesture: {gesture}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Gesture Control - Temple Run", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
