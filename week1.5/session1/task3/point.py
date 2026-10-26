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

print("Point 1 x:", point1.x)
print("Point 1 y:", point1.y)
print("Distance from origin:", point1.distance())

print("Point 2 x:", point2.x)
print("Point 2 y:", point2.y)

print("Distance between points", point1.distance_to(point2))