def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        for i in range(1, len(intervals)):
            if (intervals[i][0] < intervals[i-1][1]):
                intervals[i] = [min(intervals[i][0], intervals[i -1][0]),
                min(intervals[i][1], intervals[i-1][1])]
                count +=1
        return count