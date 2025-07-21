arr = list(map(int, input().split()))
n = int(input())
target = int(input())
arr.sort()
cnt = 0
totalhours = 0
for i in range(0,n):
    if totalhours + arr[i] <= target:
        totalhours += arr[i]
        cnt += 1
    else:
        break
print(cnt)