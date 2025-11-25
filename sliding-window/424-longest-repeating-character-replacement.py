# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_ch = s[0]
        max_freq = 0
        max_len = 0

        hash = [0] * 26

        l = 0
        for r in range(len(s)):
            hash[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, hash[ord(s[r]) - ord('A')])
                
            if (r - l + 1) - max_freq > k:
                hash[ord(s[l]) - ord('A')] -= 1

                max_freq = 0
                l += 1
            
            
            max_len = max(max_len, r - l + 1)

            
        return max_len

        
        
s = Solution()
print(s.characterReplacement("AABABBA", 1))