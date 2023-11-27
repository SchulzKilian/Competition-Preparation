

x = input().split()

rows, columns = int(x[0]),int(x[1])
oldrow = []
testmatrix =[[1 for i in range(rows-1)] for k in range(columns-1)]
for i in range(rows):
    newrow = list(input())
    if oldrow:
        for k in range(1,columns-1):
            item = newrow[k]
            if item == 0:
                continue
            elif item == "?":
                continue
            elif item == "I":
                if k >0:
                    testmatrix[i][k-1] = 0
                    testmatrix[i-1][k-1]= 0
                testmatrix[i-1][k] = 0
            elif item == "C":
                testmatrix[i][k]= 0
                testmatrix[i-1][k]= 0
            elif item == "P":
                testmatrix[i][k]= 0
                if k >0:
                    testmatrix[i][k-1] = 0
                    testmatrix[i-1][k-1]= 0




    

    oldrow = newrow
counter = 0
for k in testmatrix:
    for i in k:
        if i == 1:
            counter +=1

fields = rows*columns


result = counter*(3**(fields-4)) - (2**counter - counter -1)
print(result)