import itertools


def swap_and_check(h, w, a, b, h_perm, w_perm):
    swapped_b_cols = [[b[i][w_perm[j]] for j in range(w)] for i in range(h)]
    swapped_b = [swapped_b_cols[h_perm[i]] for i in range(h)]
    return swapped_b == a


def bubble_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            steps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return steps


h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

if a == b:
    print(0)
else:
    ar_h = [i for i in range(h)]
    h_patterns = list(itertools.permutations(range(h)))
    w_patterns = list(itertools.permutations(range(w)))
    ans = float("inf")
    for h_perm in h_patterns:
        for w_perm in w_patterns:
            if swap_and_check(h, w, a, b, h_perm, w_perm):
                h_swaps = bubble_sort(list(h_perm))
                w_swaps = bubble_sort(list(w_perm))
                total_swaps = h_swaps + w_swaps
                ans = min(ans, total_swaps)
    print(ans if ans != float("inf") else -1)
