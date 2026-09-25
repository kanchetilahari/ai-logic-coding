n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])
a.sort()
ans = []
for x, y in a:
    if len(ans) == 0:
        ans.append([x, y])
    elif x <= ans[-1][1]:
        if y > ans[-1][1]:
            ans[-1][1] = y
    else:
        ans.append([x, y])
for x, y in ans:
    print(x, y)