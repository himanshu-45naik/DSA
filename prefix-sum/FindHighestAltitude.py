# 1732. Find the highest Altitude

# There is a biker going on a road trip. 
# The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        
        altitude = 0
        max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude
    
s = Solution()
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))
print(s.largestAltitude([-5,1,5,0,-7]))