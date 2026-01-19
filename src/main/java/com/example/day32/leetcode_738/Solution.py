class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        for i in range(len(s) - 1,0,-1):
            if s[i] < s[i - 1]:
                s[i - 1] = str(int(s[i - 1]) - 1)
                for j in range(i,len(s)):
                    s[j] = '9'
        return int(''.join(s))
