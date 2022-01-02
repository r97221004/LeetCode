# 時間複雜度: O(nlog(n))
# 空間複雜度: O(n)
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        free_rooms = []
        intervals.sort(key = lambda x:x[0])
        
        heapq.heappush(free_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
                
            heapq.heappush(free_rooms, i[1])
            
        return len(free_rooms)

p = Solution()
print(p.minMeetingRooms([[0,30], [5,10], [15,20]]))


# 時間複雜度: O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        free_rooms = []
        intervals.sort(key = lambda x: x[0])
        
        free_rooms.append(intervals[0][1])
        
        for i in intervals[1:]:
            if free_rooms[-1] <= i[0]:
                free_rooms.pop()
                
            free_rooms.append(i[1])
            free_rooms.sort(reverse = True)
            
        return len(free_rooms)

p = Solution()
print(p.minMeetingRooms([[0,30], [5,10], [15,20]]))


# 時間複雜度: O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def minMeetingRooms(self, intervals):
        record = []
        res = 0
        count = 0
        
        for i, j in intervals:
            record.append([i, 1])
            record.append([j, -1])
            
        record.sort() # 這裡不能改成 record.sort(key=lambda x: x[0]) 
        
        for i, j in record:
            count += j
            if count > res: res = count
                
        return res

p = Solution()
print(p.minMeetingRooms([[0,30], [5,10], [15,20]]))