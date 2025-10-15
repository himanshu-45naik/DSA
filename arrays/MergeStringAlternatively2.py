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
        # Define an empty list.
        # Using for loop ranging from 0 to maxlength.
        # First append the charachter of word1 to the list.
        # Then append the charachter of word2 in the list.
        # In this way even if one string is larger, rest of the chrachters of larger string will get appended.
        # Join the elements of the list to form a result string.
        # Return the result.
        
        result = []
        n1 = len(word1)
        n2 = len(word2)
        
        if n1 > n2:
            max_len = n1
        else:
            max_len = n2
            
        for i in range(0, max_len):
            if i < n1:
                result.append(word1[i])
            
            if i < n2:
                result.append(word2[i])
                
        return "".join(result)