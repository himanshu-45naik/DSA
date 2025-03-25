class Solution:
    def get(self, a, b):
        
        # Approach
        # Use XOR operator such that 10 ^ 10 = 0
        # Using this logic, swap a and b
        a = a ^ b 
        b = a ^ b
        a = a ^ b
        
        return a, b
