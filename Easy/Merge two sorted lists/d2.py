def mergeTwoLists(list1,list2):
    emptylist=[]
    maxi=max(len(list1),len(list2))
    mini=min(len(list1),len(list2))
    if (len(list1)-len(list2))>0:
        var=2
    elif (len(list1)-len(list2))<0:
        var=1
    else:
        var=0
    for i in range(mini):
        emptylist.append(list1[i])
        emptylist.append(list2[i])
    if var==2:
        # list1 is longer
        for k in range(mini,maxi):
            emptylist.append(list1[k])
    elif var==1:
        # list 2 is longer
        for k in range(mini,maxi):
            emptylist.append(list2[k])
    print(emptylist)
    return emptylist





list1=[]
list2=[0]

mergeTwoLists(list1,list2)