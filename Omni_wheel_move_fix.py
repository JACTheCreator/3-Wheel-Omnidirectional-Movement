import math

x = 0
y = 255
R = 2
vel = 200

if x == 0 and y == 0:
	thetaA = thetaB = thetaC = 90
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

	FL =  (vel * math.cos(thetaA))+R
	FR = (-vel * math.cos(thetaB))+R
	BW = (-vel * math.cos(thetaC))+R

	print ("")
	print("thetaA: " + str(thetaA))
	print("thetaB: " + str(thetaB))
	print("thetaC: " + str(thetaC))

	print ("")

	print("FL: " + str(FL))
	print("FR: " + str(FR))
	print("BW: " + str(BW))

	print ("")