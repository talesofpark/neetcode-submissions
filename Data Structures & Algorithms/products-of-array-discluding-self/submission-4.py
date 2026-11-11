class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        curr_l =1
        for x in nums: 
            curr_l = curr_l * x
            left.append(curr_l)
        right = []
        curr_r =1
        for x in nums[::-1]: 
            curr_r = curr_r * x
            right.append(curr_r)

        res = []
        for i in range(len(nums)):
            j = len(nums)-2 - i
            k = -1+i
            #if (j>-1) and (k < len(nums)-1): 
            if (k < len(nums)-1 ): 
                if k<0: 
                    res.append(right[j])
                elif (k>=0) and (j>-1):
                    res.append(right[j]*left[k])
                else: 
                    res.append(left[k])
        return res

        
