import serial # Serial library use to connect python3 and arduino
from serial import Serial
import pyautogui # pyautogui library will be use to perform arrow function

arduino = serial.Serial('/dev/ttyUSB0', 9600)

i = 0

while True:
  incoming_Data = arduino.readline() #readline() function will get data from serial monitor line by line

  if 'up' in incoming_Data.decode('utf-8'): 
  	pyautogui.press('up')
  	incoming_Data = ""
  	continue
  elif 'down' in incoming_Data.decode('utf-8'):
  	pyautogui.keyDown('down')
  	incoming_Data = ""
  	i = 1
  	continue

  if i == 1:
  	pyautogui.press('up')

  i = 0

  incoming_Data = ""
