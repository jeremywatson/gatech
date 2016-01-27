import numpy as np

def test_run():
	print "1D array:"
	print np.array([2,3,4])

	print "2D array:"
	print np.array([(1,2,3),(4,5,6)])

	# print "Creating an empty array by passing a tuple:"
	# print np.empty((4,5))

	print "Creating an array of all 1s:"
	print np.ones((3,3))

	print "Creating a random array:"
	print np.random.random((2,4))

	print "Random numbers:"
	print np.random.randint(10) # 0-10, 1 val
	print np.random.randint(0, 10) # 0-10 explicit
	print np.random.randint(0, 10, size=5), # 1D array, 5 vals
	print np.random.randint(0, 10, size=(2,3)) # 2D array

	a = np.ones((4,3))
	print a.shape # size of the 2d array
	print a.size # no of elements in the array
	print a.dtype # datatype in array

	print "Sum of each column:\n", a.sum(axis=0)
	print "Sum of each row:\n", a.sum(axis=1)
	print "Array mean: ", a.mean()

	a[0,:] = 1 # assigning an entire row
	a[:,2] = [0,1,2] # assigning multiple vals

	b = np.array([(20,4,5,6),(2,3,7,4)])
	mean = b.mean()

	# masking

	print b[b<mean]
	b[b<mean] = mean # all values less than mean get replaced by mean
	

if __name__ == '__main__':
	test_run()