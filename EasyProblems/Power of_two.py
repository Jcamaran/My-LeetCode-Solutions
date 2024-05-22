import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            check = math.log2(n)
            return check == int(check)
        else:
            return False
