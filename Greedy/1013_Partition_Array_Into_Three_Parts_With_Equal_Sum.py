# 時間複雜度: O(n)
# 空間複雜度: O(1)

class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total%3 != 0: return False
        
        count, cumsum, target = 0, 0, total//3
        for i in arr:
            cumsum += i
            if cumsum == target: 
                cumsum = 0
                count += 1
        
        return count >= 3 # 會有像 arr = [1 -1 1 -1 1 -1 1 -1] 的例子，所以要大於等於 3

p = Solution()
print(p.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))