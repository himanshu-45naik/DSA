# 151. Reverse words in a string

class Solution:
    def reverseWords(self, s: str) -> str:
        """A string of sentence is given, reverse the sentence.
        If there is leading and trailing space remove it.

        Args:
            s (str): A sentance which has to be reversed.

        Returns:
            str: The reversed sentance.
        """
        
        # Remove the trailing and leading spaces.
        s = s.strip()
        
        # Create a list consisting of words of a sentance.
        ls = []
        n = len(s)
        i = 0
        word = ""
        
        while i < n:
            if s[i].isalnum() and i != n-1:
                word+=s[i]
            elif i == n-1:
                word+=s[i]
                ls.append(word)
            elif word != "":
                ls.append(word)
                word = ""
            i+=1
        
        # Reverse the list of words.
        reversed = ls[::-1]
        result = ""
        
        # Again convert the reversed list of words to a sentence.
        for i in range(0, len(ls)):
            if i != len(ls) - 1:
                result = result + reversed[i] + " "
            else:
                result = result + reversed[i]
        
        # Return the reversed list
        return result
        
s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))
