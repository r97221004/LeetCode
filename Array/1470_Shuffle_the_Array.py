# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def shuffle(self, nums, n):
        result = []
        for i, j in zip(nums[0:n], nums[n:]):
            result += [i, j] 
        
        return result

p = Solution()
print(p.shuffle([2, 5, 1, 3, 4, 7], n = 3))

# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution(object):
    def shuffle(self, nums, n):
        from functools import reduce
        return reduce(lambda x, y: x + y, zip(nums[:n], nums[n:]))

p = Solution()
print(p.shuffle([2, 5, 1, 3, 4, 7], n = 3))
    