#http://radiusofcircle.blogspot.com

#time module
import time

#time at the start of execution
start_time = time.time()

#function which will generate
#the result and return the 
#result once it had found
def pythagorean_triplet_m_n():
	#for loop to generate m,n
	for n in range(1,32):
		for m in range(1,n):
			a = n**2 - m**2
			b = 2*n*m
			c = n**2 + m**2
			if a+b+c == 1000:
				return a*b*c

#printing the result
print (pythagorean_triplet_m_n())

#Time at the end of execution
end_time = time.time()

#total Time taken
print (end_time - start_time)