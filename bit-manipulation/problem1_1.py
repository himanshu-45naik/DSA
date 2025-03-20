# Checking the K-th Bit using Bitwise Operators

# Note --> Bitwise shift operators (<< for left shift and >> for right shift) work directly on decimal (integer) numbers,
# because integers are stored in binary format at the hardware level.

class Solution:
    
    ''' n : int
        k : int
        Return Type : Boolean '''
    def checkKthBit(self, n, k):
        # We can perform this using shift operator
        
        # RIght shift -->
            # Right shift the number n by k places
            # This brings the K-th bit to the rightmost (0-th) position.
            # Perform bitwise with & with 1
            # If result is 1 than True other wise False.
            # Example --
            # n= 13, k = 2
            # 1. Right shift 13 by 2 --> 1101>>2 = 0011
            # 2. Perform & operator of 0011 and 0001(1) --> 0011 & 0001 = 100(1)
        
        # Left shift operator
            # Create a bitmask by left-shifting 1 by k places.
            # Perform bitwise AND (&) between n and the bitmask
            # If result is 1 than True otherwise False.
            # Example --
            # n= 13 , k = 2
            # 1. Create bit-mask by leftshifing 1 by k (1<<2).-->   0001<<2 = 0100 
            # 2. Perform and between bit mask and n.--> 0100 & 1101(13) = 0100(1)
        
        
        '''
        Right shift --
        return (n>>k)&1 == 1
        '''
        
        return (n&(1<<k)) != 0
    
    
s = Solution()
print(s.checkKthBit(n=4, k=0))
print(s.checkKthBit(n=500, k=3))
print(s.checkKthBit(n=4, k=2))