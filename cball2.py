#cball.py
#Simulation of the flight of a cannonball
#This version is not modularized

from math import pi, sin, cos, radians

def getInputs():
    angle = float(input)("Enter the launch angle (in degrees):"))
    vel = float(input)("Enter the initial velocity (in meters/sec): "))
    h0 = float(input)("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position and calculations: "))
    return angle, vel, h0, time

def getXYComponents(vel, angle):
    radians = (angle * pi)/180.0
    theta = radians
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

def updateCannonball(time, xpos, xvel, yvel):
    xpos = xpos + xvel * time
    yvel1 = yvel - time * 9.8
    ypos = ypos + time * (yvel + yvel1) / 2.0;
    yvel = yvel1

def main():
    #Initial step
    angle, vel, h0, time = getInputs()
    
    #calculate the initial position
    xpos = 0
    ypos = h0


    while ypos >= 0:
      xpos, ypos, yvel, = updateCannonBall(time, xpos, ypos, xvel, yvel)

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

main()
