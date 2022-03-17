limit = 4000000
sum = 0
max = False

a, b = 0, 1
while max == False:
    a, b = b, a + b
    if b > limit:
        max = True
        print (sum)
        break
    else:
        if b % 2 == 0:
            sum += b