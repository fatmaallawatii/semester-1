# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

        if type(width) is not int:
            raise TypeError()

        if type(height) is not int:
            raise TypeError()

        if width <= 0:
            raise ValueError()

        if height <= 0:
            raise ValueError()

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)


    def is_square(self):
        """
        Returns True if the rectangle is a square
        """
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """
        Returns the area of the triangle
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        perimeter = 2*(self.width + self.height)
        return perimeter

