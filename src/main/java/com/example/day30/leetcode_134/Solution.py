class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = -1
        curSum = 0
        if sum(gas) < sum(cost): return res
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            if curSum < 0:
                res = i + 1
                curSum = 0
        if res >= len(gas) or res == -1:
            return -1
        return res