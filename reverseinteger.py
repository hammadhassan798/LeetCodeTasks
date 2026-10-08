class Solution(object):
    def reverse(self, x):
        rev=x
        if(rev==-1 or rev < -1):
        
            rev=abs(rev)
        
        resul=""
        
        while rev:
            if(rev%10 !=0):
             
                 resul+=str(rev%10)
            
            rev=rev//10
        if x==-1 or x < -1 :
          resul="-"+resul 
            
        return int(resul)
obj=Solution()
print(obj.reverse(120))           