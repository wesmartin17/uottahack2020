import time
import board
import busio
import adafruit_adxl34x
import math


def mag(vector):
	return math.sqrt(vector[0]**2+vector[1]**2+vector[2]**2)


jerkMax = 3.6


class Jerk:
	i2c = busio.I2C(board.SCL, board.SDA)

	accelerometer = adafruit_adxl34x.ADXL345(i2c)
	prevAcceleration = accelerometer.acceleration

	def stepTaken(self, prevAcc, curAcc):
	    if(mag(curAcc)-mag(prevAcc) > jerkMax):
    		return True
	    if(mag(curAcc)-mag(prevAcc) < -jerkMax):
    		return True
	    else:
		return False

	timeInc = 0.06
	timeBet = 0.3
	stepNum = 0

	def __init__(self):  # Defines the initial object parameters
		print("initialized jerk")

	def stepCount(self):  # Returns the string for number of steps
		return str("You've taken %i steps" % self.stepNum)

	def stepCount(self):  # Returns the string for number of steps
		return str("You've taken %i steps" % self.stepNum

	def reset(self):  # Resets the number of steps taken
		self.stepNum=0


## Uncomment when testing step tester ##
	def getJerk(self):
		if(self.stepTaken(prevAcceleration, self.accelerometer.acceleration)):
			self.stepNum=self.stepNum + 1
			print("%f" % mag(accelerometer.acceleration))
			print("%f" % mag(prevAcceleration))
			print("you took step %i" % self.stepNum)
			time.sleep(timeBet)
		prevAcceleration=accelerometer.acceleration
		return self.stepNum
