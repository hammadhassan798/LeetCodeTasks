def squaredsum(arr:int):
    n=len(arr)
    sum=0
    for i in range(1,n+1):
        if  n % i == 0 :
            sum+=arr[i-1]**2
    return sum
print(squaredsum([1,2,3,4]))
    
    