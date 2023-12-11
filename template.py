"""
File: assignment1_signals.py
Authors: Janan Jahed (S5107318) and Andrei Medesan (S5130727) 
Description: The following functions are implemetations of signal
problems converted into code. There are 7 functions that implements
the sevem tasks described in the assignment.
"""

import math
# library used for type hints specifically lists
from typing import List

# function for reading the two different inputs
def get_input_data(message: str, number_inputs: int):
    if number_inputs == 2:
        input_1, input_2 = map(float, input(message).split())
        return input_1, input_2
    else:
        input_1, input_2, input_3 = map(int, input(message).split())
        return input_1, input_2, input_3
    
# function to read the input as a list 
def get_input_list() -> List[int]:
    lst = []
    while True:
        number = int(input())
        if number == 0:
            break
        lst.append(number)
    return lst

# function to print the result with two decimals
def print_output_data(output_data):
    print("{:.2f}".format(output_data))
    pass

# function to print the results in the form of a list
def print_output_list(output_list):
    for output_data in output_list:
        print(output_data)
    pass

def cartesian_to_polar(x: float, y: float) -> float:
    """
    Problem 1: convert the cartesian coordinates into polar
    coordinates using some specific formulas

    param: input as a list
    return: a tuple with two float values
    """
    rsquared = (x**2 + y**2)
    r = float(math.sqrt(rsquared))
    thet = float(math.atan2(y, x))
    # Round the calculated values to two decimal places
    r_result = round(r, 2)
    thet_result = round(thet, 2)
    return r_result, thet_result

def polar_to_cartesian(r: float, thet: float) -> float:
    """
    Problem 2: convert the polar coordinates into cartesian
    coordinates using some specific formulas

    param: input as a list
    return: a tuple with two float values
    """
    # calculate x and y
    x = (r*math.cos(thet))
    y = (r*math.sin(thet))
    # round the values to two decimals
    x_result = round(x , 2)
    y_result = round(y, 2)
    return x_result, y_result

def phasor_addition(f: int, n: int) -> str:
    """
    Problem 3: Calculates the sum of sinusoids

    param: f representing the frequency (int)
    param: n representing the number of sinusoids (int)
    return: a string representing the equation
    """
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

def aliasing(f0: int, fs: int) -> int: 
    """
    Problem 4: Identifying the frequency of a signal after sampling
  
    param: signal frequency 
    param: sampling frequency
    return: an integer representing the reconstructed sinusoid
    """
    f_reconstructed = abs(f0 - (round(f0 / fs) * fs))
    return f_reconstructed

def products_of_sinusoids(frequencies: List[int]) -> List[int]:
    """
    Problem 5: Frequency spectrum of a product of sinusoids

    param: list of frequencies
    return: an ordered list with the positive frequencies of
            the spectrum
    """
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

    print_output_list(sorted(list(spectrum)))

def nyquist_frequency(frequencies: List[int]) -> int:
    """
    Problem 6: Nyquist frequency evaluation

    param: list of frequencies
    return: an integer representing the nyquist value
    """
    nyquist = 0
    for i in range(len(frequencies)):
        nyquist += 2 * frequencies[i]

    return nyquist

def multipath_fading(dr: int, dt: int, x: int) -> float:
    """
    Problem 7: Calculate the amplitude of a signal that
    travels from a transmitter to a receiver and is reflected
    at a specific position

    param: an integer representing the first coordinate of the reflector
    param: an integer representing the second coordinate of the reflector
    param: an integer representing the x coordinate of the receiver
    return: a float value representing the resulting amplitude
    """
    # constants describing the signal transmitted
    frequency = 150e6
    velocity = 3e8
    # calculate the direct and reflected times
    t1 = x / velocity
    t2 = (math.sqrt(dr**2 + dt**2) + math.sqrt((dr - x)**2 + dt**2)) / velocity
    # calculate the phases since there is a shift
    phase_direct = 2 * math.pi * frequency * t1
    phase_reflected = 2 * math.pi * frequency * t2

    amplitude = abs(2 * math.cos((phase_direct + phase_reflected) / 2))

    print_output_data(amplitude)

def main(): 
    """
    Main function where the user gets ask about the problems and the code
    calls the respective functions that the user chose to determine.
    """
    while True:
        print("Choose a problem to evaluate:")

        choice = input("Enter the number of the problem (1-7): ")

        if choice == '1':
            input_1, input_2 = get_input_data("Enter two values: ", 2)
            print(f"The polar coordinates are: {cartesian_to_polar(input_1, input_2)}")

        elif choice == '2':
            input_1, input_2 = get_input_data("Enter two values: ", 2)
            print(f"The cartesian coordinates are: {polar_to_cartesian(input_1, input_2)}")

        elif choice == '3':
            f, n = get_input_data("Enter two values for f and n: ", 2)
            print(f"The resulting sinusoid is: {phasor_addition(f, n)}")

        elif choice == '4':
            f0, fs = get_input_data("Enter two values: ", 2)
            print(f"The frequency of the reconstructed sinusoid is: {aliasing(f0, fs)}")

        elif choice == '5':
            print("Enter frequencies (press 0 when to stop): ")
            input_values = get_input_list()
            print("The frequencies in the spectrum are: ")
            products_of_sinusoids(input_values)

        elif choice == '6':
            print("Enter frequencies (press 0 when to stop): ")
            input_values = get_input_list()
            print(f"The Nyquist frequency is: {nyquist_frequency(input_values)}")

        elif choice == '7':
            dr, dt, x = get_input_data("Enter three values for the coordinates: ", 3)
            print("The amplitude is: ")
            multipath_fading(dr, dt, x)

        elif choice == '-1':
            print("Bye :)")
            exit()

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

