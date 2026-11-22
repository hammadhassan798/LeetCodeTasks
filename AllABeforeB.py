class Solution(object):
    def checkstring(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seenb = False

        for ch in s:
            if ch == "b":
                seenb = True
            elif ch == "a" and seenb:
                return False

        return True


p = Solution()
print(p.checkstring("aababb"))