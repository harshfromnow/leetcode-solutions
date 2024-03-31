class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = []
        i = 0
        n = len(intervals)
        
        # Append intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            l.append(intervals[i])
            i += 1
        
        # Merge intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        l.append(newInterval)
        
        #Append intervals that come after newInterval
        while i < n:
            l.append(intervals[i])
            i += 1
        
        return l