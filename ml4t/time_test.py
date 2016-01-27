import time

def main():
	t1 = time.time()
	print "Print statement"
	t2 = time.time()
	print "Time taken to print is ", t2-t1, " seconds"

if __name__ == '__main__':
	main()