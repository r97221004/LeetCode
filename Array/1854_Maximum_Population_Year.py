# 時間複雜度: O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def maximumPopulation(self, logs):
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))
        
        dates.sort()
        
        population = 0
        max_population = 0
        max_year = 0
        
        for i, j in dates:
            population += j
            if population > max_population:
                max_year = i
                max_population = population
        
        return max_year

p = Solution()
print(p.maximumPopulation([[1993,1999],[2000,2010]]))
        