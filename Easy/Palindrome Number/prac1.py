from numpy import true_divide


array=[]
def isPalindrome(x):
    # lengthx=len(str(x))
    # strx=str(x)
    # if lengthx%2==0:
    #     y=lengthx/2
    # else:
    #     y=(lengthx+1)/2
    # y returns the position of middle element
    rev=str(x)[::-1]
    # uses start stop step STRING slicing - which is why you must convert to string
    if rev==str(x):
        # x must be a string, allows for negative number integers (otherwise breaks)
        print(1)
        return True

isPalindrome(123321)