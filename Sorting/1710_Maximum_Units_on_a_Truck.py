# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        res = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        for i, j in boxTypes:
            if truckSize - i >=0:
                res += i*j
                truckSize -= i
            else:
                res += truckSize*j
                break
                
        return res

p = Solution()
print(p.maximumUnits([[1,3], [2,2], [3,1]], 4))


                