def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [i[0] for i in intervals]
        start.sort()
        end = [i[1] for i in intervals]
        end.sort()
        res, count = 0,0
        k,l = 0,0
        while k < len(intervals):
            if start[k] < end[l]:
                count += 1
                k += 1
            else:
                count -= 1
                l += 1
            res = max(res,count)
        return res