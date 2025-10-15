# Wierd algorithm


class Solution:
    def wierd_algorithm(self, n: int)-> None:
        """Consider an algorithm that takes as input a positive integer n.
        If n is even -> divide it by 2.
        If n is odd -> multiply it by 3 and add 1.
        Repeat this until n is 1.
        

        Args:
            n (int): The input number.

        Returns:
            int: Print a line that contains all values of n during the algorithm.
        """
        
        while n > 1:
            print(n, end=" ")
            
            if (n % 2 == 0):
                n = n//2
            else:
                n = (n * 3) + 1
        print(1)

s = Solution()
n = int(input())
s.wierd_algorithm(n)
        
            
            