import math

"""All shapes in this library are regular."""

def circle_circumference(radius):
    circum = 2 * math.pi * radius
    return circum

def circle_area(radius):
    area = math.pi * radius**2
    return area

def hemisphere_surface_area(radius):
    surf_area = 4 * math.pi * r**2
    return surf_area

def hemisphere_volume(radius):
    vol = 4 * math.pi * radius**3 / 3
    return vol

def sphere_surface_area(radius):
    surf_area = 4 * math.pi * radius**2
    return surf_area

def sphere_volume(radius):
    vol = 4 * math.pi * r**3 / 3
    return vol


def triangle_perimeter(a, b, c):
    perim = a + b + c
    return perim

def triangle_area(a, b, c):
    semi_perim = triangle_perimeter(a, b, c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def rectangle_perimeter(width, length):
    perim = 2 * (width + length)
    return perim

def rectangle_area(width, length):
    area = width * length
    return area


def hexagon_perimeter(side_len):
    perim = 6 * side_len
    return perim

def hexagon_area(side_len):
    area = 3 * math.sqrt(3) / 2 * side_len**2
    #area = 6 * triangle_area(side_len, side_len, side_len)
    return area

def hexagonal_prism_surface_area(side_len, height):
    surf_area = 2 * hexagon_area(side_len) \
            + 6 * rectangle_area(side_len, height)
    return surf_area

def hexagonal_prism_volume(side_len, height):
    vol = hexagon_area(side_len) * height
    return vol
