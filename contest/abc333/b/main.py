s = list(input())
t = list(input())
adjacent_pairs = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "A")]
diagonal_pairs = [("A", "C"), ("C", "E"), ("E", "B"), ("B", "D"), ("D", "A")]
s.sort()
s = tuple(s)
t.sort()
t = tuple(t)
if (
    (s in adjacent_pairs or s[::-1] in adjacent_pairs)
    and (t in adjacent_pairs or t[::-1] in adjacent_pairs)
) or (
    (s in diagonal_pairs or s[::-1] in diagonal_pairs)
    and (t in diagonal_pairs or t[::-1] in diagonal_pairs)
):
    print("Yes")
else:
    print("No")
