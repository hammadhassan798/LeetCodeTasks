class Solution(object):
    def maximumSaleItems(self, items, budget):
      
        n = len(items)

        cheap = items[0][1]
        bigfac = items[0][0]
        for i in range(n):
            if items[i][1] < cheap:
                cheap = items[i][1]
            if items[i][0] > bigfac:
                bigfac = items[i][0]

        freq = [0] * (bigfac + 1)
        for i in range(n):
            freq[items[i][0]] += 1

        
        mults = [0] * (bigfac + 1)
        for d in range(1, bigfac + 1):
            total = 0
            cur = d
            while cur <= bigfac:
                total += freq[cur]
                cur += d
            mults[d] = total

        deals = []
        for i in range(n):
            fac = items[i][0]
            price = items[i][1]
            freeoptions = mults[fac] - 1
            if freeoptions > 0 and price <= 2 * cheap:
                deals.append([price, freeoptions])

        deals.sort()

        ans = 0
        leftmoney = budget
        for i in range(len(deals)):
            price = deals[i][0]
            freeoptions = deals[i][1]
            canbuy = leftmoney // price
            take = freeoptions
            if canbuy < take:
                take = canbuy
            ans += 2 * take
            leftmoney -= take * price

        ans += leftmoney // cheap
        return ans
p=Solution()
print(p.maximumSaleItems([[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]],35))