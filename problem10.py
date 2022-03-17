"""
Ok, so my first try for this one was re-using the code from problem 7, but that's clearly going to take ages. While looking into ways of generating primes, I realised that it's way easier to use a sieve (i.e. generate a list 1..N and then remove things) that only leaves primes than it is to actually generate them directly. Since I know we don't want any primes above 2,000,000, I can generate a collection of the integers 1..2,000,000 and then use a sieve. There are some more modern (and usually faster) options but they're less intuitive, so I'm going with Eratosthenes' sieve (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), since he's based. 

"""
from time import perf_counter 
from math import sqrt, floor

# TIME CODE STARTS

start = perf_counter()

##########################################################################


def sieve(n):

    sum1 = 0

    isPrime = [True] * (n-2) #Offset because we start at 2, so we don't want 0 or 1
    print(len(isPrime))

    max = sqrt(n)
    max = floor(max)

    for i in range(2,max):
        if isPrime[i-2]:
            for x in range((i-2)**2, n-2, i):
                isPrime[x] = False

    return isPrime
    


print(sieve(3))

##########################################################################


# TIME CODE ENDS

end = perf_counter()

print(f"Finished in {end - start:0.7f} seconds")