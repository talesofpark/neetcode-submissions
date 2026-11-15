class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #array is sorted and increasing order
        #O(1) additional space

        left = 0
        right = len(numbers)-1
        #for i,v in enumerate(numbers):
        while True: 
            sum = numbers[left] + numbers[right]
            if target == sum:
                return [left+1,right+1]
                break
            else:
                if sum >= target: 
                    right -=1
                elif sum < target: 
                    left +=1
                else:
                    break
                
            