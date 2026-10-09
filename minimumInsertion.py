def minInsertions(s):
        balance = 0  
        count = 0  

        for char in s:
            if char == "(":
               
                if balance % 2 == 1:
                    count += 1
                    balance -= 1
                
                balance += 2

            else:  
                balance -= 1

                if balance < 0:
                    count += 1
                    balance += 2

        return count + balance