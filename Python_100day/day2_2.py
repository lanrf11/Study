# Calculate the perimeter and area of a circle by entering the radius
# perimeter: C = 2 * pi * r
# area: S = pi * r ** 2

import math

r = float(input("Please input the radius:"))
c = 2 * math.pi * r
s = math.pi * r ** 2
print("The perimeter is "+ str(c) + ", and the area is " + str(s))