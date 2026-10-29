class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        treegraph = [[] for i in range(n)]
        for edge in edges:
            nodea = edge[0]
            nodeb = edge[1]
            treegraph[nodea].append(nodeb)
            treegraph[nodeb].append(nodea)
            
        nodechars = list(s)
        answerlist = []
      
        for queryitem in queries:
            parts = queryitem.split()
            operation = parts[0]
            
            if operation == "update":
                targetnode = int(parts[1])
                newchar = parts[2]
                nodechars[targetnode] = newchar
                
            elif operation == "query":
                nodeu = int(parts[1])
                nodev = int(parts[2])
                
                pathnodes = []
                queue = [[nodeu, [nodeu]]]
                visitedset = {nodeu}
                
                foundpath = False
                while queue and not foundpath:
                    curr = queue.pop(0)
                    curnode = curr[0]
                    curpath = curr[1]
                    
                    if curnode == nodev:
                        pathnodes = curpath
                        foundpath = True
                        break
                        
                    for neighbor in treegraph[curnode]:
                        if neighbor not in visitedset:
                            visitedset.add(neighbor)
                            queue.append([neighbor, curpath + [neighbor]])
                            
                charcounts = {}
                for nodeidx in pathnodes:
                    char = nodechars[nodeidx]
                    if char in charcounts:
                        charcounts[char] += 1
                    else:
                        charcounts[char] = 1
                        
                oddcount = 0
                for count in charcounts.values():
                    if count % 2 != 0:
                        oddcount += 1
                        
                if oddcount <= 1:
                    answerlist.append(True)
                else:
                    answerlist.append(False)
                    
        return answerlist