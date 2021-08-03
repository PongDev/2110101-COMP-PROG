data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])
data.sort()
ans = []
last = None
for i in data:
    if (last != i):
        ans.append(i)
        last = i
print(len(ans))
print(ans[:10])
