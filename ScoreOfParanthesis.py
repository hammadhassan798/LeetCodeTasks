def score(s):

    lis = []
    count = 0

    for i in s:

        if i == "(":
            lis.append(0)

        elif i == ")":

            value = lis.pop()

           
            if value == 0:
                value = 1

           
            else:
                value = 2 * value

            
            if lis:
                lis[-1] += value

            
            else:
                count += value

    return count


print(score("(()()())()"))