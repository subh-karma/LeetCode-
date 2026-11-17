class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Precompute minimum changes for every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                # Try all proper divisors
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Check palindrome groups
                    for r in range(d):
                        left = i + r
                        right = i + r + ((length // d) - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # DP: dp[t][i] = minimum cost to partition
        # first i characters into exactly t substrings
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for t in range(1, k + 1):
            for i in range(2 * t, n + 1):
                for j in range(2 * (t - 1), i - 1):
                    dp[t][i] = min(
                        dp[t][i],
                        dp[t - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
        
