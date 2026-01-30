class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # At each iteration, compare 2 adjacent elements and swap them if they are not sorted
        n = len(nums)
        swapped = False

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True

            if not swapped:
                break
        return nums

s = Solution()
print(s.sortArray([5, 6, 1, 3]))