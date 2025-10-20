# 1679. Max Number of k-Sum Pairs
# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array. 
# Return the maximum number of operations you can perform on the array.


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:

        # Bruteforce
        # Check each element with the other elements in the array.
        # Remove those which are equal to k.
        # Keep track of the remove operation.        

        # n = len(nums)
        # used = [False] * n  # track if an element is already used
        # count = 0

        # for i in range(n):
        #     if used[i]:
        #         continue
        #     for j in range(i + 1, n):
        #         if used[j]:
        #             continue
        #         if nums[i] + nums[j] == k:
        #             count += 1
        #             used[i] = used[j] = True  # mark both as used
        #             break  # move to next i once a valid pair is found

        # return count

        # Optimized solution

        nums.sort()
        n = len(nums)
        l = 0
        r = n-1
        sum = 0
        used = [False] * n
        count = 0

        while l < r:
            if used[l]:
                l +=1
            if used[r]:
                r-=1

            sum = nums[l] + nums[r]

            if sum == k:
                used[l] = True
                used[r] = True
                count +=1
                l+=1
                r-=1
            elif sum < k:
                l+=1
            else:
                r-=1

        return count

    
s = Solution()
print(s.maxOperations([1,2,3,4], 5))
print(s.maxOperations([3,1,3,4,3],6))
