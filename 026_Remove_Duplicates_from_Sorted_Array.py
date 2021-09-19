# 一個迴圈: 時間複雜度: O(n)
class Solution:
    def removeDuplicates(self, nums):
        if nums == []:
            return 0
        
        count = 1
        for i in range(len(nums)):
            if nums[i] != nums[count - 1]:
                nums[count] = nums[i]
                count += 1
        return count

p = Solution()
print(p.removeDuplicates([1, 1, 2, 3, 4]))

        