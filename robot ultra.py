from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

m11=18
m12=23
m21=24
m22=25
light=12

Trig = 21          # Entree Trig du HC-SR04 branchee au GPIO 23
Echo = 20      # Sortie Echo du HC-SR04 branchee au GPIO 24
distance=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.setup(light,GPIO.OUT)
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)
GPIO.output(m11 , 0)
GPIO.output(m12 , 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)
GPIO.output(light,0)
GPIO.output(Trig, False)
print "DOne"

def distance():
   
     GPIO.output(Trig, True)
     time.sleep(0.00001)
     GPIO.output(Trig, False)
     while GPIO.input(Echo)==0:  ## Emission de l'ultrason
      debutImpulsion = time.time()
     while GPIO.input(Echo)==1:   ## Retour de l'Echo
      finImpulsion = time.time()
     distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s
     print "La distance est de : ",distance," cm"
     return(distance)
     
	 
    
    
a=1
@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    GPIO.output(m11 , 1)
    GPIO.output(m12 , 0)
    GPIO.output(m21 , 0)
    GPIO.output(m22 , 1)
    return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   return 'true'

@app.route('/up_side')
def up_side():
    if distance ()> 20 :  
       data1="FORWARD"
       GPIO.output(m11 , 0)
       GPIO.output(m12 , 1)
       GPIO.output(m21 , 0)
       GPIO.output(m22 , 1)
       
       return 'true'
    else :
        GPIO.output(m11 , 1)
        GPIO.output(m12 , 0)
        GPIO.output(m21 , 1)
        GPIO.output(m22 , 0)
        time.sleep(0.5)
        GPIO.output(m11 , 0)
        GPIO.output(m12 , 0)
        GPIO.output(m21 , 0)
        GPIO.output(m22 , 0)
        return 'true'
@app.route('/down_side')
def down_side():
   data1="BACK"
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   return ('true')

@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 0)
   return  'true'
@app.route('/light_on')
def light_on () :
    data1="TURN ON"
    GPIO.output(light,1)
@app.route('/light_off')
def light_off () :
    data1="TURN OFF"
    GPIO.output(light,0)

if __name__ == "__main__":
  print "Start"
app.run(host='169.254.49.14',port=5010)

    


 



