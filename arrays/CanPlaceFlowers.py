# 605. Can place flowers 

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """ A list of flowerbed is given, if flowerbed[i] = 1 - flower is present
        Else not present. In this flowerbed, no adjacent flower can be present.
        An integer n is given, check if the n number of flowers can be placed in the flowerbed,
        without voilating the rules.
        
        Args:
            flowerbed (List[int]): List specifying if flower present or not in ith position
            n (int): Number of flowers to be placed.

        Returns:
            bool: Return True if successfully n flowers are placed, else False.
        """
        
        length = len(flowerbed)
        count = 0
        i = 0
        
        while i < length:
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1  # Place flower
                    count += 1
                    if count >= n:
                        return True
                    i += 2  # Skip next position
                else:
                    i += 1
            else:
                i += 2  # Skip next position if current has flower
        
        return count >= n
    
s = Solution()

print(s.canPlaceFlowers([1,0,0,0,1], 1))
print(s.canPlaceFlowers([1,0,0,0,1], 2))
print(s.canPlaceFlowers([1,0,0,0,0,1], 2))
print(s.canPlaceFlowers([0,1,0], 1))