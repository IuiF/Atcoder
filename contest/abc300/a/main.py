N, A, B = map(int, input().split())
ans_list = list(map(int, input().split()))
ans = A + B
print(ans_list.index(ans) + 1)
