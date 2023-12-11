"""
Authors: Janan Jahed (s5107318) & Andrei Medesan (S5130727)
Emails: j.jahed@student.rug.nl & a.medesan@student.rug.nl
Description:Problem 7 - Calculate the amplitude of a signal that
travels from a transmitter to a receiver and is reflected
at a specific position
param: an integer representing the first coordinate of the reflector
param: an integer representing the second coordinate of the reflector
param: an integer representing the x coordinate of the receiver
return: a float value representing the resulting amplitude
"""
import math

def multipath_finding(dr: int, dt: int, x: int) -> float:
    frequency = 150e6
    velocity = 3e8

    t1 = x / velocity
    t2 = (math.sqrt(dr**2 + dt**2) + math.sqrt((dr - x)**2 + dt**2)) / velocity

    phase_direct = 2 * math.pi * frequency * t1
    phase_reflected = 2 * math.pi * frequency * t2

    amplitude = abs(2 * math.cos((phase_direct + phase_reflected) / 2))

    return amplitude


dr, dt, x = map(int, input().split())
print("{:.2f}".format(multipath_finding(dr, dt, x)))



