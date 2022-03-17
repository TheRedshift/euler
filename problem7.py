"""

Off the bat, I'm thinking:

Loop over a variable incrementing by 2 (skip all evens for obvious reasons), and add each prime to a list. Then check each new prime against that list of primes, keep going until we've the list is 10,001 elements long. Might not be that fast but I'm going to try that first.

Ok that actually worked really well, super easy to write and finishes in a couple of seconds. I wonder how much of that is due to the speed difference between sets and lists?

"""

var = 5 #First non-even prime + 2 (since we only want odd numbers)

primes = {3} # First non-even prime, no point checking 2 since it's the only even prime

index = 2 # Because 3 is the 2nd prime

while index != 10001:
    prime = True
    for x in primes:
        if var % x == 0:
            var += 2
            prime = False
            break
    if prime:
        if index == 10000: #Checking 10,000 because the index hasn't been incremented yet, but this is actually the prime at index 10,001
            print(var)
            break
        primes.add(var)
        var += 2
        index += 1
        #print(index)

#print(var)
        

