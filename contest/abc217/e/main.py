from collections import deque
import heapq


arr = deque([])
que = []
heapq.heapify(que)

q = int(input())
for _ in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        arr.append(a[1])
    elif a[0] == 2:
        if len(que) > 0:
            print(heapq.heappop(que))
        else:
            print(arr.popleft())
    else:
        for _ in range(len(arr)):
            heapq.heappush(que, arr.popleft())
