from machine import Pin,SPI,PWM
import framebuf
import time
from library.library import *
from picolcd.picolcd import *
BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9


print("hello world")
printhi()

currentMenuItem=0
numMenuItems=4
lastButton=-1

def drawMenu():
    LCD.text("Main Menu",90,40,LCD.green)
    LCD.text("Select Profile",90,60,LCD.green)
    LCD.text("...",90,80,LCD.green)
    LCD.text("Start!",90,100,LCD.green)


    LCD.text("OK",210,15,LCD.white)
    LCD.text("BACK",195,110,LCD.white)

pwm = PWM(Pin(BL))
pwm.freq(1000)
pwm.duty_u16(32768)#max 65535

LCD = LCD_1inch14()
#color BRG
LCD.fill(LCD.black)

LCD.show()
drawMenu()


    
    
LCD.hline(10,10,220,LCD.blue)
LCD.hline(10,125,220,LCD.blue)
LCD.vline(10,10,115,LCD.blue)
LCD.vline(230,10,115,LCD.blue)


LCD.show()
keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)

key2 = Pin(2 ,Pin.IN,Pin.PULL_UP)#UP
key3 = Pin(3 ,Pin.IN,Pin.PULL_UP)#CENTER
key4 = Pin(16 ,Pin.IN,Pin.PULL_UP)#LEFT
key5 = Pin(18 ,Pin.IN,Pin.PULL_UP)#DOWN
key6 = Pin(20 ,Pin.IN,Pin.PULL_UP)#RIGHT

while(1):
    if(keyA.value() == 0):
        if(lastButton != 0):
            LCD.rect(208,12,20,20,LCD.green)
            print("A")
            lastButton = 0
    else :
        if(lastButton == 0 ):
            lastButton = -1
        LCD.rect(208,12,20,20,LCD.white)
        
        
    if(keyB.value() == 0):
        if(lastButton != 1):
            LCD.rect(193,103,35,20,LCD.green)
            print("B")
            lastButton = 1
    else :
        if(lastButton == 1):
            lastButton = -1
        LCD.rect(193,103,35,20,LCD.white)

    if(key2.value() == 0):#上
        if(lastButton != 2):
            LCD.fill_rect(37,35,20,20,LCD.red)
            print("UP")
            currentMenuItem-=1
            currentMenuItem=currentMenuItem%numMenuItems
            print(currentMenuItem)
            lastButton = 2
    else :
        if(lastButton == 2):
            lastButton = -1
        LCD.fill_rect(37,35,20,20,LCD.white)
        LCD.rect(37,35,20,20,LCD.red)
        
        
    if(key3.value() == 0):#中
        if(lastButton != 3):
            LCD.fill_rect(37,60,20,20,LCD.red)
            print("CTRL")
            lastButton = 3
    else :
        if(lastButton == 3):
            lastButton = -1
        LCD.fill_rect(37,60,20,20,LCD.white)
        LCD.rect(37,60,20,20,LCD.red)
        
    

    if(key4.value() == 0):#左
        if(lastButton != 4):
            LCD.fill_rect(12,60,20,20,LCD.red)
            print("LEFT")
            lastButton = 4
    else :
        if(lastButton == 4):
            lastButton = -1
        LCD.fill_rect(12,60,20,20,LCD.white)
        LCD.rect(12,60,20,20,LCD.red)
        
        
    if(key5.value() == 0):#下
        if(lastButton != 5):
            LCD.fill_rect(37,85,20,20,LCD.red)
            print("DOWN")
            currentMenuItem+=1
            currentMenuItem=currentMenuItem%numMenuItems
            print(currentMenuItem)
            lastButton = 5
    else :
        if(lastButton == 5):
            lastButton = -1
        LCD.fill_rect(37,85,20,20,LCD.white)
        LCD.rect(37,85,20,20,LCD.red)
        
        
    if(key6.value() == 0):#右
        if(lastButton != 6):
            LCD.fill_rect(62,60,20,20,LCD.red)
            print("RIGHT")
            lastButton = 6
    else :
        if(lastButton == 6):
            lastButton = -1
        LCD.fill_rect(62,60,20,20,LCD.white)
        LCD.rect(62,60,20,20,LCD.red)

        
    LCD.show()
time.sleep(1)
LCD.fill(0xFFFF)



