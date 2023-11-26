x = int(input())

k = 0
useddivisors = []
divisor = 2

while x > divisor:
    divisor = 2
    while x%divisor != 0 or divisor in useddivisors:
        divisor +=1


    k+=1
    useddivisors.append(divisor)
    x = x/divisor







print(k)