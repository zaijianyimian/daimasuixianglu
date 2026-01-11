class Solution:
    def merge(self,nums: list[int],left: int,mid:int,right: int) -> None:
        # 创建临时数组存储结果
        tmp = [0] * (right - left + 1)
       # 初始化左右数组起始索引
        i,j,k = left,mid + 1,0
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            tmp[k] = nums[j]
            j += 1
            k += 1
        for k in range(0,len(tmp)):
            nums[left + k] = tmp[k]
    def mergeSort(self,nums: list[int],left: int,right: int):
        if left >= right:
            return
        mid = (left + right) // 2
        self.mergeSort(nums,left,mid)
        self.mergeSort(nums,mid + 1,right)
        self.merge(nums,left,mid,right)