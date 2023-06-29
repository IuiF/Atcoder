x = int(input())
n = 100
count = 0

while True:
    n += n // 100
    count += 1
    if n >= x:
        print(count)
        break
