# 383. Ransom Note
# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequency of each character in magazine
        magazine_count = {}

        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1

        # Check if ransomNote can be formed
        for char in ransomNote:
            if char not in magazine_count or magazine_count[char] == 0:
                return False
            magazine_count[char] -= 1  # use one character

        return True


s = Solution()
print(s.canConstruct("a", "b"))     
print(s.canConstruct("aa", "ab"))    
print(s.canConstruct("aa", "aab"))   
