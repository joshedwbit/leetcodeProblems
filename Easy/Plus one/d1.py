def plusOne(digits):
    s=''
    array=[]
    for i in digits:
        s+=str(i)
    added=int(s)+1
    stradded=str(added)
    for i in stradded:
        array.append(i)
    print(array)

    




digits=[1,2,3]
plusOne(digits)
