# Subarrays

## Brute approach
- The first subarray starts at index `0`, the next one at `1`, and so on.
- The last valid subarray starts at index `N−k`.
- Thus, the total number of subarrays of size k is `N−k+1`.


## Sliding Window
- Instead of recomputing from scratch, remove the leftmost element and add the next rightmost element.
- This avoids redundant operations, reducing time complexity from `O(N × k)` (brute force) to `O(N)` (optimized approach).
```
A=[1,2,3,4,5]

For k = 3, the subarrays are:

    [1, 2, 3] → First window
    [2, 3, 4] → Remove 1, add 4
    [3, 4, 5] → Remove 2, add 5
```