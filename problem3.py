n = 600851475143
temp = 2
c = 0
primes = []

def isPrime(x):
    flag = False
    if x > 1:
    # check for factors
        for i in range(2, x):
            if (x % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        return False
    else:
        return True

ans = False

while temp <= n:
    if isPrime(temp):
        if n % temp == 0:
            primes.append(temp)
            n = n / temp
            temp = 2
            print(primes)
            print(n)
        else:
            temp += 1          
    else:
        temp += 1

print(max(primes))