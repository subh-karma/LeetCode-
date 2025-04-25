class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = defaultdict(int)
        freq[0], prefix, result = 1, 0, 0
        for x in nums:
            if x % modulo == k:
                prefix += 1
            m = prefix % modulo
            need = (m - k) % modulo
            result += freq[need]
            freq[m] += 1
        return result
        
