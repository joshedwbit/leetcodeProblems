def removeElement(integer,val):
    origArrayLength=len(int)
    for i in int:
        if i==val:
            int.remove(i)
    modifiedArrayLength=len(int)
    leftover=origArrayLength-modifiedArrayLength
    for i in range(leftover):
        int.append(0)

    print(int)
    


int=[3,2,2,3]
val=3
removeElement(int,val)
