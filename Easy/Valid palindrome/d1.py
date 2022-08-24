import re
def isPalindrome(s):
    pattern = "[^0-9a-zA-Z]+"
    cleanstring = re.sub(pattern, "", s)
    lowerclean=cleanstring.lower()
    rev=lowerclean[::-1]
    if rev==lowerclean:
        print('1')
        return True
    else:
        print('0')
        return False



s=' '
isPalindrome(s)