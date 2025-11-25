# 1626. Sort Array with increasing freqency

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        
        freq = {}
        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        freq_sorted = sorted(freq.items(), key= lambda x: x[0], reverse=True)
        freq_sorted = sorted(freq_sorted, key= lambda x: x[1])

        res = []
        for  i in freq_sorted:
            key, val = i
            for j in range(val):
                res.append(key)
        
        return res

s = Solution()
print(s.frequencySort([1,1,2,2,2,3]))
print(s.frequencySort([-1,1,-6,4,5,-6,1,4,1]))