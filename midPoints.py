# to display what is being calculated
import matplotlib.pyplot as plt
import math

def calcMids(cones, carPos):
	# setup a list to store the midpoints
	midPoints = []
	# split the cones up into red and blue
	redCones, blueCones = coneSetup(cones, carPos)
	# go through all the red cones
	for rCone in redCones:
		for bCone in blueCones:
			# find the distance between the two cones (cone distance)
			cd = findDisPoints(rCone, bCone)
			# check if they are in the suitable range
			if cd < 5:
				midPoint = findMidPoint(rCone, bCone)
				midPoints.append(midPoint)
	
	# return the midpoints calculated
	return midPoints

def coneSetup(cones, carPos):
	# setup lists of red and blue cones to fill up
	redCones = []
	blueCones = []
	for cone in cones:
		# find the distance between the car and cone
		distance = findDisPoints(cone, carPos)

		# if cones is red and in range
		if cone[2] == 'r' and distance < 15:
			# add distnace to the cone data
			cone.append(distance)
			# add cone to the red list
			redCones.append(cone)
		# if coen is blue and in range
		elif cone[2] == 'b' and distance < 15:
			# add distance to the cone data
			cone.append(distance)
			# add cone to the blue list
			blueCones.append(cone)

	# return the lists of red and blue cones
	return redCones, blueCones

def findDisPoints(point1, point2):
	# work out the distance between two points using the maths library
	distance = math.hypot(point2[0] - point1[0], point2[1] - point1[1])
	return distance

def findMidPoint(point1, point2):
	midPoint = []
	midPoint.append((point1[0]+point2[0])/2) # x coordinate
	midPoint.append((point1[1]+point2[1])/2) # y coordinate
	return midPoint + ['m']

def displayMap(pointMap):
	# add a grid
	plt.grid(visible = True, which = 'major', axis = 'both', alpha = 0.2)
	for point in pointMap:
		# get parameters from point
		x = float(point[0])
		y = float(point[1])
		if point[2] == "r":
			colour = "red"
			mark = 'o'
		elif point[2] == "b":
			colour = "blue"
			mark = 'o'
		elif point[2] == "c":
			colour = "green"
			mark = 'x'
		else:
			colour = "orange"
			mark = 'x'
		# plot the point into the map
		plt.scatter(x, y, marker=mark, color=colour)
	# display the map generated
	plt.show()

def startup():
	# Clear the top of the terminal for easier error spotting
	for i in range(10):
		print("\n")
	print("This code calculates the mid points using carteias coordinates")

	# there are two possible configurations that we will be given
	# [x, y] in list (BASED ON THIS FOR NOW)
	# or list of [x] followed by [y]

	# using a file to generate the points
	txtMidPoints = open("midPoints.txt", "r")
	ls = txtMidPoints.readlines()

	print("\nThe contents of the midPoints.txt file:")
	print(ls)

	print("\neach line separate")
	cones = []
	for line in ls:
		xy = line.strip("\n")
		point = xy.split(",")
		cones.append([float(point[0]), float(point[1]), point[2]])

	print("THESE ARE THE CONES THAT WILL BE USED [x, y, colour]")
	print(cones)
	# close the file
	txtMidPoints.close()
	return cones

########### MAIN

# get the position of the cones from the text file
conesLs = startup()
carPos = [3, 0, 'c']

# calculate the midpoints from the cones and car position
midPoints = calcMids(conesLs, carPos)

# display all the midpoints
print('\nMidpoints')
print(midPoints)

allPoints = conesLs + midPoints + [carPos]
print("The length of the midpoints is as follows:", len(midPoints))

displayMap(allPoints)







# def choseCones(cones):
# 	# for each cone within the cone list, compare the distance between it and the others
# 	history = []
# 	midPoints = []
# 	for id1, cone1 in enumerate(cones):
# 		history.append([id1])
# 		for id2, cone2 in enumerate(cones):
# 			# find the distance between one cone and the others
# 			# if they are on the opposite side
# 			if (cone1[2] == "r" and cone2[2] == "b") or (cone1[2] == "b" and cone2[2] == "r"):
# 				distance = findDisPoints(cone1, cone2)
# 				if len(history[id1]) < 3:
# 					# add distance to the list
# 					history[id1].append(distance)
# 					findDisPoints(cone1, cone2)
# 				else:
# 					compareDis(history[id1], distance)

# 	print('\nDisplay the history')			
# 	for i in history:
# 		print(i)

# def compareDis(curCone, newDis):
# 	print(curCone)
# 	if (curCone[1] > curCone[2]) and (curCone[1] > newDis):
# 		print('true1')
# 		print(newDis)
# 	elif (curCone[1] < curCone[2]) and (curCone[2] > newDis):
# 		print('true2')
# 		print(newDis)
# 	else:
# 		print('false')






