import pyautogui
import time


def get_status():
	print(pyautogui.position())
	print(pyautogui.size())


for i in range(3):
	pyautogui.moveTo(356, 313, duration=2)
	pyautogui.click(button="left")
	pyautogui.moveTo(531, 306, duration=2)
	pyautogui.click(button="left")