import re
def isPalindrome(s):
    lowerclean = (re.sub("[^0-9a-zA-Z]+", "", s)).lower()
    if lowerclean==lowerclean[::-1]:
        print('1')
        return True
    else:
        print('0')
        return False



s=' '
isPalindrome(s)