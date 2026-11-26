class Solution(object):
    def numberOfSubstrings(self, s):
       
        n = len(s)
        counta = 0
        countb = 0
        countc = 0
        left = 0
        total = 0

        for right in range(n):
            ch = s[right]
            if ch == "a":
                counta += 1
            elif ch == "b":
                countb += 1
            else:
                countc += 1

            while counta > 0 and countb > 0 and countc > 0:
                total += n - right
                leftch = s[left]
                if leftch == "a":
                    counta -= 1
                elif leftch == "b":
                    countb -= 1
                else:
                    countc -= 1
                left += 1

        return total


p = Solution()
print(p.numberofsubstrings("abcabc"))