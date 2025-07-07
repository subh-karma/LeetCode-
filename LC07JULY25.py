import heapq
class Solution(object):
    def maxEvents(self, events):
        events = sorted(events, key = lambda x:x[0]) #1
        total_days = max(event[1] for event in events) #2
        min_heap = [] #3
        day, cnt, event_id = 1, 0, 0 #4
