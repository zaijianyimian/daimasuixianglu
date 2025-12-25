class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0,len(arr),k * 2):
            self.reverse(arr,i,min(i + k,len(arr)) - 1)
        return ''.join(arr)
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1