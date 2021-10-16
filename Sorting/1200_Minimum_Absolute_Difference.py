# 時間複雜度: O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def minimumAbsDifference(self, arr):        
        arr.sort()
        mn = min([j - i for i, j in zip(arr, arr[1:])])
        result = [[i, j] for i, j in zip(arr, arr[1:]) if j - i == mn]
        return result

p = Solution()
print(p.minimumAbsDifference([4,2,1,3]))