#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time

GPIO.setwarnings(False)
GPIO.cleanup()

triggerPin=40
echoPin=38
buzzerPin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

GPIO.output(triggerPin,0)
time.sleep(1)

def mesafeOku():
    GPIO.output(triggerPin,1)
    time.sleep(1)

    basla=0
    bitis=0

    GPIO.output(triggerPin,0)

    while GPIO.input(echoPin) !=1:
        basla = time.time()

    while GPIO.input(echoPin) ==1:
        bitis=time.time()

    

toplam_zaman=bitis-basla

    mesafe=340.29e2*toplam_zaman/2

    print "Sesin havada geçirdiği süre: ", toplam_zaman
    print "Mesafe: ",mesafe

    if(mesafe < 15 and mesafe > 10):
        GPIO.output(3,1)
        GPIO.output(buzzerPin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(buzzerPin, GPIO.LOW)
        GPIO.output(3,0)
       
        
    elif(mesafe < 10):
        GPIO.output(3,1)
        GPIO.output(buzzerPin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(buzzerPin, GPIO.LOW)
        GPIO.output(3,0)
    else:
        GPIO.output(3,0)

    return mesafe

for i in range(100):
    print mesafeOku()
