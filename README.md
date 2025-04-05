Temple Run Gesture Control
This project allows you to control the Temple Run game using your hand gestures.
It detects swipe gestures through your webcam and simulates arrow key presses to play the game.

Step 1: Requirements
- Python 3.7 or higher
- A working webcam
- Android emulator (BlueStacks or NoxPlayer)
- Temple Run game installed on the emulator

Step 2: Install Required Libraries
Open your terminal or command prompt and run:
pip install opencv-python mediapipe pyautogui pygetwindow

Step 3: Project Files
This project contains:
- temple_gesture_control.py  (Main script)
- README.md  (Instructions)
Keep both files in one folder.

Step 4: Set Up the Emulator
1. Install BlueStacks or NoxPlayer.
2. Open the emulator and install Temple Run from the Play Store.
3. Launch the game and keep it open on the home screen or in gameplay mode.

Step 5: Run the Gesture Controller Script
1. Open a terminal inside the project folder.
2. Run the script using:
python temple_gesture_control.py
3. Your webcam will start, and a live video window will appear.

Step 6: Hand Gesture Controls
Use your hand to perform these actions in front of the webcam:

- Swipe Left  →  Move Left in the game
- Swipe Right →  Move Right in the game
- Swipe Up    →  Jump
- Swipe Down  →  Slide
  
Make sure only one hand is visible and perform the gestures clearly.

Step 7: Notes
- The script automatically finds and activates the emulator window.
- If you're using NoxPlayer, change "BlueStacks" to "Nox" in the code.
- You can tweak gesture sensitivity by editing the movement threshold in the script.



