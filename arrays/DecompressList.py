# 1313. Decompress Run-lenght Encoded List

# [freq, val] = [nums[2*i], nums[2*i+1]] => freq is the frequency of the value(val) in the decompressed list.
# Output -> Concatenate all the sublists from left to right to generate the decompressed list.

class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:

        # Append the value in the list for the given frequency.
        # Use the formula for efficiency -> [nums[2*i], nums[2*i+1]]


        n = len(nums)
        result = []

        for i in range(0, n // 2):
            val = nums[2 * i +1]
            freq = nums[2 * i]

            result = result + [val] * freq

        return result

s = Solution()
print(s.decompressRLElist([1,2,3,4]))
print(s.decompressRLElist([1,1,2,3]))