# Checking the K-th Bit using Bitwise Operators

class Solution:
    
    ''' n : int
        k : int
        Return Type : Boolean '''
    def checkKthBit(self, n, k):
        # Your code here
        # Decimal number to Binary number -- keep Dividing the decimal by 2 
        # till remainder is less than the number
        # Store the remainders such that the final binary number is reversed
        # Here there is no need to reverse, as we want to from check LSB(Least significant binary).
        
        result = []
        
        while n > 0:
            remainder = n % 2
            n = n // 2
            result.append(remainder)
            
        if n == 1:
            result.append(1)
        
        
        
        if k < 0 or k >= len(result):
            return None
            
        return result[k] == 1
    
s = Solution()
print(s.checkKthBit(n=4, k=0))
print(s.checkKthBit(n=500, k=3))
print(s.checkKthBit(n=4, k=2))