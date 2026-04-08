class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for (l, r, k ,v) in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % 1_000_000_007
                idx += k
        
        acc = nums[0]
        for n in nums[1:]:
            acc ^= n
        return acc
        
