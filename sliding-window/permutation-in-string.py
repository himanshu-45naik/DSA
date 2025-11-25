# 567. Permutation in string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Check edge case: if s1 is longer than s2, an inclusion is impossible
        if len(s1) > len(s2):
            return False

        hash_s1 = [0] * 26
        hash_s2 = [0] * 26

        for i in range(len(s1)):
            hash_s1[ord(s1[i]) - ord('a')] += 1

        # Initialize a window of size len(s1)
        for j in range(len(s1)):
            hash_s2[ord(s2[j]) - ord('a')] += 1

        # Sliding window
        for k in range(len(s1), len(s2)):
            if hash_s1 == hash_s2:
                return True

            # Slide the right edge
            hash_s2[ord(s2[k]) - ord('a')] += 1

            # Remove the left edge
            hash_s2[ord(s2[k - len(s1)]) - ord('a')] -= 1

        return hash_s1 == hash_s2 

s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
print(s.checkInclusion("ab", "eidboao"))