# Volume-Control-Gesturing
Volume Control Gesturing is an innovative system Volume Management Tool that allows you to adjust audio levels with intuitive visual feedback. Control your system's audio levels effortlessly through gestures, making volume adjustments a seamless and engaging experience.

## Logic 🧠
Using your system's visual feed, A Convolution Neural Network Model tracks hand movement for every frame. Once a hand is detected, the distance between the tips on index finger and thumb are calculated and on the basis of change in distance in current frame versus the last frame, the current volume is increased or decreased on that basis.

The program does not prefer a specific hand, the hand present in previous frame will be continued to be noticed.

## Run 🏃
`python Volume_Control.py`

## Installations 📦
* For CVzone `python -m pip install cvzone`
* For cv2 `python -m pip install cv2`
* For Colorama `python -m pip install colorama`
* For Termcolor `python -m pip install termcolor`
* For Pyautogui `python -m pip install pyautogui`
