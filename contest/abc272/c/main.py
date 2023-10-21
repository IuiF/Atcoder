n = int(input())
a = list(map(int, input().split()))
odd = [i for i in a if i % 2 != 0]
even = [i for i in a if i % 2 == 0]
if len(odd) < 2 and len(even) < 2:
    print(-1)
else:
    odd.sort(reverse=True)
    even.sort(reverse=True)
    print(max(sum(odd[:2]), sum(even[:2])))
