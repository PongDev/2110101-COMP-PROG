ans = []
count = 0

n = int(input())
for i in range(n):
    data = int(input())
    if count % 2 == 0:
        ans.append(data)
    else:
        ans = [data]+ans
    count += 1
for data in [int(e) for e in input().split()]:
    if (count % 2 == 0):
        ans.append(data)
    else:
        ans = [data]+ans
    count += 1
while True:
    data = int(input())
    if (data == -1):
        break
    if (count % 2 == 0):
        ans.append(data)
    else:
        ans = [data]+ans
    count += 1
print(ans)
