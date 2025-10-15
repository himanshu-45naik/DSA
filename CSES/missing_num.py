## Missing number

class Solution:
    def missing_num(self, n: int, num: str)-> int:
        """Num has numbers from 1 to n
            The input has one missinf number.
            Find the missing number.
        
        n (int): The total numbers.
        num(str): Numbers of size n-1, as it has one missing number. 
        """
        nums = list(map(int, num.split()))
        nums.sort()
        nums_sum = sum(nums)
        actual_sum = (n*(n+1)) // 2        
        result = actual_sum - nums_sum
        return result
        
           
s = Solution()
n = int(input())
num = str(input())
print(s.missing_num(n, num))