class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #not sure as to how to efficiently check for the sub boxes yet
        #check for row and col
        #do we even need hash sets? why not append to list and check if seen? 
        #dont want to reloop over every list again, so faster look up 
        # so maybe dict is better, then what? j check if it exists?
        #also dont need to be solvable? so we only care about the dupes?
        #dupes in row, col, or box? 

        #seen_row = {} #we would want this to reset for every row tho 
        #seen_col = {} #same here, reset for every col
        """
        for row in board: #0-8
            seen_row = {}
            seen_col = {}
            for col in row: #row checker 
        """ 
        #row checker
        for r in range(9):
            seen_r = set() #resets every row 
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                else:
                    if board[r][c] in seen_r:
                        return False 
                    else: 
                        seen_r.add(board[r][c])
                
        #wait fresh start, hold every col 
        #col checker 
        for c in range(9):
            seen_c = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue 
                else:
                    if board[r][c] in seen_c:
                        return False 
                    else: 
                        seen_c.add(board[r][c])

        #box checker
        for b in range(9): #9boxes 
            #b_list = []
            seen_b = set()
            for r in range(9):
                for c in range(9):
                    if (r // 3) * 3 + (c // 3) != b: #if not in the curr box we in
                        continue
                    curr = board[r][c]
                    if curr == ".":
                        continue 
                    elif curr in seen_b:
                        return False
                    else:
                        seen_b.add(curr)

        return True #no dupes raised anything 



