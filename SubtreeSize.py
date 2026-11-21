class Solution(object):
    def findSubtreeSizes(self, parent, s):
        
        n = len(parent)
        origadj = [[] for i in range(n)]
        for i in range(1, n):
            origadj[parent[i]].append(i)

        newp = list(parent)
        lastseen = [-1] * 26
        saved = [-1] * n
        stack = [(0, 0)]

        while stack:
            node, state = stack.pop()
            idx = ord(s[node]) - ord("a")
            if state == 0:
                if node > 0 and lastseen[idx] != -1:
                    newp[node] = lastseen[idx]
                saved[node] = lastseen[idx]
                lastseen[idx] = node
                stack.append((node, 1))
                for nxt in origadj[node]:
                    stack.append((nxt, 0))
            else:
                lastseen[idx] = saved[node]

        finaladj = [[] for _ in range(n)]
        for i in range(1, n):
            finaladj[newp[i]].append(i)

        ans = [1] * n
        order = [(0, 0)]
        while order:
            node, state = order.pop()
            if state == 0:
                order.append((node, 1))
                for nxt in finaladj[node]:
                    order.append((nxt, 0))
            else:
                total = 1
                for nxt in finaladj[node]:
                    total += ans[nxt]
                ans[node] = total

        return ans