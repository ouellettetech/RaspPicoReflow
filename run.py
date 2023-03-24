from machine import Pin,PWM
import time
from picolcd.picolcd import *
from encodermenu.lcd_menu import *

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9


print("hello world")

currentMenuItem=0
numMenuItems=4
lastButton=-1

pwm = PWM(Pin(BL))
pwm.freq(1000)
pwm.duty_u16(32768)#max 65535
keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)

keyUp = Pin(2 ,Pin.IN,Pin.PULL_UP)#UP
keyCenter = Pin(3 ,Pin.IN,Pin.PULL_UP)#CENTER
keyLeft = Pin(16 ,Pin.IN,Pin.PULL_UP)#LEFT
keyDown = Pin(18 ,Pin.IN,Pin.PULL_UP)#DOWN
keyRight = Pin(20 ,Pin.IN,Pin.PULL_UP)#RIGHT

LCD = LCD_1inch14()
Menu = LCD_Menu(LCD)

Menu.initMenu(LCD.black, LCD.green, LCD.white)
Menu.display(0,"Main Menu","Select Profile","...","...","Start!")
Menu.initKeys(keyA,keyB,keyUp,keyDown)

Menu.run()


time.sleep(1)
LCD.fill(0xFFFF)



