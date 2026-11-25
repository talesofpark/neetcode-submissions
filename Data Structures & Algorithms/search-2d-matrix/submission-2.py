class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #claude guided change if order 
        i = 0
        j = len(matrix)-1
        #row1 = matrix[i]
        #row2 = matrix[j]
        foundrow = 0
        while i <= j:
            #have to make midr adaptable to new sizes 
            midr = (i + j)//2
            if matrix[midr][0] > target: 
                j = midr-1
            elif matrix[midr][-1] < target:
                i = midr+1
            #check if the row 1 and row 2 are looking at the same row 
            else: 
                foundrow = midr 
                break #found the row 
            #if the target smaller than midpoint 
            
        
        #we now have a row lets find the colm
        #in here we can also return false 
        #now should be the same tech as the normal bin search
        
        left = 0
        right = len(matrix[0])-1

        while left <=right: 
            midc = (left + right) //2 
            if matrix[foundrow][midc] == target: 
                return True 
            #if the midpoint n is bigger than target
            elif matrix[foundrow][midc] > target: 
                right = midc-1 
            else:
                left = midc+1 
        
        #else nothing found
        return False 