class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerb = 1
        upperb = max(piles)
        k=1
        while lowerb <= upperb:
            mid = (lowerb + upperb) // 2
            hours = sum((p + mid - 1) // mid for p in piles)

            if hours <= h:
                res = mid 
                upperb = mid -1
            else:
                lowerb = mid +1
        return res 