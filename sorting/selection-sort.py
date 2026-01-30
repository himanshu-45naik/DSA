class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        # In first iteration find the smallest element and swap it with the first element 
        # Now the first element is sorted
        # now start the iteration from 2nd element -> find the shortest element in this sublist
        # Swap the smallest element with th 2nd index
        # Continue this untill the last element

        n = len(nums)

        for i in range(n):
            min_idx = i
            for k in range(i + 1, n):
                if nums[k] < nums[min_idx]:
                    min_idx = k

            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return nums

s = Solution()
print(s.sortArray([5, 6, 1, 3]))
