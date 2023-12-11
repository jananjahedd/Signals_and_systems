""""
Authors: Janan Jahed (s5107318) & Andrei Medesan (S5130727)
Emails: j.jahed@student.rug.nl & a.medesan@student.rug.nl
Description: Problem 5 - Frequency spectrum of a product of sinusoids
param: list of frequencies
return: an ordered list with the positive frequencies of the spectrum
"""
from typing import List

def products_of_sinusoids(frequencies: List[int]) -> List[int]:
    spectrum = set()

    if len(frequencies) < 2:
        return spectrum

    difference = abs(frequencies[0] - frequencies[1])
    summation = frequencies[0] + frequencies[1]
    spectrum.add(difference)
    spectrum.add(summation)

    for i in range(2, len(frequencies)):
        new_spectrum = set()

        for spectre in spectrum:
            new_difference = abs(spectre - frequencies[i])
            new_summation = spectre + frequencies[i]
            new_spectrum.add(new_difference)
            new_spectrum.add(new_summation)
            
        spectrum = new_spectrum

    return sorted(list(spectrum))

frequency = []
while True:
    number = int(input())
    if number == 0:
        break
    frequency.append(number)

spectrum_output = products_of_sinusoids(frequency)
for value in spectrum_output:
    print(value)
