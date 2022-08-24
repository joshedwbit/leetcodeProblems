def romanToInt(s):
    normNum=0
    # normNum is the output integer
    if 'IV' in s:
        normNum+=4
        s=s.replace('IV','')
    if 'IX' in s:
        normNum+=9
        s=s.replace('IX','')
    if 'XL' in s:
        normNum+=40
        s=s.replace('XL','')
    if 'XC' in s:
        normNum+=90
        s=s.replace('XC','')
    if 'CD' in s:
        normNum+=400
        s=s.replace('CD','')
    if 'CM' in s:
        normNum+=900
        s=s.replace('CM','')
    # carries forward s without anomalies
    for i in s:
        if i=='I':
            normNum+=1
        if i=='V':
            normNum+=5
        if i=='X':
            normNum+=10
        if i=='L':
            normNum+=50
        if i=='C':
            normNum+=100
        if i=='D':
            normNum+=500
        if i=='M':
            normNum+=1000

romanToInt('LXXXIX')