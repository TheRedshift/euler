"""
First thought here is that I want to generate a collection of valid solutions to a+b+c = 1000 while a<b<c, but I'm actually not sure that's worthwhile, since I'll get a ton of 1,2, 997 style values there. The question is, is it faster to do that, then check which of them are valid Pythagorean triplets (we can stop at the first one since the problem confirms there's only one), or is there a smarter way to eliminate some of them early?

Alternatively maybe I try to generate valid Pythagorean triplets and then check that a+b+c is 1000. That might be faster since there should be far fewer of them, but each of them will take longer to validate than the first option. I'm going to try this one first I think.

Ok, I've realised I can speed up the generation because I know that a can't be more than 332, since a<b<c, and 332 + 333 + 334 is 999, so there's no bigger valid value for a. b can't be more than 499 for the same reason. 

We can also check the 1000 sum condition in the same loop cheaply thanks to the lazy evaluation, so we don't have to generate a list of tuples at all, we can just iterate over until we find the magic triplet.

The last bit was to add a variable (ans) to break out of all the nested loops since I didn't write this as a function, but in general I'm quite happy with this! Took 4.8665390 seconds, which I think is good enough to not bother with trying the option where I generate all the triplets (or all the a,b,c combos that sum to 1000) as well.

Ok, so just before I went to bed I googled this one, and it turns out you can do it insanely fast (see problem9Better.py from https://radiusofcircle.blogspot.com/2016/04/problem-9-project-euler-solution-with-python.html) with either Dickinson's method or the one from here (https://www.mathsisfun.com/numbers/pythagorean-triples.html), which are both much faster ways of actually finding valid triplets. problem9Better uses Euclid's Formula, which I haven't seen before, and completely smashes my "dumb" solution, running in 0.0001411437 seconds. Ouch. Oh well, I guess I'm not a mathematician... 

"""
from time import perf_counter 

# TIME CODE STARTS

start = perf_counter()

##########################################################################

ans = False


for c in range (1, 1000): #Doing them backwards since we're enforcing a<b<c
    if ans == True:
        break
    for b in range (1, 500):
        if ans == True:
            break
        for a in range (1, 332):
            if (a+b+c == 1000) and (a<b<c) and (a**2 + b**2 == c**2): #Ordered like this because Python uses lazy evaluation and the first statement is far easier to compute
                print({a,b,c})
                print(a*b*c)
                ans = True
                break

##########################################################################


# TIME CODE ENDS

end = perf_counter()

print(f"Finished in {end - start:0.7f} seconds")