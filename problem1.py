"""
Authors: Janan Jahed (s5107318) & Andrei Medesan (S5130727)
Emails: j.jahed@student.rug.nl & a.medesan@student.rug.nl
Description: Problem 1 - convert the cartesian coordinates into polar
coordinates using some specific formulas
param: input as a list
return: a tuple with two float values
"""
import math

user_input = input().split()

x = float(user_input[0])
y = float(user_input[1])

rsquared = (x**2 + y**2)
r = float(math.sqrt(rsquared))
thet = float(math.atan2(y, x))
r_result = round(r,2)
thet_result = round(thet,2)
print (r_result, thet_result)





