class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Assume first element to be sorted
        # thus we have two portions - sorted and unsorted portions
        # Start iteration from second element, compare it with the sorted portion, if its smaller then the element in sorted portion than insert it before it.
        # Continue this -> such that the comparison in sorted portion starts from the back
        n = len(nums)
        
        for i in range(1, n):
            
            key = nums[i]
            j = i - 1

            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums 


s = Solution()
print(s.sortArray([5, 6, 1, 3]))