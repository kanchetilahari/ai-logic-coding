from collections import deque
n = int(input())
nums = list(map(int, input().split()))
k = int(input())
high = deque()
low = deque()
left = 0
max_len = 0
answer_pos = 1
for right in range(n):
    while high and nums[high[-1]] < nums[right]:
        high.pop()
    high.append(right)
    while low and nums[low[-1]] > nums[right]:
        low.pop()
    low.append(right)
    while nums[high[0]] - nums[low[0]] > k:
        if high[0] == left:
            high.popleft()
        if low[0] == left:
            low.popleft()
        left += 1
    current = right - left + 1
    if current > max_len:
        max_len = current
        answer_pos = left + 1
print(max_len, answer_pos)