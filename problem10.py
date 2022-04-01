"""
Ok, so my first try for this one was re-using the code from problem 7, but that's clearly going to take ages. While looking into ways of generating primes, I realised that it's way easier to use a sieve (i.e. generate a list 1..N and then remove things) that only leaves primes than it is to actually generate them directly. Since I know we don't want any primes above 2,000,000, I can generate a collection of the integers 1..2,000,000 and then use a sieve. There are some more modern (and usually faster) options but they're less intuitive, so I'm going with Eratosthenes' sieve (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), since he's based. 

Ok, came back to this later, gave up and decided to just use numpy, and honestly I'd forgotten how awesome it is. This runs in 0.0086379 seconds, which is just insane.

"""
from time import perf_counter 
import numpy as np

# TIME CODE STARTS

start = perf_counter()

##########################################################################



def primes(n):
    x = np.ones((n+1,), dtype=bool)
    x[0] = False
    x[1] = False
    for i in range(2, int(n**0.5)+1):
        if x[i]:
            x[2*i::i] = False

    primes = np.where(x == True)[0]
    ans = primes.sum()
    return ans

print(primes(2_000_000))

##########################################################################


# TIME CODE ENDS

end = perf_counter()

print(f"Finished in {end - start:0.7f} seconds")