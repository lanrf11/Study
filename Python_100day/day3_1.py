# Unit conversion: inches and centimeters
# 1 inche = 2.54 cm

value = float(input("Please input the value:"))
unit = input("Please input the unit(inche/cm):")

if unit == "inche":
    print(str(value) + "inche = " + str(value / 2.54) + "cm.")
elif unit == "cm":
    print(str(value) + "cm = " + str(value * 2.54) + "inche.")
else:
    print("The unit is wrong!")
