# Enter a number to determine whether it is a leap year

year = int(input("Please input a year:"))
isleap = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0 )
leapyear = ["is not " ,"is "]
print("It "+ leapyear[isleap] +"a leap year!")
