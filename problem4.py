"""
Authors: Janan Jahed (s5107318) & Andrei Medesan (S5130727)
Emails: j.jahed@student.rug.nl & a.medesan@student.rug.nl
Description: Problem 4 - Identifying the frequency of a signal after sampling
param: signal frequency 
param: sampling frequency
return: an integer representing the reconstructed sinusoid

"""

def aliasing(f0: int, fs: int) -> int: 
    f_reconstructed = abs(f0 - (round(f0 / fs) * fs))
    return f_reconstructed


f0_input, fs_input =  map(int, input().split())
result = aliasing(f0_input, fs_input)
print(result)

