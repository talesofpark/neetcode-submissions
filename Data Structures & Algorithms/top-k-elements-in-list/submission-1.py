class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count --> sort (order in reverse) --> return top K
        seen = {}
        for num in nums: 
            if num not in seen: 
                seen[num]=1
            else:
                seen[num] +=1
        #count dictionary made
        ordered = sorted(seen, key=seen.get, reverse=True) #ordered&reversed now
        return ordered[:k]

        #claude rec for clean up
        #return ordered[:k]
        """ 
        instead of: 

        res = [] 
        for i in range(k): 
            res.append(ordered[i])
        return res
        """
