class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""
            
        nines = sum // 9
        remainder = sum % 9

        result = []
        

        for i in range(nines):
            result.append('9')
   
        if remainder > 0:
            result.append(str(remainder))
            

        while len(result) < num:
            result.append('0')
            
        return "".join(result)
        