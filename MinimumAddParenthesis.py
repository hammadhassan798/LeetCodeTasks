def mini(s):

    count = 0
    lis = []

    for i in s:

        if i == "(":
            lis.append(i)

        elif i == ")":

            if lis and lis[-1] == "(":
                lis.pop()

            else:
                count += 1

    return count + len(lis)
print (mini("((("))