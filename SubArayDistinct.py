class Solution(object):
    def sumCounts(self, nums):
        
        totalSum=0
        n=len(nums)
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                distinctcount = len(seen)
                totalSum += distinctcount ** 2
        return totalSum
p=Solution()
print(p.sumCounts([2,2]))
# but not acceptable by leet code 
class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, left, right):
            if lazy[node] == 0:
                return

            mid = (left + right) // 2
            val = lazy[node]

            for child, length in (
                (node * 2, mid - left + 1),
                (node * 2 + 1, right - mid)
            ):
                old = total[child]
                squares[child] += 2 * val * old + val * val * length
                total[child] += val * length
                lazy[child] += val

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                length = right - left + 1
                old = total[node]

                squares[node] += 2 * old + length
                total[node] += length
                lazy[node] += 1
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = total[node * 2] + total[node * 2 + 1]
            squares[node] = squares[node * 2] + squares[node * 2 + 1]

        last = {}
        ans = 0

        for i, num in enumerate(nums):
            prev = last.get(num, -1)

            update(1, 0, n - 1, prev + 1, i)

            last[num] = i
            ans = (ans + squares[1]) % MOD

        return ans
