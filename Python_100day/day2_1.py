# Convert Fahrenheit temperature to Celsius temperature
# F = 1.8C + 32

ft = float(input("Please input the Fahrenheit temperature:"))
ct = (ft - 32) / 1.8
print("The corresponding Celsius temperature is "+ str(ct))