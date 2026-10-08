def longestPalindrome( s):

        longest = ""

        for i in range(len(s)):

            # Odd length palindrome
            left = i
            right = i

            while left >= 0 and right < len(s):

                if s[left] != s[right]:
                    break

                current = s[left:right + 1]

                if len(current) > len(longest):
                    longest = current

                left -= 1
                right += 1

            # Even length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < len(s):

                if s[left] != s[right]:
                    break

                current = s[left:right + 1]

                if len(current) > len(longest):
                    longest = current

                left -= 1
                right += 1

        return longest
    
print(longestPalindrome("ababab"))