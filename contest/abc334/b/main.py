a, m, l, r = map(int, input().split())
tree_min = (l - a + m - 1) // m
tree_max = (r - a) // m
print(max(0, tree_max - tree_min + 1))
