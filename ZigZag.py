def zigzagpattern(s, numRows):

    if numRows == 1:
        return s

    rows = [[] for i in range(numRows)]

    row = 0
    direction = 1

    for i in s:

        rows[row].append(i)

        if row == numRows - 1:
            direction = -1

        elif row == 0:
            direction = 1

        row += direction

    answer = ""

    for r in rows:
        answer += "".join(r)

    return answer


print(zigzagpattern("PAYPALISHIRING", 3))