class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        
        while L < R:
            mid = (L+R)//2
            this_h = 0
            for p in piles:
                this_h += math.ceil(p/mid)
            if this_h > h:
                L = mid + 1
            else:
                R = mid
        return R