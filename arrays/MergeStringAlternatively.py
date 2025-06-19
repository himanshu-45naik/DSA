# 1768. Merge Strings Alternatively

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Here combine both the given strings such that the resultant string has 
        alternate characters of word1 and word2.

        Args:
            word1 (str): String to be combined with word2.
            word2 (str): String to be combined with word1.

        Returns:
            str: Return string which has alternate character from word1 and word2.
        """
        
        # Check which string is larger.
        # Using a while loop which runs for n1+n2 times i.e total length of both strings.
        # If the index of resultant string is even then we put the character of word1
        # Else (i.e if odd index) we put character of word2.
        # If word1 is larger then we add all remaining characters of word1 in the result after the chracters of word2 are exhausted.
        # Same logic if word2 is larger.
        # Return the result.
        
        checker = 0
        result = ""

        n1 = len(word1)
        n2 = len(word2)

        if n1 > n2:
            max_len = n1
        else:
            max_len = n2

        i = 0 # Index of word1
        j = 0 # Index of word2

        counter = 0
        while counter <= n1+n2:
            if checker % 2 == 0 and i < n1:
                result+= word1[i]
                i+=1
            elif j < n2:
                result+=word2[j]
                j+=1
            elif i < n1 and max_len == n1 and j >= n2 :
                result+= word1[i]
                i+=1
            elif j < n2 and max_len == n2 and i >= n1:
                result+= word2[j]
                j+=1
            
            counter+=1
            checker+=1
        return result