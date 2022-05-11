# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

# Import the standard math module so that
# math.pi can be used in this program.
import math


def main():
    # Four parallel lists, one list for each attribute of the cans.
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
    can_radiuses = [
        6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
    ]
    can_heights = [
        10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    ]
    can_costs = [
        0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
    ]

    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1

    # For each can in the parallel lists, unpack the values
    # into the variables name, radius, height, and cost.
    for i in range(len(can_names)):
        name = can_names[i]
        radius = can_radiuses[i]
        height = can_heights[i]
        cost = can_costs[i]

        # Call the compute_storage_efficiency and
        # compute_cost_efficiency functions.
        store_eff = compute_storage_efficiency(radius, height)
        cost_eff  = compute_cost_efficiency(radius, height, cost)

        # Print the can size name, storage
        # efficiency, and cost efficiency.
        print(f"{name} {store_eff:.2f} {cost_eff:.0f}")

        # If the storage efficiency of the current can size is
        # greater than the maximum storage efficiency, save then
        # the current can size name and its storage efficiency.
        if store_eff > max_store_eff:
            best_store = name
            max_store_eff = store_eff

        # If the cost efficiency of the current can size is
        # greater than the maximum cost efficiency, then save
        # the current can size name and its cost efficiency.
        if cost_eff > max_cost_eff:
            best_cost = name
            max_cost_eff = cost_eff

    # Print the best storage and cost efficiencies.
    print()
    print("Best can size in storage efficiency:", best_store)
    print("Best can size in cost efficiency:", best_cost)


"""Here is another solution. This solution organizes the data about
the cans in a compound list. A compound list is a list that contains
lists. CSE 111 students study lists and compound lists in lesson 7.

def main():
    # A compound list (a list that contains lists).
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]

    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1

    # For each can in the can_sizes list, unpack the values
    # into the variables name, radius, height, and cost.
    for name, radius, height, cost in can_sizes:
        .
        .
        .
"""


def compute_storage_efficiency(radius, height):
    """Compute and return the storage efficiency of a steel can size.
    The storage efficiency is the volume of the can divided by its
    surface area.

    Parameters
        radius: the radius of the steel can
        height: the height of the steel can
    Return: the storage efficiency of the steel can
    """
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    efficiency = volume / surf_area
    return efficiency


def compute_cost_efficiency(radius, height, cost):
    """Compute and return the cost efficiency of a steel can size.
    The cost efficiency is the volume of the can divided by its cost.

    Parameters
        radius: the radius of the steel can
        height: the height of the steel can
        cost: the cost of the steel can
    Return: the cost efficiency of the steel can
    """
    volume = compute_volume(radius, height)
    efficiency = volume / cost
    return efficiency


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
