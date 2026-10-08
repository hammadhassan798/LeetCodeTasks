class Solution(object):
    def isValid(self, s):
        li = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:

            if i in "([{":
                li.append(i)

            elif i in ")]}":

                if len(li) == 0:
                    return False

                if li[-1] != pairs[i]:
                    return False

                li.pop()

        return len(li) == 0