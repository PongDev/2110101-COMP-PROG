data = [int(e) for e in input().split()]

ans = 0
for i in range(1, len(data)-1):
    if (data[i-1] < data[i] > data[i+1]):
        ans += 1
print(ans)
