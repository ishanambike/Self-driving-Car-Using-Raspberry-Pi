# Self-driving-Car-Using-Raspberry-Pi
This project develops a prototype of self driving car which basically demonstrates lane tracking, automated parking,obstacle detection and traffic lights detection.

The project aims to build a monocular vision using Raspberry Pi as a processing chip. A Pi camera along with an ultrasonic sensor is used to provide necessary data from the real world to the module. The proposed module helps the driver in reaching the given destination safely and intelligently thus avoiding the risk of human errors. Many existing algorithms like  Obstacle detection,Traffic signal detection ,Automatic parking  and Lane tracking are combined together to provide the necessary control to the car.Obstacle detection and Automatic parking  is carried out by Ultrasoic sensors . Lane Tracking and Traffic signal detection is done with help of PIcamera along with OpenCV. 

 A miniature car including above features will be developed which will show optimum performance in the simulated environment considering the fact that all assumptions and Dependencies are met.
 
 Hardware Requirements:
 1 x Raspberry Pi Model 3B 
 1 x Raspberry Pi 5v Camera 
 2 x HCSR04 Ultrasonic Sensor 
 1 x L293D Motor Driver 
 1 x Robot Chassis Cost 
 1 x Power Bank Cost 
 1 x 9v Battery Cost 
 1 x Set of Jumper wires 
 1 x 16 GB Micro SD Card 
 1 x  Bread Board Cost   
 
 
 Software Requirements:
 Raspian Os
 Xming Server
 PuTTY SSH Session
 Remote Desktop Connection
 Opencv 3.0
 Python 2.7
 
 Modules presented in this project:
 
 I] Obstacle Avoidance:
 Working Steps:
 1.Trig pin on ultrasonic sensor is made logic high using external trigger signal.
 2.A signal is sent from the transmitter module.
 3.The signals return back after hitting a surface and the receiver detects this signal.
 4.The Echo pin is high from the time of sending the signal and receiving it.
 5.This time can be converted to distance using appropriate calculations.The speed of sound is 340 m/s or 29 microseconds per centimeter
   Distance(cm) = (Time/29)/2
 6.This information is processed by the Pi. If the distance between the car and the obstacle is less than 30cm, the car stops.
 7.Wheels on the left move opposite to the wheels on the right. This helps the car to turn.
 
 
 
 
 II] Lane Tracking:
 Working Steps:
 1.Extract the color range for the road.
 2.Convert the image into grayscale image.
 3.Identify the lane in white/yellow color using Canny edge algorithm.
 4.Define the region of interest by using image mask.
 5.Transform the curved lines using Hough transform.
 6.Find the slope of lanes obtained from Hough transform.
 7.If (slope>= -80 and slope <= -30):
      r+=1 (increment right lane counter)
      l=0 (reset left lane counter)
   If(slope>= 30 and slope <= 80):
      l+=1 (increment left lane counter)
      r=0 (reset right lane counter)
8.If l > 10:
    Turn left
  elif r > 10:
    Turn right
  else:
    Move straight 
9.Repeat from step 1

III] Traffic light detection:
Working Steps:
1.Capture Frames from the pi camera.
2.Define the specific region in each frame which will be considered for computation.
3.In defined region using color & shape detection identify Red & Green traffic signal.
4.If Red signal detected stop the car.
5.If Green signal detected move the car.

IV] Automated Parking:
Working Steps:
1.Trig pin on ultrasonic sensor is made logic high using external trigger signal.
2.A signal is sent from the transmitter module.
3.The signals return back after hitting a surface and the receiver detects this signal.
4.Echo pin is high from the time of sending the signal and receiving it.
5.This time can be converted to distance using appropriate calculations.
      The speed of sound is 340 m/s or 29 microseconds per centimeter
      Distance(cm) = (Time/29)/2
6.The car will keep checking for empty slots by detecting empty spaces with distance>30 cm.
7.Once it detects free space it keeps checking whether distance in >30 cm for about 1 sec while moving forward.
8.If it gets distance >30cm for 1 sec then it has found space to park and car will stop.
9.Then it will park in that spot.



 
 
