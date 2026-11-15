class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        #i,j,k = 0,1, len(nums)-1
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            j,k = i+1, len(nums)-1

            while j<k:
                current_sum = nums[j] + nums[k]
                target = -nums[i]
                if target == current_sum: 
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -=1
                    while j < k and nums[j] == nums[j-1]: #fix 2: skip repeated j
                        j += 1
                elif current_sum < target: 
                    j += 1
                else:
                    k -= 1
                
        return res

        