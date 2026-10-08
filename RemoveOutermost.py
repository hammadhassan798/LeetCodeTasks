def remove(s):
    
    balance =0
    lis=[]
    for i in s :
        if i == "(" :
            if balance > 0 :
             lis.append(i)
            balance+=1
            
        elif i == ")":

         balance -= 1

         if balance > 0:
                lis.append(i)
            
    return lis
print(remove("()()"))