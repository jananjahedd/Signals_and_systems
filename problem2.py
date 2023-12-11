"""
Authors: Janan Jahed (s5107318) & Andrei Medesan (S5130727)
Emails: j.jahed@student.rug.nl & a.medesan@student.rug.nl
Description: Problem 2 - convert the polar coordinates into cartesian
coordinates using some specific formulas
param: input as a list
return: a tuple with two float values
"""
import math
user_input = input().split()

r = float(user_input[0])
thet = float(user_input[1])

x = (r*math.cos(thet))
y = (r*math.sin(thet))

x_result = round(x , 2)
y_result = round(y, 2)

print(x_result, y_result)
