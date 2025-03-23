class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        heap, min_time, cnt_ways = [(0, 0)], [inf]*n, [0]*n
        min_time[0], cnt_ways[0] = 0, 1
        while heap:
            curr_time, node = heappop(heap)
            if curr_time == min_time[node]:        
                for neighbor, time in graph[node]:
                    new_time = curr_time + time
                    if new_time < min_time[neighbor]:
                        heappush(heap, (new_time, neighbor))
                        min_time[neighbor] = new_time
                        cnt_ways[neighbor] = cnt_ways[node]
                    elif new_time == min_time[neighbor]:
                        cnt_ways[neighbor] = (cnt_ways[neighbor] + cnt_ways[node]) % 1000000007
        return cnt_ways[-1]
        
