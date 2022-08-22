# As a fan of geometry, I want to
# model a line based on a point
# consisting of (x, y) co-ordinates
# using the Cartesian system,
# So that I can calculate its
# length .
#
# - A Length as 2 Points (x1, y1) and (x2, y2)
# - Length of a Line = sqrt( (x2 - x1) ^ 2 + (y2 - y1) ^ 2)

# Math library from python
import math


# Function to calculate distance
def calculatedistancebetweentwopoints(x1, y1, x2, y2):
    # Calculating distance
    # - Length of a Line = sqrt( (x2 - x1) ^ 2 + (y2 - y1) ^ 2)
    return math.sqrt(math.pow(x2 - x1, 2) +
                     math.pow(y2 - y1, 2) * 1.0)


# Driving Code
print("%.6f" % calculatedistancebetweentwopoints(3, 4, 4, 3))