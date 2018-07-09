import RPi.GPIO as GPIO                    #Import GPIO library
import time

#Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    # programming the GPIO by BCM pin numbers

TRIG = 17
ECHO = 27
led = 22

m11=16
m12=12
m21=21
m22=20

GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input
GPIO.setup(led,GPIO.OUT)                  

GPIO.setup(m11,GPIO.OUT)
GPIO.setup(m12,GPIO.OUT)
GPIO.setup(m21,GPIO.OUT)
GPIO.setup(m22,GPIO.OUT)


 
GPIO.output(led, 1)

time.sleep(5)

def stop():
    print 'stop'
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

def forward():
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print 'Forward'

def back():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    print 'back'

def left():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    print 'left'

def right():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
    print "right"

def dist():
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    time.sleep(0.1)                                   #Delay

    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                           #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    
    while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
        GPIO.output(led, False)             
    pulse_start = time.time()

    while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH
        GPIO.output(led, False) 
    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor

    distance = pulse_duration* 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
    distance = round(distance,2)                 #Round to two decimal points
    return distance

p=0
count=0
forward()
while True:

    if(p==1):
        stop()
	
	now = time.time()
        while(time.time()<=now+1.2):
	     left()
        stop()  
        now = time.time()
        
        while(time.time()<=now+0.7):
	     back()      
	print 'park'
	stop()
        break
    distance=dist()
    
    if(distance>30):
       
        now = time.time()
        while(time.time()<=now+0.3):
             distance=dist()
             print distance    
             if(distance<30):
                  p=0
                  break
             p=1


    
   	   
 
	
  
