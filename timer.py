import os
import time

hours = 0
minutes = 0
seconds = 0

start = raw_input("Enter r to run the program: ") 

while start.lower() =="r":
    if seconds >= 60:
        seconds = 0 #restes the seconds
        minutes = minutes + 1
    if minutes >=60:
        minutes = 0
        hours = hours + 1
    os.system('clear') #for windows use cls

    seconds = (seconds + .1)
    print (hours,":", minutes,":", seconds)
    time.sleep(.1) #every .1 seconds it will go back up and clear the screen
