# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        """initialise a point with x and y coordinates."""
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        """calculate yej distance from the origin (0, 0)."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # Add distance_to() method here
    def distance_to(self, other):
        """calclate the distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point

point1 = Point(3, 4)
point2 = Point(6, 8)



# Add a definition for a Circle class here, giving it
class Circle:
    """a circle with radius and centre coordinates"""


#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
    def __init__(self, centre, radius):
        """initialise a circle with a radius and a centre"""
        self.centre = centre
        self.radius = radius

#  - A method area(), returning the area of the circle
    def area(self):
        """calculate the area of the circle"""
        return 3.14159 * self.radius ** 2


#  - A method perimeter(), returning the perimeter of the circle
    def parimeter(self):
        """calculate the parimeter of the circle."""
        return 2 * 3.14159 * self.radius

# Don't add any testing code to this file!
