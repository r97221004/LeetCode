# 時間複雜度：O(n)
# 空間複雜度：O(1)
class Solution:
    def maxArea(self, height):
        # BRUTE FORCE
        # maxArea = 0

        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         area = (j - i)*min(height[i], height[j])
        #         maxArea = max(maxArea, area)

        # return maxArea

        maxArea = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left)*min(height[left], height[right])
            maxArea = max(maxArea, area)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return maxArea


p = Solution()
print(p.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
