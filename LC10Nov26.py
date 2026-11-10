class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def dfs(i):
            if i == 0:  return 0

            return min(
                dfs(prev) + (i - prev) ** 2
                for prev in range(max(i - 3, 0), i)
            ) + costs[i - 1]

        return dfs(n)
        
