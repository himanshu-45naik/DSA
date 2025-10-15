## Key Characteristics of Backtracking:

1. Recursive Approach: Backtracking is often implemented using recursion, as it naturally handles the nested exploration of choices.       
2. Incremental Construction: Solutions are built step by step, with each step involving a choice.
3. Exploration of Choices: The algorithm explores all possible choices at each step.  
4. Pruning (Bounding): If a partial solution is found to be invalid, the algorithm prunes the search space by abandoning that path. This is a crucial optimization for efficiency.
5. Systematic Search: Backtracking ensures that all possible solutions are explored.  
6. State Management: The algorithm needs to maintain the current state of the solution being built, so it can backtrack to previous states.



## Combination Sum 1
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        stack = []

        def backtrack(start, curr_sum):
            if curr_sum == target:
                res.append(stack[:])  # Append a copy of the current stack
                return
            if curr_sum > target:
                return

            for i in range(start, len(candidates)):
                stack.append(candidates[i])
                backtrack(i, curr_sum + candidates[i])  # Allow the same element to be reused
                stack.pop()  # Backtrack by removing the last added element

        backtrack(0, 0)
        return res
```
- This code produces all possible answers with repitition of candidates[i]

-------------------------------------------------------------------------------------------------

## Combination sum 2

### What does return actually do?
```python
def backtrack(start,sum):
    if sum == target:
        res.append(stk[:])
        return
    if sum > target:
        return
```
- return is used to terminate the current recursive call, effectively **pruning this branch of the search tree**. This optimization is essential for efficiency, as it avoids exploring paths that are guaranteed to fail
  
----------------------------------------------------------------------------------------------------------------------------------------

### How does the variable sum reset after a search tree is pruned? (as no explicit [sum = 0 or to previous sum] code is written)
- In a backtracking algorithm, especially when implemented recursively, the "reset" of variables like sum after pruning is handled implicitly by the function's call stack. Here's a breakdown of how it works:

##### Understanding the Call Stack

- When a recursive function like backtrack is called, a new "frame" is pushed onto the call stack. This frame contains:
    - The function's local variables (like sum).
    - The function's parameters (like start).
    - The return address (where the function should return to).
    When a return statement is encountered, the current frame is popped off the stack, and the function execution resumes at the return address in the previous frame.

#### How to avoid duplicates?
- Sorting: candidates.sort() is now present at the beginning of the CombinationSum2 function. This is absolutely crucial for handling duplicates correctly. Without sorting, you can't reliably skip duplicates in the same level of the recursion.

- Duplicate Skipping: The core logic to prevent duplicate combinations is the if i > start and candidates[i] == candidates[i - 1]: continue line inside the for loop of the backtrack function. This condition checks:

    - i > start: Ensures that we are not at the very first element in the loop (for a given recursion level). We only want to skip duplicates after the first occurrence of a number.

    - candidates[i] == candidates[i - 1]: Checks if the current number is the same as the previous number in the sorted candidates list. If both conditions are true, it means we've already considered this number in the previous iteration of the loop **at the same level of the recursion**, so we skip it to avoid duplicate combinations.