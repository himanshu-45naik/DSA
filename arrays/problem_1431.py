# 1431. kids with greatest number of candies

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """There are n kids. A list of number of candies for each kid is given. An integer extracandies is given
        For each kid, if the addition of extracandies for ith kid is larger than any other assign true for that kid.
        Else assign false
        Args:
            candies (List[int]): The list of number of candies for each ith kid.
            extraCandies (int): The extra candies to be added for each ith kid.

        Returns:
            List[bool]: List of boolean specifying if the addition of extracandies for ith kid is highest among all the kids.
        """
        
        # First find the largest number of candies.
        n = len(candies)
        maxi = candies[0]
        for i in range(1, n):
            if candies[i] >= maxi:
                maxi = candies[i]
            
        # Add extra candies for each ith kid, if its larger than maxi assign True, else assign False.
        result = [True]* n
        for i in range(0, n):
            if (candies[i] + extraCandies) >= maxi:
                result[i] = True
            else:
                result[i] = False
        
        return result
    
s = Solution()
print(s.kidsWithCandies([1,3,5,6,2], 4))