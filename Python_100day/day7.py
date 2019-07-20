# Task1: Display marquee text on the screen.
import os
import time
def displayTxet(str_show):
    txt = str_show
    while True:
        os.system('clear')  # ubuntu system
        print(txt)
        time.sleep(0.5)
        txt = txt[1:] + txt[0]


# Task2: Generate a verification code of the specified length, 
# which consists of uppercase and lowercase letters and numbers.
import random
def getVerificationCode(code_len):
    str_choice = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    str_code = ""
    for i in range(code_len):
        str_code += random.choice(str_choice)
    return str_code 

# Task3: Returns the suffix name of the given file name.
import os
def getSuffixName(str_filename):
    return os.path.splitext(str_filename)[-1]

def getSuffixName2(str_filename):
    position = str_filename.rfind(".")      # string.index() / string.find(): index from the start
    if 0 <= position < len(str_filename) - 1:   # string.rindex() / string.rfind(): index from the end
        return str_filename[position:]      # index / rindex: Erro if no found    
    else:                                   # find / rfind: return -1 if no found.
        return None


# Task4: Returns the largest value and second largest element in the a list.
def getLargestAndSecond(given_list):
    list_sort = sorted(given_list)
    return list_sort[-1], list_sort[-2]

# Task5: Calculate the number of sequences for that day in that given date.
def isLeapYear(year_number):
    if year_number % 4 != 0 or ( year_number % 400 != 0 and year_number % 100 == 0):
        return False
    else:
        return True

def getDateNumber(year_number, month_number, day_number):
    leap_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    notleap_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    daynum = 0
    if isLeapYear(year_number) :
        for i in range(month_number - 1):
            daynum += leap_month[i] 
        daynum += day_number
    else:
        for i in range(month_number - 1):
            daynum += notleap_month[i] 
        daynum += day_number
    return daynum


# Task6: Print Pascal's Triangle.
def printTriangle(row_triangle):
    num_list = [[]]*row_triangle
    for row in range(row_triangle):
        num_list[row] = [None] * (row + 1)
        for column in range(row+1):
            if column == 0 or column == row:
                num_list[row][column] = 1
            else:
                num_list[row][column] = num_list[row-1][column-1] + num_list[row-1][column]
        print(num_list[row])


# Task7: Two-color ball
import random
def selectBall(num_select):
    redball = 33
    blueball = 16
    list_num =([ x for x in range(1, redball+1)],[ x for x in range(1, blueball+1)]) 
    for i in range(num_select):
        list_select = [[random.sample(list_num[0], 6)], [random.sample(list_num[1], 1)]]
        print("{} -- Red: {}, Bule: {}".format(i+1, 
        ''.join(str(i) for i in list_select[0]), ''.join(str(i) for i in list_select[1])))

def selectBall2(num_select):
    redball = 33
    blueball = 16
    list_num =([ x for x in range(1, redball+1)],[ x for x in range(1, blueball+1)]) 
    for i in range(num_select):
        redlist_select = random.sample(list_num[0], 6)
        bluelist_select = random.sample(list_num[1], 1)
        print("{} -- Red: {}, Bule: {}".format(i+1, 
        ' '.join(str(i) for i in redlist_select), ' '.join(str(i) for i in bluelist_select)))


# Task8: Josephus problem 
def Josephus(num_people, num_start, num_out):
    list_people = [x for x in range(1, num_people+1)]
    list_out = []
    list_update = list_people[num_start:] + list_people[: num_start]
    while len(list_update) > 0 :
        num_list_out = num_out % len(list_update)
        list_out.append(list_update[num_list_out-1])
        if num_list_out == 0:
            list_update = list_update[:num_list_out-1]
        else:
            list_update = list_update[num_list_out:] + list_update[:num_list_out-1]
    return list_out

# Task9: Lucky christian.
def getChristianPosition(num_people, num_start, num_out, num_left):
    list_people = [x for x in range(1, num_people+1)]
    list_out = []
    list_left = []
    list_update = list_people[num_start:] + list_people[: num_start]
    while len(list_update) > num_left :
        num_list_out = num_out % len(list_update)
        list_out.append(list_update[num_list_out-1])
        if num_list_out == 0:
            list_update = list_update[:num_list_out-1]
        else:
            list_update = list_update[num_list_out:] + list_update[:num_list_out-1]
    list_left = [i for i in list_people if i not in list_out]
    return list_left



if __name__ == "__main__":

    # x1 = "PYTHON IS GREAT!"
    # displayTxet(x1)

    # x2 = 6
    # print(getVerificationCode(x2))

    # x3 = "q123.py"
    # y3 = "huijio"
    # print(getSuffixName(x3))
    # print(getSuffixName2(x3))
    # print(getSuffixName(y3))
    # print(getSuffixName2(y3))

    # x4 = [1, 2, 5, 87, 34, 234]
    # y4 = ['a', 'c', 'f', 'l', 'z', 'w']
    # print(getLargestAndSecond(x4))
    # print(getLargestAndSecond(y4))

    # x5 = [2000, 3, 1]
    # y5 = [2100, 3, 1]
    # print(getDateNumber(x5[0], x5[1], x5[2]))
    # print(getDateNumber(y5[0], y5[1], y5[2]))

    # printTriangle(10)

    # selectBall()
    # selectBall(4)
    # selectBall2(4)

    x8 = 30
    y8 = 5
    z8 = 9
    a8 = 15
    b8 = Josephus(x8, y8, z8)
    c8 = getChristianPosition(x8, y8, z8, a8)
    print(b8)
    print(c8)