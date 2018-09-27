import RPi.GPIO as io
import time

io.setmode(io.BOARD)
io.setwarnings(True)

# Movimento storage 1 (SX)
def moveStor1(msg):
    io.setmode(io.BOARD)
    io.setup(11, io.OUT)
    motorStor1 = io.PWM(11, 50)
    if msg == True:
        print("Erogating Arabic capsule")
    motorStor1.start(2.5)
    motorStor1.ChangeDutyCycle(7.5)
    time.sleep(0.12)
    motorStor1.ChangeDutyCycle(0)
    time.sleep(0.1)
    motorStor1.ChangeDutyCycle(15)
    time.sleep(0.16)
    motorStor1.stop()
    io.cleanup()
    
# Movimento storage 2 (DX)
def moveStor2(msg):
    io.setmode(io.BOARD)
    io.setup(12, io.OUT)
    motorStor2 = io.PWM(12, 70)
    if msg == True:
        print("Erogating Classic capsule")
    motorStor2.start(12.5)
    motorStor2.ChangeDutyCycle(7.5)
    time.sleep(0.13)
    motorStor2.ChangeDutyCycle(0)
    time.sleep(0.1)
    motorStor2.ChangeDutyCycle(2)
    time.sleep(0.2)
    motorStor2.stop()
    io.cleanup()

# Movimento braccio
def moveArm(msg):
    io.setmode(io.BOARD)
    io.setup(15, io.OUT)
    motorArm = io.PWM(15, 30)
    motorArm.start(12.5)
    motorArm.ChangeDutyCycle(7.5)
    time.sleep(0.25)
    motorArm.stop()
    if msg == True:
        print("Please take the capsule within the next 10 seconds.")
        time.sleep(5)
    else:
        time.sleep(1)
    motorArm.start(7.5)
    motorArm.ChangeDutyCycle(2.5)
    time.sleep(0.2)
    motorArm.stop()
    io.cleanup()

def getCapsule(type, msg=True):
    if type == 1:
        moveStor1(msg)
    elif type == 2:
        moveStor2(msg)
    if msg == True:
        time.sleep(2.5)
        moveArm(msg)

def systemCheck():
    print("Checking motors...")
    time.sleep(0.2)
    print("Performing Left Motor check")
    time.sleep(0.5)
    try:
        getCapsule(1, False)
        time.sleep(1)
        print("Left Motor status: OK")
    except KeyboardInterrupt:
        time.sleep(0.3)
        print("Something's wrong with Left Motor")
    time.sleep(0.2)
    print("Performing Right Motor check")
    time.sleep(0.5)
    try:
        getCapsule(2, False)
        time.sleep(1)
        print("Right Motor status: OK")
    except KeyboardInterrupt:
        time.sleep(0.3)
        print("Something's wrong with Right Motor")
    time.sleep(0.2)
    print("Performing Arm Motor check")
    time.sleep(0.5)
    try:
        moveArm(False)
        time.sleep(1)
        print("Arm Motor status: OK")
    except KeyboardInterrupt:
        time.sleep(0.3)
        print("Something's wrong with Arm Motor")

systemCheck()
