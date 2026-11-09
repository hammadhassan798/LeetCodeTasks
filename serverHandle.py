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

    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        busyservers = []
        servercounts = [0] * k
        
        freeservers = []
        for i in range(k):
            freeservers.append(i)
            
        for i in range(len(arrival)):
            currenttime = arrival[i]
            duration = load[i]
            
            while busyservers and busyservers[0][0] <= currenttime:
                item = self.popheap(busyservers)
                serverid = item[1]
                
                low = 0
                high = len(freeservers) - 1
                insertpos = len(freeservers)
                while low <= high:
                    mid = (low + high) // 2
                    if freeservers[mid] >= serverid:
                        insertpos = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                freeservers.insert(insertpos, serverid)
                
            if not freeservers:
                continue
                
            preferred = i % k
            assignedserver = -1
            
            low = 0
            high = len(freeservers) - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if freeservers[mid] >= preferred:
                    idx = mid
                    high = mid - 1
                else:
                    low = mid + 1
                    
            if idx != -1:
                assignedserver = freeservers[idx]
                freeservers.pop(idx)
            else:
                assignedserver = freeservers[0]
                freeservers.pop(0)
                
            servercounts[assignedserver] += 1
            finishtime = currenttime + duration
            self.pushheap(busyservers, [finishtime, assignedserver])
            
        maxcount = 0
        for count in servercounts:
            if count > maxcount:
                maxcount = count
                
        resultlist = []
        for i in range(k):
            if servercounts[i] == maxcount:
                resultlist.append(i)
                
        return resultlist