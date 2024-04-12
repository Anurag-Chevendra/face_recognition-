
# About
This is a simple home security project that was created as a part of the IEEE internship under Dr. Rohin Daruwala during my sophomore year. It basically involves Facial Recognition which then leads to a "buzzer" trigger or automatic door bypass based on the results of the model along with entire event logging available on a simple php website with firebase DB. I personally implemented this for my own room until my mom threw it out. All of this is deployed on a Rasberry pi 4. 

## Going Forward
in your vscode terminal:
pip install opencv-contrib-python


other than this you also have to create 2 other files: 

1)dataSet
2)trainer 


it should look something like this:


![](images/c1.PNG)


NOTE: try and keep the Raspberrypi's temperature below 47C, works the best.

NOTE2: you also have to have a composer, php v 7(NOT version 8), and firebase admin sdk 4x (NOT 5x)
