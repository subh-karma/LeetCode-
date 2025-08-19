class Solution:
    def farMin(self, arr):
        n = len(arr)
        ans = [-1] * n

        # Create a list of (value, index) and sort by value
        value_index_pairs = sorted([(val, idx) for idx, val in enumerate(arr)])
        
        farthest_idx = value_index_pairs[0][1]  # Start with the smallest value's index

        for _, idx in value_index_pairs:
            if idx < farthest_idx:
                ans[idx] = farthest_idx
            else:
                farthest_idx = idx

        return ans
        # Code Here
        
