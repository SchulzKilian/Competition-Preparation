

x = input().split()

rows, columns = int(x[0]),int(x[1])
oldrow = ["P","P","P","P"]
testmatrix =[[1 for i in range(rows-1)] for k in range(columns-1)]
for i in range(columns):
    newrow = input().split()
    print("Iteration number" + str(i))
    print("Old row: " + str(oldrow))
    print("New row: " + str(newrow))
    for k in range(rows):
        item = newrow[k]
        if item == 0:
            continue
        elif item == "?":
            continue
        elif item == "I":
            
            if k >0:



    

    oldrow = newrow
