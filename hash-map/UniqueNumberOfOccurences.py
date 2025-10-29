# 1207. Unique Number of Occurrences.

# Given an array of integers arr, 
# return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        # Create a dictionary such that 
            ## element:count pair is represented in the dict
            ## If the values is same with any of the other elements
            ## Return False
            ## Otherwise false

        hash_map = {}

        for i in range(len(arr)):
            if arr[i] in hash_map.keys():
                hash_map[arr[i]] += 1
            else:
                hash_map[arr[i]] = 1

        j = 0
        occur = list(hash_map.values())

        while j < len(hash_map):
            for i in range(j+1, len(hash_map)):
                if occur[j] == occur[i]:
                    return False
            j+=1

        return True        

s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))