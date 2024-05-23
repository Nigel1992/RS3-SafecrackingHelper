from PIL import ImageGrab
from playsound import playsound
import pyautogui
import time

# Hex color to look for and tolerance for color matching
color_to_find = (24, 219, 24)  # RGB equivalent of #18db18
tolerance = 30  # Adjust tolerance as needed

def similar_color(c1, c2):
    # Check if two colors are similar within the tolerance
    return all(abs(c1[i] - c2[i]) <= tolerance for i in range(3))

def find_similar_color_around_mouse():
    # Get the current mouse position
    x, y = pyautogui.position()
    # Define the area to search around the mouse (e.g., 50x50 pixels)
    search_area = 10

    # Grab a screenshot of the area around the mouse
    screenshot = ImageGrab.grab(bbox=(x - search_area, y - search_area, x + search_area, y + search_area))
    pixels = screenshot.load()

    # Search for similar colors within the screenshot
    for i in range(screenshot.width):
        for j in range(screenshot.height):
            if similar_color(pixels[i, j], color_to_find):
                return True
    return False

# Main loop
while True:
    if find_similar_color_around_mouse():
        # Play sound if a similar color is found
        playsound('sound.mp3')
    # Pause for 1 millisecond before checking again
    time.sleep(0.001)
