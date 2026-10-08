s = "()(())()"

li = []
balan = 0

for i in range(len(s)):

    if s[i] == "(":
        balan += 1

        if balan % 2 == 0:
            li.append(1)
        else:
            li.append(0)

    else:  # ')'

        if balan % 2 == 0:
            li.append(1)
        else:
            li.append(0)

        balan -= 1

print(li)