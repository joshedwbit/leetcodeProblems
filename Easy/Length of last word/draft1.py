def lengthoflastword(s):
    stripped=s.strip()
    array=stripped.split()
    return len(array[-1])



s="hello world my name is Joshua a dhusvab"

lengthoflastword(s)
    
