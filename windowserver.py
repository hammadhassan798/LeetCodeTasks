class Solution(object):
    def countServers(self, n, logs, x, queries):
       
        sortedlogs = []
        for item in logs:
            sortedlogs.append([item[1], item[0]])
        sortedlogs.sort()
        
        indexedqueries = []
        for i in range(len(queries)):
            indexedqueries.append([queries[i], i])
        indexedqueries.sort()
        
        resultarr = [0] * len(queries)
        servercounts = {}
        leftptr = 0
        rightptr = 0
        
        for q in indexedqueries:
            querytime = q[0]
            originalindex = q[1]
            windowstart = querytime - x
            
            while rightptr < len(sortedlogs) and sortedlogs[rightptr][0] <= querytime:
                timeval = sortedlogs[rightptr][0]
                serverid = sortedlogs[rightptr][1]
                servercounts[serverid] = servercounts.get(serverid, 0) + 1
                rightptr += 1
                
            while leftptr < len(sortedlogs) and sortedlogs[leftptr][0] < windowstart:
                timeval = sortedlogs[leftptr][0]
                serverid = sortedlogs[leftptr][1]
                servercounts[serverid] -= 1
                if servercounts[serverid] == 0:
                    del servercounts[serverid]
                leftptr += 1
                
            activeservers = len(servercounts)
            resultarr[originalindex] = n - activeservers
            
        return resultarr
p=Solution()
print(p.countServers(3,[[1,3],[2,6],[1,5]],5,[10,11]))