class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #2nd try, fresh, only should move when the actual length to move make sense 
        #while loop to actually check without having to iterate all left pointers sequentially
        
        #init 
        maxA = 0
        maxH = 0
        maxB = 0
        left = 0 
        right = len(heights)-1

        while left < right: 
            #check base and height and area
            currB = right - left
            currH = min(heights[left], heights[right])
            currA = currB * currH

            maxA = max(maxA, currA)

            #if stmts to check 
            if heights[left] < heights[right]:
                #move left pointer
                left +=1
            else:
                right -=1 

        return maxA


