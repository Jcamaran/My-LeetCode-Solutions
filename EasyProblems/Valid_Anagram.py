class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we know sorted function alphabetically orders lettrers as well as numbers, so we can just remove the first check which makes it run slower
        s = sorted(s)
        t = sorted(t)
        
        return s == t

        
