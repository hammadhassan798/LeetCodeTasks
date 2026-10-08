class Solution(object):
    def longestValidParentheses(self, s):

        stack = [-1]
        print( stack)
        max_length = 0

        for i in range(len(s)):

            if s[i] == "(":
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)

                else:
                    length = i - stack[-1]

                    if length > max_length:
                        max_length = length

        return max_length
    
    
obj =Solution()
print(obj.longestValidParentheses("())())"))