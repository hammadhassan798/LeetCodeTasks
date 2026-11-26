class Solution(object):
    def canAliceWin(self, n):
        counter=10
        Alice=False
        bob=False
        check=-1
        if n<10:
           return False
              
        if n >=10:
            n-=counter
            check=0
        while n != 0:
          
                counter-=1
                if counter <= n :
                 n-=counter
                else :
                    break
                if counter % 2 == 0:
                    check=0
                else :
                    check=1
        if check == 0 :
            return True
        else :
            return False       

                
p=Solution()
print(p.canAliceWin(2))           