def soln(S, T, N, M, a, b):
    # メモ化のための配列を初期化
    memo = {}

    # 再帰的に解く関数を定義
    def dp(pos, time_left):
        # メモ化されている場合はそれを返す
        if (pos, time_left) in memo:
            return memo[(pos, time_left)]

        # 買えるかもしれない店の個数
        shops_visited = 0

        # 走査する座標の範囲
        lo, hi = 0, pos
        if S > pos:
            lo, hi = pos, S

        # 店を通る
        for p in a:
            if lo <= p <= hi:
                if time_left >= abs(pos - p) + 1:
                    shops_visited = max(
                        shops_visited, 1 + dp(p, time_left - abs(pos - p) - 1)
                    )

        # テレポートする
        for p in b:
            if time_left >= abs(pos - p) + 1:
                shops_visited = max(shops_visited, dp(p, time_left - abs(pos - p) - 1))

        # ゴールに到達する
        if pos == S and time_left >= 0:
            shops_visited = max(shops_visited, 0)

        # メモ化して返す
        memo[(pos, time_left)] = shops_visited
        return shops_visited

    # 初期呼び出し
    P = -dp(0, T)
    Q = T

    # 最適解を求める
    for time in range(T + 1):
        current = -dp(0, time)
        if current == P:
            Q = time
            break

    return P, Q


# 入力を読む
N, M, S, T = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*soln(S, T, N, M, a, b))
