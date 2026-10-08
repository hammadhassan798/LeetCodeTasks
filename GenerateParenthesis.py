class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open, close):

            if open == n and close == n:
                result.append(current)
                return

            if open < n:
                backtrack(current + "(", open + 1, close)

            if close < open:
                backtrack(current + ")", open, close + 1)

        backtrack("", 0, 0)

        return result
onje=Solution()
print(onje.generateParenthesis(3))


    
    #with iterator
    
class Solution:
    def generateParenthesis(self, n):
        result = []
        stack = [("", 0, 0)]

        while stack:
            current, open, close = stack.pop()

            # Complete valid combination
            if open == n and close == n:
                result.append(current)
                continue

            # Try adding '('
            if open < n:
                stack.append((current + "(", open + 1, close))

            # Try adding ')'
            if close < open:
                stack.append((current + ")", open, close + 1))

        return result