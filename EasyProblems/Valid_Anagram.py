class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        j = sorted(s)
        c = sorted(t)
        if c != j:
            return False
        else:
            return True
            

