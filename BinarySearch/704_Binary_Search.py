# 時間複雜度: O(n)
class Solution:
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
p = Solution()
print(p.search([-1,0,3,5,9,12], 9))

# Classical binary search  
# 時間複雜度: O(log(n))
class Solution:
    def search(self, nums, target):
        beg, end = 0, len(nums)
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
                
        if beg < len(nums) and nums[beg] == target:
            return beg
        else:
            return -1
p = Solution()
print(p.search([-1,0,3,5,9,12], 9))

# 時間複雜度: 使用內建函式，不算時間複雜度
class Solution:
    def search(self, nums, target):
        try:
            return nums.index(target)
        except:
            return -1

lst = [1, 2, 4]
print(lst.index(3))