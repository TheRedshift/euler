"""
This one honestly took me about a minute to write, and it finishes in less than a second. Not sure how you could possibly make this better/faster since it was so

"""

temp = 0
temp2 = 0

for x in range(1, 101):
    temp += x

temp = temp * temp

for x in range(1, 101):
    temp2 = temp2 + x * x

print(temp - temp2)

