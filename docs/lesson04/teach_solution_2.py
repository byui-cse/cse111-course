# Copyright 2026, Brigham Young University-Idaho. All rights reserved.

# Import the standard math module so that
# math.pi can be used in this program.
import math


def main():
    print(f"#1 Picnic   {compute_storage_efficiency(6.83, 10.16):.2f}")
    print(f"#1 Tall     {compute_storage_efficiency(7.78, 11.91):.2f}")
    print(f"#2          {compute_storage_efficiency(8.73, 11.59):.2f}")
    print(f"#2.5        {compute_storage_efficiency(10.32, 11.91):.2f}")
    print(f"#3 Cylinder {compute_storage_efficiency(10.79, 17.78):.2f}")
    print(f"#5          {compute_storage_efficiency(13.02, 14.29):.2f}")
    print(f"#6Z         {compute_storage_efficiency(5.4, 8.89):.2f}")
    print(f"#8Z short   {compute_storage_efficiency(6.83, 7.62):.2f}")
    print(f"#10         {compute_storage_efficiency(15.72, 17.78):.2f}")
    print(f"#211        {compute_storage_efficiency(6.83, 12.38):.2f}")
    print(f"#300        {compute_storage_efficiency(7.62, 11.27):.2f}")
    print(f"#303        {compute_storage_efficiency(8.1, 11.11):.2f}")


def compute_storage_efficiency(radius, height):
    """Compute and return the storage efficiency of a cylnder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the storage efficiency of the cylinder
    """
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    return storage_efficiency


def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area


# Start this program by
# calling the main function.
main()
