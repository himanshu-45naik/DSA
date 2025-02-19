from typing import List

class Solution:
    def CombinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stk = []
        candidates.sort()  # Crucial: Sort the candidates for skipping duplicates

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(stk[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                stk.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])  # Use i+1 to avoid reusing the same element
                stk.pop()

        backtrack(0, target)
        return res


s = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
print(s.CombinationSum2(candidates, 8))








# We need to find all unique combinations of numbers from the candidates list that sum up to the target. The rules are:

#     Numbers can only be used once in a particular combination. This means we can't re-use the number at the same index more than once. For example, if candidates = [2, 3, 6, 7] and target = 7, the combination [7] is valid, but [3, 3] is NOT (even if 3 appeared twice in candidates at different indexes), and neither is [6, 6].

#     We must avoid duplicate combinations, which means combinations that contain the same numbers, regardless of the order. [2, 6] and [6, 2] are considered the same combination.

# How the Code Solves the Problem (Revised Explanation)

# The code uses backtracking, and here's how it ensures both constraints are met:

#     start Index: The backtrack(start, remaining) function is the heart of the solution. The start parameter is crucial for ensuring we don't reuse the same element at the same index in the candidates list.

#     The for Loop: The for i in range(start, len(candidates)): loop controls which elements are considered at each level of the recursion. start specifies the starting index for the loop.

#     The Recursive Call: The key line is backtrack(i + 1, remaining - candidates[i]). Notice that the recursive call passes i + 1 as the new start value. This is critical!

#         Preventing Re-use of Same Index: By passing i + 1, we guarantee that in the next recursive call, the loop will start from the next element in the candidates list. The element at index i will never be considered again in the current branch of the recursion. This enforces the rule that we can only use each number at each index once in the given combiantion

#     Duplicate Combination Prevention (with Sorting): As explained before, if i > start and candidates[i] == candidates[i - 1]: continue is necessary in addition to i+1 in the backtrack call to avoid duplicate combinations.

# Example Trace

# Let candidates = [2, 3, 6, 7] and target = 7.

#     backtrack(0, 7):

#         i = 0: candidates[0] = 2. We add 2 to stk. Call backtrack(1, 5).

#     backtrack(1, 5):

#         i = 1: candidates[1] = 3. We add 3 to stk. Call backtrack(2, 2).

#     backtrack(2, 2):

#         i = 2: candidates[2] = 6. We add 6 to stk. Call backtrack(3, -4). remaining < 0, so backtrack.

#         i = 3: candidates[3] = 7. We add 7 to stk. Call backtrack(4, -5). remaining < 0, so backtrack.

#         Remove 7 from stk.

#         Remove 6 from stk.

#     Continue backtrack(1,5)
#     -i=2: candidates[2] = 6. We add 6 to stk. Call backtrack(3, -1)
#     -Remove 6 from stk.

#     Continue backtrack(0,7)

#         i = 3: candidates[3] = 7. We add 7 to stk. Call backtrack(4, 0). remaining == 0, so add [7] to res.