temp = 0
temp2 = 0

for x in range(1, 101):
    temp += x

temp = temp * temp

for x in range(1, 101):
    temp2 = temp2 + x * x

print(temp2 - temp)

