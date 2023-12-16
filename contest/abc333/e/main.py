n = int(input())
events = [list(map(int, input().split())) for _ in range(n)]

future_needs = {}
actions = [0] * len(events)

for i in range(len(events) - 1, -1, -1):
    t, x = events[i]
    if t == 2:
        future_needs[x] = future_needs.get(x, 0) + 1
    elif t == 1:
        if future_needs.get(x, 0) > 0:
            actions[i] = 1
            future_needs[x] -= 1
        else:
            actions[i] = 0


K_min = 0
current_potions = 0
for i, (t, x) in enumerate(events):
    if t == 1 and actions[i] == 1:
        current_potions += 1
        K_min = max(K_min, current_potions)
    elif t == 2:
        if current_potions > 0:
            current_potions -= 1

print(K_min)
print(*actions)
