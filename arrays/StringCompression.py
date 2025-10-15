# 443. String Compression

# Given an array of characters chars, compress it using the following algorithm:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.

class Solution:
    def compress(self, chars: list[str]) -> int:
        
        # We have to return the lenght of output list
        # The output list is such that -> 
            # Input is [a,a,a,b,b,b,c]
            # Output is [a,3,b,2,c] -> If the count of an alphabet is one than place it as it is.

        result = {}
        output = 0

        for element in chars:
            if element in result:
                result[element]+=1
            else:
                result[element] = 1

        for cnt in result.values():
            if cnt == 1:
                output+=1
            elif cnt > 9:
                output+=3
            else:
                output+=2
        return output

s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a"]))
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))