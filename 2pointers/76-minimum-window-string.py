# 76. Minimum Window String
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # This is a brute force approach
        # In this approach we will find the all possible windows using 2 pointer approach
        # s = "ADOBECODEBANC" t = "ABC" 
        # Now here the edge case is that even if there is duplicates in t we will have to consider that in s.
        # Thus we will use a hashtable which stores the frequency of each character in the t string
        # Logic:
        # In the hash we will decrease the frequency once that char of t is found
        # This will help us with edge case too i.e duplicates
        # We will also track the count, once the count is equal to size of t, it means all the characters of t are found.
        # Save the start index and size of the window.
        
        max_len = 10 ** 9
        s_ind = -1

        m = len(s)
        n = len(t)

        for i in range(m):
            hash = [0] * 256
            cnt = 0

            for ch in t:
                hash[ord(ch)] += 1
            
            for j in range(i, m):
                if hash[ord(s[j])] > 0:
                    cnt+=1
                    hash[ord(s[j])] -= 1
                if cnt == n:
                    if j - i + 1 < max_len:
                        max_len = j - i + 1
                        s_ind = i
                        break
        
        if s_ind == -1:
            return ""
        return s[s_ind: s_ind+max_len]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
