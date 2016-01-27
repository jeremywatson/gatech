import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def error(line, data):
	''' compute error bt line model and data

	line: tuple list or array (C0, C1) where C0 is slope and C1 is y-intercept
	data: 2d array where each row is a point (x,y)

	returns error as a single real value
	'''

	err = np.sum((data[:,1] - (line[0] * data[:,0] + line[1])) ** 2)
	return err

def fit_line(data, error):
	# gen initial guess
	l = np.float32([0, np.mean(data[:,1])])

	xEnds = np.float32([-5, 5])
	plt.plot(xEnds, l[0] * xEnds + l[1], 'm--', linewidth=2.0, label="Initial guess")

	result = spo.minimize(error, l, args=(data,), method='SLSQP', options={'disp': True})
	return result.x

def main():
	# define a line
	lOrig = np.float32([4,2])
	print "Original line: C0 = {}, C1 = {}".format(lOrig[0], lOrig[1])
	xOrig = np.linspace(0,10,21)
	yOrig = lOrig[0] * xOrig + lOrig[1]
	plt.plot(xOrig, yOrig, 'b ', linewidth=2.0, label="Original line")

	# add some noise for fun
	NOISE_SIGMA = 3.0
	noise = np.random.normal(0, NOISE_SIGMA, yOrig.shape)
	data = np.asarray([xOrig, yOrig + noise]).T
	plt.plot(data[:,0], data[:,1], 'go', label="Data points")

	# fit a line to our noisy data
	lFit = fit_line(data, error)
	print "Fitted line: C0 = {}, C1 = {}".format(lFit[0], lFit[1])
	plt.plot(data[:,0], lFit[0] * data[:,0] + lFit[1], 'r--', linewidth=2.0, label="Fitted line")

	plt.show()

if __name__ == '__main__':
	main()