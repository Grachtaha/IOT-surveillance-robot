project video : https://www.youtube.com/watch?v=izTjZLzoPM0
# IOT-surveillance-robot
This project is a raspberry pi based web controlled surveillance robot .
Installing and Configuring ‘Mjpeg stremer’ for getting Video :https://github.com/jacksonliam/mjpg-streamer 
Flask Setup in Raspberry Pi for Controlling Robot through Webpage:
   Install a flask support package into the Raspberry Pi by using given command:        
    $ pip install Flask
HTML code for webpage:
   User needs to copy-paste the above given HTML code in some text editor (notepad) and save the file with .HTML extension (robot.html).    Then put this HTML file in the /templates folder with respect to your python script location. Means you need to create a folder named   templates, where you have put your Python Code file for this Raspberry Surveillance Robot, then put robot.html file in this templates   folder. This step is important, otherwise our project won’t work. You can directly open the robot.html file by double clicking on it to see how your control links will look. Further check the whole process in Demonstration Video at the end. After we have done with the programming and all, we can just run the Python code in Raspberry Pi and open the IP_address_of_your_Pi:5010 in web Browser (like http://192.168.49.14:5010)

code :
  Complete Python code is given below, where we have written various functions to control the Robot on clicking the links on the webpage. You can understand them easily or if you are a beginner then check our previous Raspberry Pi Tutorials. Also visits our Robotics Section for more interesting and easy to build Robots.
