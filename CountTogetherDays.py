class Solution(object):
    def convertDateToDays(self, datestr):
        daysinmonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(datestr[:2])
        day = int(datestr[3:])
        
        totaldays = day
        for m in range(month - 1):
            totaldays += daysinmonths[m]
        return totaldays

    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        alicestart = self.convertDateToDays(arriveAlice)
        aliceend = self.convertDateToDays(leaveAlice)
        bobstart = self.convertDateToDays(arriveBob)
        bobend = self.convertDateToDays(leaveBob)
        
        overlapstart = max(alicestart, bobstart)
        overlapend = min(aliceend, bobend)
        
        if overlapstart <= overlapend:
            return (overlapend - overlapstart) + 1
            
        return 0
    
p=Solution()
print(p.countDaysTogether("08-15","08-18","08-16","08-19"))