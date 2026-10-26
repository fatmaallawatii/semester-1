# A bad class implementation

# What does the runtime error mean?
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
