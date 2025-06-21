# 305. Reverse vowel of the String

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        n = len(s)
        result = [ch for ch in s]
        isVowel = []
        vowels = []
        for i in range(0, n):
            if s[i] in "aeiouAEIOU":
                isVowel.append(True)
                vowels.append(s[i])
            else:
                isVowel.append(False)

        reversed = vowels[::-1]
        j = 0
        
        for i in range(0, n):
            if isVowel[i] == True:
                result[i] = reversed[j] 
                j+=1
        return "".join(result)
    
s = Solution()
print(s.reverseVowels("IceCreAm"))
print(s.reverseVowels("Euston saw I was not Sue."))
print(s.reverseVowels("race car"))
