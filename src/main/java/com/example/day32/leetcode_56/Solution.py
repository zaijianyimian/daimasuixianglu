from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []
        mi = intervals[0][0]
        ma = intervals[0][1]
        for i in range(1,len(intervals) + 1):
            if  i < len(intervals) and intervals[i][0] <= ma:
                ma = max(ma,intervals[i][1])
            else:
                res.append([mi,ma])
                mi = intervals[i][0]
                ma = intervals[i][1]
        return res