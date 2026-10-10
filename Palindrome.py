def palin(s):
    i=0
    j=len(s)-1
    found=False
    while i >= 0 and j>=i:
        if s[i]==s[j]:
            i+=1
            j-=1
            continue
        else :
            return found 
    found=True
    return found
print(palin("10"))