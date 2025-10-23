class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s) - 2
        cur = 1
        left = int(s[0])
        right = int(s[n + 1])

        for i in range(n):
            cur *= (n - i)
            cur //= (i + 1)
            left = (left + int(s[i + 1]) * cur) % 10
            right = (right + int(s[n - i]) * cur) % 10

        return left == right
        
