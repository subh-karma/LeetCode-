class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        open_count = close_count = unlocked1 = unlocked2 = 0
        for i in range(n):
            # Left-to-right
            if locked[i] == '0':
                unlocked1 += 1
            elif s[i] == '(':
                open_count += 1
            elif s[i] == ')':
                open_count -= 1
            if open_count + unlocked1 < 0:
                return False

            # Right-to-left
            j = n - i - 1
            if locked[j] == '0':
                unlocked2 += 1
            elif s[j] == ')':
                close_count += 1
            elif s[j] == '(':
                close_count -= 1
            if close_count + unlocked2 < 0:
                return False

        return True