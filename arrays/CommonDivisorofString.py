# 1071. Greatest common divisor of Srings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Find a common divisor for both the stings.

        Args:
            str1 (str): Input string
            str2 (str): Input string

        Returns:
            str: The common divisor for both strings.
        """
        
        # Get GCD of lengths
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        # If they don’t concatenate to the same result, there’s no common base
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_len = gcd(len(str1), len(str2))
        
        # Return the prefix of length gcd_len from either string
        return str1[:gcd_len]