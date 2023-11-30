from collections import deque
import heapq


arr = deque([])
que = []
q = int(input())
for _ in range(q):
    a = input()
    if a[0] == "1":
        arr.append(int(a[-1]))
    elif a[0] == "2":
        if len(que) > 0:
            print(heapq.heappop(que))
        else:
            print(arr.popleft())
    else:
        que.extend(list(arr))
        arr.clear()
        heapq.heapify(que)
