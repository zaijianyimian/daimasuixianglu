from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        arr = [0] * 26
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] = i
        res = []
        i = 0
        while i < len(s):
            if i == arr[ord(s[i]) - ord('a')]:
                res.append(1)
                i += 1
                continue
            end = arr[ord(s[i]) - ord('a')]
            cur = 1
            j = i
            while j < end:
                end = max(end,arr[ord(s[j]) - ord('a')])
                j += 1
                cur += 1
            res.append(cur)
            i = j + 1
        return res