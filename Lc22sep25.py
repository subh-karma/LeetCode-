class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = [0] * 101
        max = 0
        res = 0
        for n in nums:
            freq[n] += 1
            f = freq[n]
            if f > max:
                max = f
                res = f
            elif f == max:
                res += f
        return res
        
