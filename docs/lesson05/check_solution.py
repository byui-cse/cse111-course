# 1. The sqrt() function is in the math module,
# so import that first.
import math


# 2. Define the calculate_euclidean function here. It will  
# need parameters for each of the coordinates (4 in total),
#  and should return the Euclidean distance.
def calculate_euclidean(ax, ay, bx, by):
	x_component = (ax - bx) ** 2
	y_component = (ay - by) ** 2
	
	distance = math.sqrt(x_component + y_component)
	return distance


# 3. Define the calculate_manhattan function here. It will
# also need four parameters and should return the Manhattan 
# distance.
def calculate_manhattan(ax, ay, bx, by):
	x_component = abs(ax - bx)
	y_component = abs(ay - by)
	
	distance = x_component + y_component
	return distance


# 4. Define your display_results function here. It will need
# two parameters, one for each distance you wish to display.
# It does not need to return anything.
def display_results(euclidean, manhattan):
	print()
	print(f"The Euclidean Distance between A and B is: {euclidean:.2f}")
	print(f"The Manhattan Distance between A and B is: {manhattan:.2f}")


# 5. Now that your functions are defined, get the input 
# values from the user, making sure to convert them to floats.
ax = float( input("Enter A's x coordinate: ") )
ay = float( input("Enter A's y coordinate: ") )

bx = float( input("Enter B's x coordinate: ") )
by = float( input("Enter B's y coordinate: ") )


# 6. Call each of your distance functions, passing the input 
# values as arguments. Make sure to store the results of each 
# function in variables.
euclidean_distance = calculate_euclidean(ax, ay, bx, by)
manhattan_distance = calculate_manhattan(ax, ay, bx, by)


# 7. Call the display_results function, passing as arguments  
# the two variables you're using to store your distances.
display_results(euclidean_distance, manhattan_distance)