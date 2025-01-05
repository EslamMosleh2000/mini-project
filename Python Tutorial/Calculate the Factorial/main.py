n = int (input ("enter the number  "))
factorial= 1
for i in range (n+1):
    if i == 0 :
        continue
    else:

        factorial *= i

print (factorial)