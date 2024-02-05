class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        sorted_R = "".join(sorted(ransomNote))
        sorted_M = "".join(sorted(magazine))
        for i in sorted_R:
            if sorted_M.count(i) < sorted_R.count(i):
                return False
        return True
