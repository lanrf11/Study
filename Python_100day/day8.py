# Object

# Task 1: a class that describes a digital clock.
import time
class Clock(object):

    def __init__(self, hour=0, minite=0, second=0):
        self._hour = hour
        self._minite = minite
        self._second = second
    
    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minite += 1
            if self._minite == 60:
                self._minite = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        print("{:0>2d}:{:0>2d}:{:0>2d}".format(self._hour, self._minite, self._second))     # {:0>2d}: 1->01, 11->11

# if __name__ == "__main__":
#     clock = Clock(23, 58, 1)
#     while True:
#         clock.show()
#         clock.run()
#         time.sleep(1)


# Task 2: a class that describes points on a plane, moves points, and calculates the distance to another point.
class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def show(self):
        print("x: {}, y: {}".format(self._x, self._y))

    def move(self, moveX, moveY):
        self._x += moveX
        self._y += moveY

    def distanceTo(self, secondX, secondY):
        dist = ((self._x - secondX)**2 + (self._y - secondY)**2)**0.5
        return dist

if __name__ == "__main__":
    point = Point(1, 5)
    point.show()
    point.move(5, 3)
    point.show()
    distanceTo = point.distanceTo(0, 0)
    print(distanceTo)