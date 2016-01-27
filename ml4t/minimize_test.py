import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):
	# given a scalar x, return some real value	
	Y = (X - 1.5)**2 + 0.5
	print "X = {}, Y = {}".format(X,Y)
	return Y

def main():
	xGuess = 2.0
	min_result = spo.minimize(f, xGuess, method='SLSQP', options={'disp': True})
	print 'minima found at:'
	print 'X={}, Y={}'.format(min_result.x, min_result.fun)

if __name__ == '__main__':
	main()	
