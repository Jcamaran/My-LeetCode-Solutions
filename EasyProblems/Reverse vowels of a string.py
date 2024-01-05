class Solution(object):
    def reverseVowels(self, s):
        #setting the counter from the left#
        i = 0 
        #setting counter from the right#
        j = len(s) - 1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
            elif s[i] in vowels and s[j] not in vowels:
                j -= 1
            
            elif s[i] not in vowels and s[j]  in vowels:
                i += 1
            
            else:
                j -= 1
                i += 1
        x = "".join(s)
        return x

            





        
