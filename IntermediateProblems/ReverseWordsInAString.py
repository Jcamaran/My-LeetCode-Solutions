class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        reversed = " ".join(words)
        return reversed
    

            
