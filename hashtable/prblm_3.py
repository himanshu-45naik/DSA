#  Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Approach
        # Use sliding window for subarrays
        # First initialize the window such that the window ends before a duplicate value. =
        # In a for loop, keep adding one character and removing the first charachter such that we increment the window.
        # We will keep increasing the length of window till there is no duplicate value. --> So the length of window is no constant
        # Keep storing the length of window just to compare with the longest window length already stored. 
        
        window = []
        n = len(s)
        longest_length = 0 
        left = 0  
        
        for right in range(n):
            while s[right] in window:
                window.pop(0) 
            
            window.append(s[right])
            longest_length = max(longest_length, len(window))  
        
        return longest_length
    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))