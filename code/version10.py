#pip install inputs maybe???
#pip3 install pynput
#https://pypi.org/project/pynput/
from pynput import keyboard
import board
import digitalio
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
import time
import random

global total_letters
global line_pos
global line # which line the command prompt is on

def on_press(key):
    global total_letters
    global line_pos
    global line
    
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        letter = (key.char) # single letter
        print (letter)
        
        with canvas(device) as draw:

            #program needs to remember previous letters
            total_letters = total_letters + letter
        
            #display the letter       
            draw.text((0, line_pos), total_letters, fill="white")
            line += 1
            print (line)
                        
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        
        letter = " "
               
        with canvas(device) as draw:

            #program needs to remember previous letters
            total_letters = total_letters + letter
        
            #display the letter       
            draw.text((0, line_pos), total_letters, fill="white")

def on_release(key):
    #print('{0} released'.format(key))
    #print ({0}.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
        '''ADD SOMETING THAT SAYS GOOD BYE'''

line_pos =  0
total_letters = " "
line = 0

# set up button
from gpiozero import Button
button = Button(21)

# set up oled 
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
oled_reset = digitalio.DigitalInOut(board.D4)
retro_screen = sh1106(serial_interface=0, width=128, height=64, rotate=0, reset=oled_reset)
WIDTH = 132
HEIGHT = 64 # Change to 32 depending on your screen resolution



with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


#letter = input("Please Enter Your Letter")
# display press the ready button
    

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()    

