class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        res = []
        
        def backtrack(rem, start, stk, count):
            if rem == 0 and count == k:  # Changed condition
                res.append(stk[:])
                return
            if count == k or rem < 0 or start > 9:  # Added bound check
                return
                
            for i in range(start, 10):  # Changed to iterative approach
                stk.append(i)
                backtrack(rem - i, i + 1, stk, count + 1)
                stk.pop()
        
        backtrack(n, 1, [], 0)
        return res
    
s = Solution()
k = 3
n = 7
print(s.combinationSum3(k,n))