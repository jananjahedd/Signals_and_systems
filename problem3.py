"""
Authors: Janan Jahed (s5107318) & Andrei Medesan (S5130727)
Emails: j.jahed@student.rug.nl & a.medesan@student.rug.nl
Description: Problem 3 - Calculates the sum of sinusoids
param: f representing the frequency (int)
param: n representing the number of sinusoids (int)
return: a string representing the equation
"""

import math

def phasor_addition(f,n):
    real_part = 0
    imaginary_part = 0

    counter = 0
    while counter < n:
        amplitude,phase = map(float,input().split())  
        counter+=1
        real_part += amplitude * math.cos(2 * math.pi * f + phase)
        imaginary_part += amplitude * math.sin(2 * math.pi * f + phase)

    amplitude_result = round(math.sqrt(real_part**2 + imaginary_part**2), 2)
    phase_result = round(math.atan2(imaginary_part, real_part), 2)

    if amplitude_result == 0:
        result = "x(t) = 0.00"
    else:
        result = f"x(t) = {amplitude_result}cos(2*pi*{f}*t+{phase_result})"

    return result

f, n = map(int, input().split())
result = phasor_addition(f,n)
print(result)
