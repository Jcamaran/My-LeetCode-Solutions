# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l,j = 1,n
        while True:
            mid = (l+j) // 2
            result = guess(mid)
            if result > 0:
                l = mid + 1
            elif result < 0:
                j = mid -1  
            else:
                return mid
