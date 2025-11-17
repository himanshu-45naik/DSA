# 3. Longest Substring Without Repeating Characters.

# Given a string s, find the length of the longest without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We have to find the length of longest substring which has no repeating characters
        # How can we do this?
            ## We can use a sliding window
            ## Initially create an empty window.
            ## Then slide the window, such that there is no repetitions.
            ## When you come across a repetition then just move the window.
        # How do we move the window?
            ## Parse the string and add each chracter in the window till there is no repition.
            ## When there is repetition, we will use a while loop and keep removing first element till there is no repetition.

        n = len(s)
        window = []
        max_len = 0

        for right in range(n):
            while s[right] in window:
                window.pop(0)
            
            window.append(s[right])
            max_len = max(max_len, len(window))

        return max_len
    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
        