# 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# "ace" is a subsequence of "abcde" while "aec" is not.

class Solution():
    def isSubseqence(self, s: str, t: str) -> bool:

        # How to take care of the sequence ?
            ## 

        last_index = 0
        j = 0

        if not s:
            return True
        
        for i in range(len(t)):
            if j < len(s) and s[j] not in t:
                return False
            
            if s[j] == t[i]:
                if last_index >= i:
                    return False
                else:
                    last_index = i
                    j += 1

        return True

s = Solution()
print(s.isSubseqence("abc", "ahbgdc"))
# print(s.isSubseqence("axc", "ahbgdc"))