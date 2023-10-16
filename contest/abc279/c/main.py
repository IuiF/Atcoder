h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
rot_s = [list(x) for x in zip(*s)]
rot_s.sort()
t = [list(input()) for _ in range(h)]
rot_t = [list(x) for x in zip(*t)]
rot_t.sort()

print("Yes" if rot_s == rot_t else "No")
