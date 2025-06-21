# 305. Reverse vowel of the String

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)  # Convert to list for in-place swapping
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        return "".join(s)

s = Solution()
print(s.reverseVowels("IceCreAm"))
print(s.reverseVowels("Euston saw I was not Sue."))
print(s.reverseVowels("race car"))
