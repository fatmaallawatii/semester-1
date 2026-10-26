# Week 1.5, Session 1: Task 4

from geometry import Point, Circle
# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
centre = Point(2, 3)
#  - Creates a Circle object, using the Point object and a value for radius
circle = Circle(centre, 4)
#  - Displays the area of the circle
print("Area of circle:", circle.area())
#  - Displays the perimeter of the circle
print("Perimeter of circle:", circle.parimeter())
