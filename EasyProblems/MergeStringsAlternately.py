class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        l1 = len(word1)
        l2 = len(word2)
        n = min(l1,l2)
        for i in range(n):
            result += word1[i] + word2[i]
        if l1 == l2:
            return result
        elif l1 > l2:
            return result + word1[n:]
        else:
            return result + word2[n:] 
        return result
