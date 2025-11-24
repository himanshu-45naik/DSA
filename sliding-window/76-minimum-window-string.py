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

       # ----------------------------Brute Force Approach---------------------------- 
        # max_len = 10 ** 9
        # s_ind = -1

        # m = len(s)
        # n = len(t)

        # for i in range(m):
        #     hash = [0] * 256
        #     cnt = 0

        #     for ch in t:
        #         hash[ord(ch)] += 1
            
        #     for j in range(i, m):
        #         if hash[ord(s[j])] > 0:
        #             cnt+=1
        #             hash[ord(s[j])] -= 1
        #         if cnt == n:
        #             if j - i + 1 < max_len:
        #                 max_len = j - i + 1
        #                 s_ind = i
        #                 break
        
        # if s_ind == -1:
        #     return ""
        # return s[s_ind: s_ind+max_len]

# -----------------------------------------------Optimal Solution------------------------------------
        # Sliding window Solution

            
        # 1. Pointers:
        #    - right: EXPANDS the window (moves forward to find a valid substring).
        #    - left:  SHRINKS the window (moves forward to minimize the valid substring).

        # 2. Key Variables:
        #    - hash[]: Stores frequency of characters in 't'.
        #              * Positive (> 0): We strictly NEED this character.
        #              * Zero (0): We have exactly enough.
        #              * Negative (< 0): We have EXTRA (surplus) of this character in the window.
        #    - cnt:    Tracks how many required characters we have currently "matched".
        #    - min_len & s_start: To store the smallest valid window found so far.

        # 3. Initialization:
        #    - Pre-fill 'hash' with frequencies of 't'.
        #    - l = 0, r = 0, cnt = 0.

        # ------------------------------------------------------------------
        # PHASE 1: EXPANSION (The 'for' loop using 'r')
        # ------------------------------------------------------------------
        # - We assume every character 's[r]' contributes to the window.
        # - Always DECREMENT hash[s[r]] first (to record we found it).
        # - CRITICAL CHECK:
        #   Did we actually *need* this character?
        #   If hash[s[r]] >= 0 (after decrementing, or check > 0 before):
        #       It means we haven't exhausted the requirement yet.
        #       -> cnt += 1
        #   (If hash was negative, it means it's an extra duplicate, so don't increase cnt).

        # ------------------------------------------------------------------
        # PHASE 2: CONTRACTION (The 'while' loop using 'l')
        # ------------------------------------------------------------------
        # - Condition: Run while (cnt == len(t)). This means the current window is VALID.
        # - Step A: Update Answer.
        #           Check if (r - l + 1) is smaller than 'min_len'. Update 's_start' and 'min_len'.
        # - Step B: Remove s[l].
        #           We are tossing s[l] out, so we must INCREMENT hash[s[l]].
        # - CRITICAL CHECK:
        #   Did removing this character break our validity?
        #   If hash[s[l]] > 0 (after incrementing):
        #       It means we are now "in debt" (we need that character back).
        #       -> cnt -= 1 (This will break the while loop).
        #   (If hash is <= 0, it means we had extras, so the window is still valid without it).
        # - Step C: l += 1

        # ------------------------------------------------------------------
        # DRY RUN EXAMPLE:
        # s = "A A B C", t = "A B C" (Target length = 3)
        # Initial Hash: {A: 1, B: 1, C: 1}
        # ------------------------------------------------------------------

        # i = 0, Char 'A':
        #   - Hash['A'] becomes 0.
        #   - Is 0 >= 0? Yes. It was needed.
        #   - cnt becomes 1.
        #   - Window: "A" (Not valid)

        # i = 1, Char 'A' (The Duplicate):
        #   - Hash['A'] becomes -1. (Negative means "Surplus")
        #   - Is -1 >= 0? No. We didn't need this specific copy to reach the target count.
        #   - cnt stays 1.
        #   - Window: "A A" (Not valid)

        # i = 2, Char 'B':
        #   - Hash['B'] becomes 0.
        #   - cnt becomes 2.
        #   - Window: "A A B" (Not valid)

        # i = 3, Char 'C':
        #   - Hash['C'] becomes 0.
        #   - cnt becomes 3. -> VALID! (cnt == len(t))
        #   - Window: "A A B C" (Length 4). Update min_len = 4.

        #   --- Shrinking Phase (while cnt == 3) ---
        #   1. Remove s[l] (First 'A'):
        #      - Hash['A'] goes from -1 -> 0.
        #      - Is Hash['A'] > 0? No. (0 means we still have exactly enough).
        #      - cnt stays 3. (Loop continues).
        #      - l moves to 1.
        #      - New Window: "A B C" (Length 3). Update min_len = 3.

        #   2. Remove s[l] (Second 'A'):
        #      - Hash['A'] goes from 0 -> 1.
        #      - Is Hash['A'] > 0? Yes! We are now missing a required 'A'.
        #      - cnt drops to 2.
        #      - Loop breaks.

        cnt = 0
        s_ind = -1
        max_len = 10 ** 9

        m = len(s)
        n = len(t)

        hash = [0] * 256
        for ch in t:
            hash[ord(ch)] += 1

        l = 0

        for r in range(m):
            
            if hash[ord(s[r])] > 0:
                if s[r] in t:
                    cnt += 1  
            hash[ord(s[r])] -= 1
            
            while cnt == n:
                if cnt == n:
                    if r - l + 1 < max_len:
                        max_len = r - l + 1
                        s_ind = l  

                # Removing the charachter from the window(sliding the window by shringking)
                hash[ord(s[l])] += 1  # Increase the frequency of that character which now will be removed from the window.

                if hash[ord(s[l])] > 0:  # We will decrease the cnt only if the frequency is more than 0, beucase this char is already found.
                    cnt -= 1

                l += 1

        if s_ind == -1:
            return ""
        return s[s_ind: s_ind+max_len] 

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ddaaabbca", "abc"))
