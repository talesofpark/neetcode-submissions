class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #array is sorted and increasing order
        #O(1) additional space

        left = 0
        right = len(numbers)-1
        #for i,v in enumerate(numbers):
        while True: 
            c_sum= numbers[left] + numbers[right]
            if target == c_sum:
                return [left+1,right+1]
            else:
                if c_sum >= target: 
                    right -=1
                elif c_sum < target: 
                    left +=1
                
            