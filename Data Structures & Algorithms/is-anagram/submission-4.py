class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s)
        y = sorted(t)

        if len(x) != len(y):
            return False 
        
        for i,v in enumerate(y): 
            if v != x[i]:
                return False
        return True 

