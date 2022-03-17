"""
This one honestly took me about a minute to write, and it finishes in less than a second. Not sure how you could possibly make this better/faster since it was so fast.

Correction - Daniel actually improved this, by pointing the obvious fact that I don't need two for loops, because you can work on both halves of the problem at the same time since we're not mutating x at all in the loop. The new version is about twice as fast.

"""

from time import perf_counter 

# TIME CODE STARTS

start = perf_counter()

##########################################################################

temp = 0
temp2 = 0

for x in range(1, 101):
    temp += x
    temp2 = temp2 + x * x

temp = temp * temp

print(temp - temp2)

##########################################################################


# TIME CODE ENDS

end = perf_counter()

print(f"Finished in {end - start:0.7f} seconds")

