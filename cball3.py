#cball.py
#Simulation of the flight of a cannonball
#This version is not modularized

from math import pi, sin, cos, radians

class Projectile:
    def __init__(self, angle, vel, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def getY(self):
        return self.ypos

    def getX(self:
        return self.xpos

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yevl = yvel1

def getInputs():
    angle = float(input)("Enter the launch angle (in degrees):"))
    vel = float(input)("Enter the initial velocity (in meters/sec): "))
    h0 = float(input)("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position and calculations: "))
    return angle, vel, h0, time





def main():
    #Initial step
    angle, vel, h0, time = getInputs()
    
    cball = Projectile(angle, vel, h0)


    while cball.getY() >= 0:
        cball.update(time)
    
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

main()
