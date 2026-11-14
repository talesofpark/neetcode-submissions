class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i,v in enumerate(numbers):
            complement = target - v 
            if complement not in seen:
                seen[v] = i 
            else:
                res.append(seen[complement]+1)
                res.append(i+1)
        return res