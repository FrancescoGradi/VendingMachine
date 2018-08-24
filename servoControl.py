"""import RPi.GPIO as io
import time

# Impostazioni generali per disposizione pin e visualizzazione di warning selativi ai pin

io.setmode(io.BOARD)
io.setwarnings(False)

# Imposta come attivi i pin che servono

io.setup(7, io.OUT)
io.setup(11, io.OUT)
io.setup(15, io.OUT)

# Inizializzazione dei motori

motorStorage1 = io.PWM(7, 15)
motorStorage2 = io.PWM(11, 15)
motorMechaArm = io.PWM(15, 50)

# Funzioni da chiamare nei vari file per muovere i motori

def moveStorage1():
    motorStorage1.start(7.5)
    motorStorage1.ChangeDutyCycle(2.0)
    time.sleep(0.60)
    motorStorage1.stop()

def moveStorage2():
    motorStorage2.start(7.5)
    motorStorage2.ChangeDutyCycle(2.0)
    time.sleep(0.60)
    motorStorage2.stop()

def moveMechaArm():
    # Ancora abbastanza sperimentale in realtà: appena abbiamo la macchina costruita ci farò delle prove.
    motorMechaArm.start(2.5)
    time.sleep(1)
    motorMechaArm.ChangeDutyCycle(12.5)
    motorMechaArm.stop()
    print("Prelevare la cialda entro 15 secondi.")
    time.sleep(15)
    motorMechaArm.start(12.5)
    time.sleep(1)
    motorMechaArm.ChangeDutyCycle(2.5)
    motorMechaArm.stop()"""
