# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        anagram_dict = defaultdict(list)    # SC -> n: Number of words
        # In parenthesis we give the default value,
        # which is used to initalize the key.

        for s in strs:  # TC => N
            count = [0] * 26   # TC => 1
            for c in s:  # TC => k : maximum size of each word
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)

            # Why use defalutdict?
                ## Lets say the key do not already exist in the dict, 
                ## so the defaultdict intializes the key with a empty list here
            anagram_dict[key].append(s)

        return list(anagram_dict.values())

        # TC => O(n * k)
        # SC => O(n * k) -> Total number of chracters
        # This gives us a space complexity of O(N∗K) just to store all the characters in the values.


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
