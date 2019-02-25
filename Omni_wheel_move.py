import math

def moveCartesian(x, y, vel = 100):
	print("Cartesian")
	if x == 0 and y == 0:
		return
	if x == 0 and y > 0:
		theta = 90
	if x == 0 and y < 0:
		theta = 270
	else:
		theta = math.degrees(math.atan2(y,x))

	print("theta: " + str(theta))
	thetaA = math.radians(60-theta)
	thetaB = math.radians(120-theta)
	thetaC = math.radians(0-theta)

	FL = vel * math.cos(thetaA)
	FR = vel * math.cos(thetaB)
	BW = vel * math.cos(thetaC)

	print("thetaA: " + str(thetaA))
	print("thetaB: " + str(thetaB))
	print("thetaC: " + str(thetaC))

	print ("")

	print("FL: " + str(FL))
	print("FR: " + str(FR))
	print("BW: " + str(BW))

	print ("")

def moveAngle(angle, vel = 100):
	x, y = convertPolarToCartesian(angle)
	print(x , y)

	# moveCartesian(x, y, vel)

def convertPolarToCartesian(angle, r = 1):
	angle = math.degrees(angle)
	return (r * math.cos(angle), r * math.sin(angle))

# x, y = 0, 1
# moveCartesian(x, y)

angle = 22.6
moveAngle(angle, 13)
