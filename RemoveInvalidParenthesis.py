class Solution(object):
    def removeInvalidParentheses(self, s):

        left_remove = 0
        right_remove = 0

        # Find how many '(' and ')' need to be removed
        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, path, open_count, close_count,
                      left_remove, right_remove):

            # End of string
            if index == len(s):
                if left_remove == 0 and right_remove == 0:
                    if open_count == close_count:
                        result.add("".join(path))
                return

            ch = s[index]

            # If current character is '('
            if ch == '(':

                # Remove it
                if left_remove > 0:
                    backtrack(
                        index + 1,
                        path,
                        open_count,
                        close_count,
                        left_remove - 1,
                        right_remove
                    )

                # Keep it
                path.append('(')

                backtrack(
                    index + 1,
                    path,
                    open_count + 1,
                    close_count,
                    left_remove,
                    right_remove
                )

                path.pop()

            # If current character is ')'
            elif ch == ')':

                # Remove it
                if right_remove > 0:
                    backtrack(
                        index + 1,
                        path,
                        open_count,
                        close_count,
                        left_remove,
                        right_remove - 1
                    )

                # Keep it only if valid
                if close_count < open_count:

                    path.append(')')

                    backtrack(
                        index + 1,
                        path,
                        open_count,
                        close_count + 1,
                        left_remove,
                        right_remove
                    )

                    path.pop()

            # If current character is a letter
            else:

                path.append(ch)

                backtrack(
                    index + 1,
                    path,
                    open_count,
                    close_count,
                    left_remove,
                    right_remove
                )

                path.pop()

        backtrack(
            0,
            [],
            0,
            0,
            left_remove,
            right_remove
        )

        return list(result)