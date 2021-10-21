# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        result = 0
        for i, j in boxTypes:
            if i >= truckSize:
                result += truckSize*j
                return result
            else:
                result += i*j
                truckSize -= i
        
        return result

p = Solution()
print(p.maximumUnits([[1,3],[2,2],[3,1]], 4))
                