

x = input().split()

rows, columns = int(x[0]),int(x[1])
oldrow = []
testmatrix =[[1 for i in range(rows-1)] for k in range(columns-1)]
for i in range(rows):
    newrow = list(input())
    print("Iteration number" + str(i))
    print("Old row: " + str(oldrow))
    print("New row: " + str(newrow))
    if oldrow:
        for k in range(1,columns-1):
            item = newrow[k]
            print(item)
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


print(testmatrix)