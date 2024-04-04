from math import pi, pow


# defining the function 
def calc_circle(diameter, multiplier=1):
    """
    
    Calculates the size of a circle.

    inputs:
    * diameter: diameter of the circle
    
    """
    radius = diameter / 2
    size = pow(radius, 2) * pi

    # multiply the size
    size_multiplied = size * multiplier

    return size_multiplied, radius


# using the function
circle_size, radius_size = calc_circle(20, 4)



pass

