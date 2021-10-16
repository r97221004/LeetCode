# 時間複雜度: O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def highFive(self, items):
        items.sort(reverse = True)
        result = []
        curr = []
        idx = items[0][0]
        
        for i, val in items:
            if i == idx:
                if len(curr) < 5:
                    curr.append(val)
            else:
                result.append([idx, sum(curr)//len(curr)])  # 要的是整數部分，所以用 // 運算子
                curr = [val]
                idx = i
        
        result.append([idx, sum(curr)//len(curr)])
        result = result[::-1]
        
        return result

p = Solution()
print(p.highFive( [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76], [2,10]]))