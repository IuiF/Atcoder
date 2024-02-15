from collections import Counter

n = int(input())
a = list(map(int, input().split()))
evens = a[0::2]
odds = a[1::2]
evens_cnt = Counter(evens)
odds_cnt = Counter(odds)

if evens_cnt.most_common(1)[0][0] == odds_cnt.most_common(1)[0][0]:
    if len(evens_cnt) == 1 and len(odds_cnt) == 1:
        print(n // 2)
    else:
        second_most_common_even = (
            evens_cnt.most_common(2)[1][1] if len(evens_cnt) > 1 else 0
        )
        second_most_common_odd = (
            odds_cnt.most_common(2)[1][1] if len(odds_cnt) > 1 else 0
        )
        if evens_cnt.most_common(1)[0][1] > odds_cnt.most_common(1)[0][1]:
            print(n - evens_cnt.most_common(1)[0][1] - second_most_common_odd)
        elif evens_cnt.most_common(1)[0][1] < odds_cnt.most_common(1)[0][1]:
            print(n - second_most_common_even - odds_cnt.most_common(1)[0][1])
        else:
            print(
                min(
                    n - evens_cnt.most_common(1)[0][1] - second_most_common_odd,
                    n - second_most_common_even - odds_cnt.most_common(1)[0][1],
                )
            )
else:
    print(n - evens_cnt.most_common(1)[0][1] - odds_cnt.most_common(1)[0][1])
