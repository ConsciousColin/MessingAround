
def FibonacciSequencer (iter=10):
	seq = [0,1]
	first = 0 
	second = 1
	while i <= 100:
		n = first + second
		seq.append(n)
		first += 1 
		second += 1

	print seq 

FibonacciSequencer()