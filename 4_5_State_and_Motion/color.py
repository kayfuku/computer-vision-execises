import matplotlib.pyplot as plt
'''
The color class creates a color from 3 values, r, g, and b (red, green, and blue).

attributes:
    r - a value between 0-255 for red
    g - a value between 0-255 for green
    b - a value between 0-255 for blue
'''


class Color(object):

    # __init__ is called when a color is constructed using color.Color(_, _, _)
    def __init__(self, r, g, b):
        # Setting the r value
        self.r = r

        # Set the other two color variables g and b
        self.g = g
        self.b = b

    # __repr__ is called when a color is printed using print(some_color)
    # It must return a string
    def __repr__(self):
        '''Display a color swatch and then return a text description of r,g,b values.'''

        plt.imshow([[(self.r/255, self.g/255, self.b/255)]])

        # Write a string representation for the color
        # ex. "rgb = [self.r, self.g, self.b]"
        # Right now this returns an empty string
        string = f"rgb = [{self.r}, {self.g}, {self.b}]"

        return string

    # __add__ is called when two colors are added together using color1 + color2
    # It must return a color
    def __add__(self, other):
        '''Add two colors together and return a new color.'''

        # Create a new color with the sum of the r values, g values, and b values
        # Make sure to cap the values at 255
        new_color = Color(min(self.r + other.r, 255), min(self.g + other.g, 255), min(self.b + other.b, 255))

        return new_color
