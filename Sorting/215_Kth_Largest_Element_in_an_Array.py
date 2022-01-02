# 時間複雜度: O(n*log(n))
# 空間複雜度: O(n)
class Solution(object):
    def findKthLargest(self, nums, k):
        self.mergeSort(nums)
        nums = nums[::-1]
        return nums[k - 1]
        
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] > R[j]:
                    nums[k] = R[j]
                    j += 1
                    k += 1
                else:
                    nums[k] = L[i]
                    i += 1
                    k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

p = Solution()
print(p.findKthLargest([3, 2, 1, 5, 6, 4], 2))

# 時間複雜度: O(n*log(n))
# 空間複雜度: O(n)
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse = True)
        return nums[k - 1]

p = Solution()
print(p.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    
