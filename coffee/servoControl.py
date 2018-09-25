import RPi.GPIO as io
import time

io.setmode(io.BOARD)
io.setwarnings(True)
#io.setup(15, io.OUT)
#io.setup(12, io.OUT)
#io.setup(11, io.OUT)

#motorStor1 = io.PWM(11, 50)
#motorStor2 = io.PWM(12, 70)
#motorArm = io.PWM(15, 15)

"""La definizione delle funzioni è corretta (tutto fa quel che deve, esattamente
   come deve... il problema sta nel test in fondo"""

# Movimento storage 1 (SX)
def moveStor1():
    io.setmode(io.BOARD)
    io.setup(11, io.OUT)
    motorStor1 = io.PWM(11, 50)
    print("Fornisco cialda tipo 1")
    motorStor1.start(2.5)
    motorStor1.ChangeDutyCycle(7.5)
    time.sleep(0.1)
    motorStor1.ChangeDutyCycle(0)
    time.sleep(0.1)
    motorStor1.ChangeDutyCycle(15)
    time.sleep(0.11)
    motorStor1.stop()
    io.cleanup()
    
# Movimento storage 2 (DX)
def moveStor2():
    io.setmode(io.BOARD)
    io.setup(12, io.OUT)
    motorStor2 = io.PWM(12, 70)
    print("Fornisco cialda tipo 2")
    motorStor2.start(12.5)
    motorStor2.ChangeDutyCycle(7.5)
    time.sleep(0.12)
    motorStor2.stop()
    time.sleep(0.1)
    motorStor2.start(7.5)
    motorStor2.ChangeDutyCycle(2)
    time.sleep(0.14)
    motorStor2.stop()
    io.cleanup()

# Movimento braccio
def moveArm():
    io.setmode(io.BOARD)
    io.setup(15, io.OUT)
    motorArm = io.PWM(15, 15)
    motorArm.start(12.5)
    motorArm.ChangeDutyCycle(7.5)
    time.sleep(0.9)
    motorArm.stop()
    print("Ritirare la cialda entro 10 secondi.")
    time.sleep(5)
    motorArm.start(7.5)
    motorArm.ChangeDutyCycle(2.5)
    time.sleep(0.17)
    motorArm.stop()
    io.cleanup()

def getCapsule(type):
    if type == 1:
        moveStor1()
    elif type == 2:
        moveStor2()
    time.sleep(2.5)
    moveArm()

"""Praticamente chiamando una singola funzione tutto procede come dovrebbe. Se
   si avvia un test con getCapsule(1), si attende la fine e poi si avvia lo
   stesso test con getCapsule(2), tutto funziona. Se chiamo in sequenza le due
   funzioni, invece, motorStor1 e motorStor2 funzionano bene, mentre motorArm
   (che viene chiamato due volte) la seconda volta si ferma. Possibile che
   abbia sbagliato ad inizializzare qualcosa?"""
"""x = 0
while(x < 10):
    getCapsule(1)
    time.sleep(1)
    getCapsule(2)
    time.sleep(1)
    x = x+1"""
