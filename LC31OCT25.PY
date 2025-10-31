class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += 1  # Shift values to avoid zero-index issues

        ans = []
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                ans.append(index)
            else:
                nums[index] *= -1  # Mark as visited

        return ans
