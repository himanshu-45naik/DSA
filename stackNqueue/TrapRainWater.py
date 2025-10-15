# 42.  Trap Rainwater


class Solution:
    def trap(self, height: list[int]) -> int:
        """We are given non-negative integers which represent elevations.
        We have to find how many space of height 1 can store rain water.
        If in a space if the water stored is of height 2 units than increase count by 2.

        Args:
            height (List[int]): The list of integers representing elevations.

        Returns:
            int: Number of total spaces that store rain water.
        """

        # Approach
        # Water will be stored only when there is larger size integers on either side.
        # min(leftmax, Rightmax) - arr[i]
        #
        n = len(height)
        if n == 0:
            return 0

        prefixmax = [0] * n
        suffixmax = [0] * n

        prefixmax[0] = height[0]
        for i in range(1, n):
            prefixmax[i] = max(prefixmax[i - 1], height[i])

        suffixmax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suffixmax[i] = max(suffixmax[i + 1], height[i])

        total = 0
        for i in range(1, n - 1):
            water = min(prefixmax[i], suffixmax[i]) - height[i]
            if water > 0:
                total += water

        return total


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
