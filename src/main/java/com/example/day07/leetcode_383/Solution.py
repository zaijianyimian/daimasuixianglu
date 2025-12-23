class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        arr = [0] * 26
        for i in range(len(magazine)):
            arr[ord(magazine[i]) - 97] += 1
        for i in range(len(ransomNote)):
            if arr[ord(ransomNote[i]) - 97] > 0:
                arr[ord(ransomNote[i]) - 97] -= 1
            else:
                return False
        return True

