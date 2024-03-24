import pyautogui
import cv2
import numpy as np
import os
from datetime import datetime

def find_color_on_screen(color, tolerance=10):
    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to an OpenCV image
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Define the lower and upper bounds for the color to search for
    lower_bound = np.array([color[0] - tolerance, color[1] - tolerance, color[2] - tolerance])
    upper_bound = np.array([color[0] + tolerance, color[1] + tolerance, color[2] + tolerance])

    # Find pixels within the specified color range
    mask = cv2.inRange(screenshot_cv, lower_bound, upper_bound)

    # Find contours of the color regions
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, return the coordinates of the center of the largest contour
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        return cx, cy
    else:
        return None

# Example usage
color_to_find = (255, 0, 0)  # For example, search for red color (in BGR format)
tolerance = 10  # Tolerance for color matching

# Find the color on the screen
result = find_color_on_screen(color_to_find, tolerance)
if result:
    print(f"Color found at coordinates: {result}")
else:
    print("Color not found on the screen.")
