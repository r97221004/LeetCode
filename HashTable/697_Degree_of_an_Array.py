# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def findShortestSubArray(self, nums):
        first = {}
        count ={}
        deg = 0
        res = 0

        for i, val in enumerate(nums):
            first.setdefault(val, i)
            count[val] = count.get(val, 0) + 1
            
            if count[val] == deg:
                res =  min(res, i - first[val] + 1)
            elif count[val] > deg:
                res = i - first[val] + 1
                deg = count[val]
            
        return res
    

p = Solution()
print(p.findShortestSubArray([1, 2, 2, 3, 1]))