def subarr(num):
    num.sort()
    result=[]
    for i in range(len(num)):
        for j in range(i,len(num)):
            suba=num[i:j+1]
            result.append(suba)
    
    return result
print(subarr([1,4,3,2,-1]))
            