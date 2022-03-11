# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# # Set pin 11 as an output, and define as servo1 as PWM pin
# GPIO.setup(11,GPIO.OUT)
# servo0 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

# # Set pin 13 as an output, and define as servo1 as PWM pin
# GPIO.setup(13,GPIO.OUT)
# servo1 = GPIO.PWM(13,50) # pin 11 for servo1, pulse 50Hz

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
servo = [GPIO.PWM(11,50),GPIO.PWM(13,50)]

# Start PWM running, with value of 0 (pulse off)
servo[0].start(0)
servo[1].start(0)

duty = [7,7]
# set to 90 initial

servo[0].ChangeDutyCycle(duty[0])
time.sleep(0.5)
servo[0].ChangeDutyCycle(0)

servo[1].ChangeDutyCycle(duty[1])
time.sleep(0.5)
servo[1].ChangeDutyCycle(0)


# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)

try:
    while True:
        #Ask user for duty value and turn servo to it
        # duty = float(input('Enter angle between 2 & 12: '))
        # servo1.ChangeDutyCycle(duty)
        # time.sleep(0.5)
        # servo1.ChangeDutyCycle(0)

        # #Ask user for angle and turn servo to it    
        # angle = float(input('Enter angle between 0 & 180: '))
        # servo1.ChangeDutyCycle(2+(angle/18))
        # time.sleep(0.5)
        # servo1.ChangeDutyCycle(0)
        snum, dir = input("Enter two numbers here: ").split()
        snum = int(snum)

        if dir == "CW" and duty[snum]<=7:
            duty[snum]+=5
            servo[snum].ChangeDutyCycle(duty[snum])
            time.sleep(0.5)
            servo[snum].ChangeDutyCycle(0)
        if dir == "CCW" and duty[snum]>=7:
            duty[snum]-=5
            servo[snum].ChangeDutyCycle(duty[snum])
            time.sleep(0.5)
            servo[snum].ChangeDutyCycle(0)





finally:
    #Clean things up at the end
    servo[0].stop()
    servo[1].stop()
    GPIO.cleanup()
    print("Goodbye!")

