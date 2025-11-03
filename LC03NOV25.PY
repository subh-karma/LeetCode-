class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(n - 1):
            if colors[i] == colors[i + 1]:
                minTime = min(neededTime[i], neededTime[i + 1])
                ans += minTime
                neededTime[i + 1] = max(neededTime[i], neededTime[i + 1])
        return ans
        
