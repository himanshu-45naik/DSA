# Increasing Array

# Array of n integers is given
# Sort those numbers in increasing order

# We have to sort the numbers in increasing order
# If the number is arr[i] <= arr[i+1] then its fine
# Otherwise if its not, we will have to add 1 no. number at a time to increase the element
# Thus satisfying arr[i] <= arr[i+1]
class Solution:
    def increasing_array(self, size, array_of_number):
        count = 0
        for i in range(1, size):
            if array_of_number[i-1] > array_of_number[i]:
                count += array_of_number[i-1] - array_of_number[i]
                array_of_number[i] = array_of_number[i - 1]

        return count

s = Solution()
size = int(input())
arr = input()
arr = list(map(int, arr.split()))


print(s.increasing_array(size, arr))
