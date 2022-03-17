"""
Took me a while, and had to google to find a fast solution. 
2520 is the smallest number that can be divided by all the numbers 1..10, so we may as well start with that, and set that to the step
We can also remove a lot of divisors to test, since a lot of them are redundant (i.e. any number divisible by 20 is divisible by 2, so we don't need to check 2 explicitly)
After that we can just stop the loop when we validate the lowest required divisor, which is 11
We also go faster by checking the biggest divisors first, and then moving downwards, hence reversing the list

"""



var = 2520

ans = False

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

check_list.reverse()



while not ans:
    for x in check_list:
        if var % x == 0:      
            print (x)    
            if x == 11: 
                ans = True
                break
        else:
            print(var)
            var += 2520
            break
    
        
print (var)
