# 1456. Maximum number of vowel in a Substring of given length 
# Given a string s and an integer k, 
# return the maximum number of vowel letters in any substring of s with length k.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Create a list of vowel
        # Initially create a window of length k
        # Using this window slide over to next characters.

        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        for i in range(k, n):
            if s[i] in vowels:
                count+=1

            if s[i-k] in vowels:
                count-=1

            max_count = max(max_count, count)
        return max_count
    
s = Solution()
print(s.maxVowels("abciiidef", 3))