"""
Going to add some code timing from this problem onwards, just for fun.

So for this problem, straight away I'm thinking that long number needs to be in some kind of collection, but I'm really not sure what kind. It definitely needs to be ordered as well. 

My first thought on the solution is to try the first four numbers, store that in a temp variable, and then just compare to each future value. I'm also thinking about adding some code to catch any four adjacent digits that have a 0 in them, since they'll obviously have a product of 0, but I'm not sure if that's actually any faster than just multiplying them without explicitly checking that first. Let's see!

I'm going to start with a list just because it's easiest. 

Trying out math.prod rather than typing everything out, and using list splicing for the same reason.

Ok, so after using map() to make sure the list elements were all ints, I got the correct answer in 0.0004271 seconds, which is so fast I'm not even going to bother trying any other collection types.

"""

from time import perf_counter 
from math import prod

# TIME CODE STARTS

start = perf_counter()

##########################################################################

initial = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


print(len(str(initial)))

num = list(map(int, str(initial)))
max = 0

for x in range (len(num) -3): #The last digit we need to check has index 996, since 996..999 is the last 4 digit combo. This removes the situation where x+3 is an invalid index
    tempList = num[x:x+13]
    temp = prod(tempList)
    if temp > max:
        max = temp
    
print(max)

##########################################################################


# TIME CODE ENDS

end = perf_counter()

print(f"Finished in {end - start:0.7f} seconds")