class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        for c in t:
            arr[ord(c) - ord('a')] -= 1
        for i in range(26):
            if arr[i] != 0:
                return False
        return True