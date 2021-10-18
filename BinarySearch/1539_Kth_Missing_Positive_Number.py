# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def findKthPositive(self, arr, k):
        arr = [0] + arr
        for i, j in zip(arr, arr[1:]):
            if j - i -1 >= k:
                return i + k
            else:
                k -= (j - i - 1)
        
        return arr[-1] + k

p = Solution()
print(p.findKthPositive([2,3,4,7,11], 5))


# 時間複雜度: O(log(n))
# 空間複雜度: O(1)
class Solution:
    def findKthPositive(self, arr, k):
        beg, end = 0, len(arr)
        
        while beg < end:
            mid = (beg + end)//2
            if arr[mid] - mid - 1 >= k:
                end = mid
            else:
                beg = mid + 1
        
        return arr[beg - 1] + k - (arr[beg - 1] - (beg - 1) - 1 )

p = Solution()
print(p.findKthPositive([2, 3, 4, 7, 11], 5))