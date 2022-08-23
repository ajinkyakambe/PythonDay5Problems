# UC3 As a fan of geometry, I want to
# compare two lines based on
# the end points, So that I know
# one line is equal, greater or
# less than the other line.

import math


def check_equality_between_lines(x1, x2, x3, x4, y1, y2, y3, y4):

    length1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    length2 = math.sqrt(math.pow(x4 - x3, 2) + math.pow(y4 - y3, 2))

    print("The length of first line is: ")
    print(length1)
    print("The length of second line is: ")
    print(length2)

    if length1 > length2:
        print("Length of first line is greater than that of second line.")
    elif length1 < length2:
        print("Length of first line is lesser than that of second line.")
    else:
        print("Lengths of both the lines are equal.")


# Driving code
check_equality_between_lines(1, 1, 4, 4, 1, 8, 2, 4)