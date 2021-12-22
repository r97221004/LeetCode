# Brute Force 暴力法
# 時間複查度 O(n*m), m = len(nums1) 且 n = len(nums2)
# 空間複雜度: O(n), 注意 result 是我們必要的返回結果，所以我們這裡可以不用算進去空間複雜度
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        data = {}
        for i, val in enumerate(nums2):
            data[val] = i
            
        for i, val in enumerate(nums1):
            for j in range(data[val] + 1, len(nums2)):
                if nums2[j] > val:
                    result.append(nums2[j])
                    break
            
            else:
                result.append(-1)
        
        return result

p = Solution()
print(p.nextGreaterElement([4,1,2], [1,3,4,2]))

# stack 堆疊
# 時間複雜度: O(n + n + m ) => O(n), 注意在這裡 nums1 是 nums2 的子集, 所以 m <= n
# 空間複雜度: O(n)
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        data = {}
        stack = []
        
        for i in nums2:
            while stack and stack[-1] < i:
                data[stack.pop()] = i
            stack.append(i)
            
        for i, val in enumerate(nums1):
            nums1[i] = data.get(val, -1)
        
        return nums1

p = Solution()
print(p.nextGreaterElement([4,1,2], [1,3,4,2]))

