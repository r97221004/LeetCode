# Bubble Sort(氣泡排序)
# Time Limit Exceeded
# 時間複雜度: O(n**2)
# 空間複雜度: O(1)
class Solution(object):
    def sortArray(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
        return nums

p = Solution()
print(p.sortArray([6, 5, 3, 1, 8, 7, 2, 4]))


# Merge Sort
# 時間複雜度: O(n*log(n))
# 空間複雜度: O(n)
class Solution(object):
    def sortArray(self, nums):
        self.mergeSort(nums)
        return nums
    
	# @mergeSort
    def mergeSort(self, nums): 
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 
            
            # recursion
            self.mergeSort(L)
            self.mergeSort(R)
            
            # merge
            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i += 1
                else: 
                    nums[k] = R[j] 
                    j += 1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i += 1
                k += 1

            while j < len(R): 
                nums[k] = R[j] 
                j += 1
                k += 1

p = Solution()
print(p.sortArray([6, 5, 3, 1, 8, 7, 2, 4]))