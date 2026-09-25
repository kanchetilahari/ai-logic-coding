n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
i = 0
j = 0
carry = 0
result = []
while i < n or j < m or carry != 0:
    if i < n:
        x = a[i]
    else:
        x = 0
    if j < m:
        y = b[j]
    else:
        y = 0
    s = x + y + carry
    result.append(s % 10)
    carry = s // 10
    i += 1
    j += 1
print(*result)