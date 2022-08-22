# UC2: As a fan of geometry, I want to
# check equality of two lines
# based on the end points, So
# that I know when two lines are
# the equal. - Using Java equals method to check equality of 2 Lengths is
# preferable.


# sol: two given straight lines are identical then there co-efficients should be proportional
# a1/a2 = b1/b2 = c1/c2

def equality_of_two_lines(a1, b1, c1, a2, b2, c2):
    if ((a1 // a2 == b1 // b2) and
            (a1 // a2 == c1 // c2) and
            (b1 // b2 == c1 // c2)):
        print("The given straight lines",
              "are identical")
    else:
        print("The given straight lines",
              "are not identical")


# Driver Code for same lines
a1, b1 = -2, 4
c1, a2 = 3, -6
b2, c2 = 12, 9
equality_of_two_lines(a1, b1, c1, a2, b2, c2)

# Driver Code for different lines

d1, e1 = -3, 4
f1, d2 = 4, 6
e2, f2 = 13, 42

equality_of_two_lines(d1, e1, f1, d2, e2, f2)