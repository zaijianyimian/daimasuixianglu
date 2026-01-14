from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                break
            reach = max(reach,i + nums[i])
        return reach >= len(nums) - 1
if __name__ == '__main__':
    s = Solution()
    print(s.canJump([1,1,1,1,0]))