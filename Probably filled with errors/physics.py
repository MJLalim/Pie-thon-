"""
Description: This program is meant to calculate physics work
Programmer: Michael John A. Lalim
Date Started: 2023-04-27
Date Ended: 
"""
import math as m
import random as r
class Kinematics:
    def __init__ (self,vInital,vFinal,timeInterval,displacement,acceleration,velocity,horionztalVelocity):
        self.vInitial=vInital
        self.vFinal=vFinal
        self.timeInterval=timeInterval
        self.displacement=displacement
        self.acceleration=acceleration
        self.velocity = velocity
        self.horizontalVelocity = horionztalVelocity
    #---------------------------------------------------------------------------------
    """
    These equations are "normal" equations, meaning none of them are rearranged... yet
    """
    #---------------------------------------------------------------------------------
    #Three variable equations
    #---------------------------------------------------------------------------------
    def timeInt(self):
        answer = self.displacement/self.horizontalVelocity
        return answer
    def averageVelocity(self):
        answer = self.displacement/self.timeInterval
        return answer
    def displacement1(self):
        answer = self.velocity * self.timeInterval
        return answer
    #---------------------------------------------------------------------------------
    #Equations for displacement
    #---------------------------------------------------------------------------------
    #Equation 1
    def displacement2(self):
        answer = (self.vFinal + self.vInitial/2) * self.timeInterval
        return answer
    #Equation 3
    def displacement3(self):
        answer = (self.vInitial * self.timeInterval) + 1/2 * (self.acceleration * (self.timeInterval ** 2))
        return answer
    #Equation 5
    def displacement4(self):
        answer = (self.vFinal * self.timeInterval) - 1/2 * (self.acceleration * (self.timeInterval ** 2))
        return answer
    #---------------------------------------------------------------------------------
    #Equations for final velocity
    #---------------------------------------------------------------------------------
    #Equation 2
    def finalVelocity1(self):
        answer = self.vInitial + (self.acceleration * self.timeInterval)
        return answer
    #Equation 4
    def finalVelocity2(self):
        answer = m.sqrt((self.vInitial ** 2) + 2 *(self.acceleration * self.displacement))
        return answer
    #---------------------------------------------------------------------------------
    """
    These equations are rearranged in order to answer the question...
    """
    #---------------------------------------------------------------------------------
    #Equation for displacement
    #---------------------------------------------------------------------------------
    #
    # Equation 4
    #
    #Finds the displacement when time is not given
    def displacementRearrangedEquation4(self):
        answer = (((self.vFinal**2)-(self.vInitial**2)/ 2) * (self.acceleration))
        return answer
    #---------------------------------------------------------------------------------
    #Finds the initial velocity when time is not given
    def vInitialRearrangedEquation4(self):
        answer = m.sqrt((self.vFinal ** 2) - 2 * (self.acceleration * self.displacement))
        return answer
print("Enter 'x' if the value is not given");print("Enter 'find' for the value you need to find\n")
vInitial = input("Enter value for the initial velocity: ")
vFinal = input("Enter value for the final velocity: ")
timeInterval = input("Enter value for the time interval: ")
displacement = input("Enter value for the displacement: ")
acceleration = input("Enter value for the acceleration: ")
horizontalVelocity = input("Enter value for the horizontal velocity: ")
velocity = None
if vInitial == "find":
    if timeInterval == "x":
        vInitial = float(0);timeInterval = float(0)
        vFinal = float(vFinal);displacement = float(displacement);acceleration = float(acceleration)

#THIS PROJECT IS NOT FINISHED YET.... OMG....
