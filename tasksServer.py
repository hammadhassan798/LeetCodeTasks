class Solution(object):
    def pushheap(self, heap, item):
        heap.append(item)
        idx = len(heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if heap[idx] < heap[parent]:
                heap[idx], heap[parent] = heap[parent], heap[idx]
                idx = parent
            else:
                break

    def popheap(self, heap):
        if not heap:
            return None
        top = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            idx = 0
            length = len(heap)
            while True:
                left = 2 * idx + 1
                right = 2 * idx + 2
                smallest = idx
                if left < length and heap[left] < heap[smallest]:
                    smallest = left
                if right < length and heap[right] < heap[smallest]:
                    smallest = right
                if smallest != idx:
                    heap[idx], heap[smallest] = heap[smallest], heap[idx]
                    idx = smallest
                else:
                    break
        return top

    def assignTasks(self, servers, tasks):
       
        freeservers = []
        for i in range(len(servers)):
            self.pushheap(freeservers, [servers[i], i])
            
        busyservers = []
        ans = [0] * len(tasks)
        currenttime = 0
        
        for j in range(len(tasks)):
            if currenttime < j:
                currenttime = j
                
            while busyservers and busyservers[0][0] <= currenttime:
                item = self.popheap(busyservers)
                releasetime = item[0]
                serverweight = item[1]
                serverindex = item[2]
                self.pushheap(freeservers, [serverweight, serverindex])
                
            if not freeservers:
                item = self.popheap(busyservers)
                currenttime = item[0]
                releasetime = item[0]
                serverweight = item[1]
                serverindex = item[2]
                self.pushheap(freeservers, [serverweight, serverindex])
                
                while busyservers and busyservers[0][0] <= currenttime:
                    item = self.popheap(busyservers)
                    self.pushheap(freeservers, [item[1], item[2]])
                    
            serveritem = self.popheap(freeservers)
            chosenweight = serveritem[0]
            chosenindex = serveritem[1]
            ans[j] = chosenindex
            
            finishtime = currenttime + tasks[j]
            self.pushheap(busyservers, [finishtime, chosenweight, chosenindex])
            
        return ans
    
p=Solution()
print(p.assignTasks( [3,3,2],[1,2,3,2,1,2]))