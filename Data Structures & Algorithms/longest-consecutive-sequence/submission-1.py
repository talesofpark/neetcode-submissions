class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1: 
            return 0

        nums = sorted(set(nums)) 
        count = 1
        best_count =1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                count += 1
                best_count = max(best_count, count)
            else:
                count = 1 
        return best_count   