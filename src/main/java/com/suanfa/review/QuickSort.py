class QuickSort:
    def partition(self,nums: list[int],left: int,right : int) -> int:
        i,j = left,right
        while i < j:
            while i < j and nums[i] <= nums[i] <= nums[j]:
                i += 1
            while i < j and nums[j] >= nums[left]:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]
            nums[i],nums[left] = nums[left],nums[i]
        return i
    def quickSort(self,nums: list[int],left: int,right: int) -> None:
        if left >= right:
            return
        # 划分边界
        privort = self.partition(nums,left,right)
        # 递归处理左数组
        self.quickSort(nums,left,privort - 1)
        # 递归处理右数组
        self.quickSort(nums,privort + 1,right)