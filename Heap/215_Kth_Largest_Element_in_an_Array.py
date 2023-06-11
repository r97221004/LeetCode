import heapq


class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums) - k]


class Solution:
    def findKthLargest(self, nums, k):
        nums = [-n for n in nums]
        heapq.heapify(nums)  # 時間複雜度 n 的操作

        for _ in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)
