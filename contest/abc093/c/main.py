A = list(map(int, input().split()))
mid = sum(A) - max(A) - min(A)

if min(A) % 2 == mid % 2:
    print((mid - min(A)) // 2 + (max(A) - mid))
else:
    print((mid - min(A)) // 2 + (max(A) - mid) + 2)
