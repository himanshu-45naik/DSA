# 438. Find all anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        
        if len(s) < len(p):
            return []

        hash_p = [0] * 26
        hash_s = [0] * 26

        for i in range(len(p)):
            hash_p[ord(p[i]) - ord('a')] += 1
        
        # Initialize the window
        for j in range(len(p)):
            hash_s[ord(s[j]) - ord('a')] += 1
        
        res = []
        if (hash_p == hash_s):
                res.append(0)

        # Sliding window
        for k in range(len(p), len(s)):

            # Move the window
            hash_s[ord(s[k]) - ord('a')] += 1

            # Remove the left edge
            hash_s[ord(s[k - len(p)]) - ord('a')] -= 1

            if (hash_p == hash_s):
                res.append(k - len(p) + 1)

        return res
                
s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))