from gpiozero import Button
from signal import pause
import os


def send2pd(message=''):
    os.system("echo '" + message + "' | pdsend 3000")

def but1_on():
    print("Button 1: Down")
    message = 'but1 5;'
    send2pd(message)

def but2_on():
    print("Button 2: Down")
    message = 'but2 1;'
    send2pd(message)

button1 = Button(17)
button2 = Button(27)

button1.when_pressed = but1_on
button2.when_pressed = but2_on

pause()

