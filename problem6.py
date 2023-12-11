"""
Authors: Janan Jahed (s5107318) & Andrei Medesan (S5130727)
Emails: j.jahed@student.rug.nl & a.medesan@student.rug.nl
Description: Problem 6  - Nyquist frequency evaluation
param: list of frequencies
return: an integer representing the nyquist value
"""
from typing import List

def nyquist_frequency(frequencies: List[int]) -> int:
    nyquist = 0
    for i in range(len(frequencies)):
        nyquist += 2 * frequencies[i]

    return nyquist

frequency = []
while True:
    number = int(input())
    if number == 0:
        break
    frequency.append(number)

print(nyquist_frequency(frequency)) 
