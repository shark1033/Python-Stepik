for i in range(0,len(s)):
    if len(s)==1:
        print(s[0])
        break
    elif i==0:
        l.insert(i, s[1]+s[len(s)-1])
    elif i==len(s)-1:
        l.insert(i, s[0]+s[i-1])
    else:
        l.insert(i, s[i-1]+s[i+1])
    print(l[i], '',end='')
