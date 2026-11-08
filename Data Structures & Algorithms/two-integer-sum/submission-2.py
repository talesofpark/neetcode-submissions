class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i,v in enumerate(nums): 
            complement_num = target - v
            if complement_num not in seen.keys(): 
                seen[v] = i
            else:
                res.append(seen[complement_num])
                res.append(i)
        return res 