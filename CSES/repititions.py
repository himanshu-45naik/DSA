class Solution:
    def repititions(self,dnaSequence: str)-> int:
        """A DNA sequence is given consisting of characters A,C,G,T.
        Return the length of longest repitition in the sequence.

        Args:
            dnaSequence (str): The string containing DNA sequence.

        Returns:
            int: The length of largest substring which has repitition of a sequence.
        """
        
        # Approach
        # First we will intialize a variable with string[0].
        # We will use a for loop such that we remove one left character and add a new right character at each iteration.
        # And simultaneously update the length of largest substring.
        
        
        if not dnaSequence:
            return 0
        
        maxi = 1
        max_string = maxi
        
        for i in range(1,len(dnaSequence)):
            if dnaSequence[i] == dnaSequence[i-1]:
                maxi+=1
                max_string = max(maxi, max_string)
            else:
                maxi = 1
                
                
        return max_string
    
s = Solution()
dnaSequence = input()
print(s.repititions(dnaSequence))