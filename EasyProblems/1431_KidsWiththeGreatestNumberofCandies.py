class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        x = max(candies)
        for i in candies:
            result.append(i + extraCandies >= x)
        return result
