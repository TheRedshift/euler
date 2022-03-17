"""
Going to add some code timing from this problem onwards, just for fun.

"""
from time import perf_counter 

# TIME CODE STARTS

start = perf_counter()

temp = 0
temp2 = 0

for x in range(1, 101):
    temp += x

temp = temp * temp

for x in range(1, 101):
    temp2 = temp2 + x * x

print(temp - temp2)



# TIME CODE ENDS

end = perf_counter()

print(f"Finished in {end - start:0.7f} seconds")