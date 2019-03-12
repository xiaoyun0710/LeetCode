# Given n non-negative integers a1, a2, ..., an ,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i
# is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.


class Solution:
    def maxArea(self, height: [int]) -> int:

        # Step 1 O(n^2)
        # Max(i,j) means max area between i to j.
        # a(i,j) means area between i to j.
        # Max(i,j) = max(a(i,j), Max(i+i,j), Max(i,j-1))
        #
        # Step 2 O(n)
        # if height(i) > height(j):
        #
        # Max(i,j-1) = max(a(i,j-1),Max(i+1,j-1))
        # Max(i+1,j) = max(a(i+1,j),Max(i+1,j-1))        #
        # a(i,j-1) > a(i+1,j)
        #
        # Get Max(i,j-1) > Max(i+1,j)
        # And Max(i,j) = max(a(i,j), Max(i,j-1))

        area = 0

        start = 0
        end = len(height) - 1

        while end > start:
            if height[start] > height[end]:
                area = max((end - start) * height[end], area)
                end -= 1
            else:
                area = max((end - start) * height[start], area)
                start += 1

        return area
