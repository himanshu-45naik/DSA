# 443. String Compression

# Given an array of characters chars, compress it using the following algorithm:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.

class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        cnt = 1
        j = 0

        for i in range(n - 1):
            if chars[i] == chars[i + 1]:
                cnt += 1
            else:
                chars[j] = chars[i]
                j += 1

                if cnt > 1:  
                    for ch in str(cnt):  
                        chars[j] = ch
                        j += 1

                cnt = 1  

    
        chars[j] = chars[-1]
        j += 1
        if cnt > 1:
            for ch in str(cnt):
                chars[j] = ch
                j += 1

        while len(chars) > j:
            chars.pop()

        print(chars)
        return j



    
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a"]))
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))