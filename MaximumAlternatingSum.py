def maxsum(arr:int):
    squares = [x * x for x in arr]
       
    squares.sort()
        
    n = len(squares)
    negative_count = n // 2  
        
    score = 0
        
    for i in range(negative_count):
            score -= squares[i]
            
    for i in range(negative_count, n):
            score += squares[i]
            
    return score
            
            
        
print(maxsum([1,2,3]))