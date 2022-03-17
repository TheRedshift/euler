"""
Ok, so my first try for this one was re-using the code from problem 7, but that's clearly going to take ages. While looking into ways of generating primes, I realised that it's way easier to use a sieve (i.e. generate a list 1..N and then remove things) that only leaves primes than it is to actually generate them directly. Since I know we don't want any primes above 2,000,000, I can generate a collection of the integers 1..2,000,000 and then use a sieve. There are some more modern (and usually faster) options but they're less intuitive, so I'm going with Eratosthenes' sieve (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), since he's based. 

"""
from time import perf_counter 

# TIME CODE STARTS

start = perf_counter()

##########################################################################


var = 5 #First non-even prime + 2 (since we only want odd numbers)

primes = {3} # First non-even prime, no point checking 2 since it's the only even prime

sum = 2 # Sum of the primes we've found

index = 2 # Because 3 is the 2nd prime

while index != 2000000:
    prime = True
    for x in primes:
        if var % x == 0:
            var += 2
            prime = False
            break
    if prime:
        primes.add(var)
        sum += var
        print(index)
        if index == 2000000: #Checking 10,000 because the index hasn't been incremented yet, but this is actually the prime at index 10,001
            print(sum)
            break
        var += 2
        index += 1


##########################################################################


# TIME CODE ENDS

end = perf_counter()

print(f"Finished in {end - start:0.7f} seconds")