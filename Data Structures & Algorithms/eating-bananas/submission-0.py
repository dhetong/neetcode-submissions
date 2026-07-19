class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate_max = max(piles)
        rate_min = 1
        while rate_min < rate_max:
            point = rate_min + (rate_max-rate_min)//2
            time = sum([(pile+(point-1))//point for pile in piles])
            if time > h:
                rate_min = point + 1
            else:
                rate_max = point
        return rate_min     