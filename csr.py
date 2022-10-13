import numpy as np
import pyautogui
import cv2
def screen():
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	cv2.imwrite("screen.png", image)
