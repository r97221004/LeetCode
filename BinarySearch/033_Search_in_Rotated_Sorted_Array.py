# 時間複雜度: O(log(n))
# 空間複雜度: O(1)
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if found target value, return the index
            if nums[mid] == target:
                return mid
            
            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[left]: # left rotated
                # in ascending order side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right rotated
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1

p = Solution()
print(p.search([4,5,6,7,0,1,2], 0))