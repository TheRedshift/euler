def bigPal():

    best = 0

    for x in range(999, 1, -1):
        for y in range(999, 1, -1):
            palindrome = True
            temp = x * y
            tempStr = str(temp)
            innerTemp = len(tempStr) // 2
            current = 0
            end = len(tempStr)-1 
            while current <= innerTemp:
                if tempStr[current] == tempStr[end]:
                    current += 1
                    end -= 1
                else:
                    palindrome = False
                    break
            if palindrome == True and temp > best: 
                print(x,y, tempStr)
                best = temp
                break

    return best

print(bigPal())

