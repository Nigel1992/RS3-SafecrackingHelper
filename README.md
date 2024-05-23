# SafeCracking Helper
SafeCracking Helper is a Python script that assists in cracking safes by monitoring the area around the mouse cursor on your screen and playing a sound if it detects a specific color within a defined tolerance.

## Installation
1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required libraries using pip: pip install pillow playsound pyautogui

## Usage
1. Clone this repository to your local machine or download the script directly.
2. Navigate to the directory where the script is located.
3. Run the script by executing the following command in your terminal or command prompt: python SafeCracking_Helper.py
4. Once the script is running, move your mouse cursor around the screen. If the color around the cursor matches the specified color within the defined tolerance, a sound will be played.

## Customization
You can customize the behavior of the script by modifying the following variables:

- `color_to_find`: The RGB color code that the script will search for.
- `tolerance`: The tolerance level for color matching. Adjust this value to make the color matching more or less strict.
- `search_area`: The size of the area around the mouse cursor to capture for color detection. Increasing this value will increase the area searched, but may impact performance.

## Dependencies
- [Pillow](https://python-pillow.org/): Python Imaging Library (Fork)
- [playsound](https://pypi.org/project/playsound/): Pure Python, cross-platform, single function module with no dependencies for playing sounds.
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/): PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
