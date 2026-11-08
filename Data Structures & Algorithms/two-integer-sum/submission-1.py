class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i,v in enumerate(nums): 
            for j,k in enumerate(nums):
                if i != j and nums[i]+nums[j]== target: 
                    res.append(i)
                    res.append(j)
                    return res
                
