n, m = map(int, input().split());

arr = [];

for _ in range(n):
    row = list(map(int,input().split()));
    arr.append(row);

cnt=0;

for i in range(n):
    sum=0;
    temp=0;
    for j in range(m):
        if arr[i][j] % 2 == 1:
            sum += arr[i][j];
            temp+=1;
            if sum % 2 == 0:
                cnt = max(cnt,temp);


print(cnt);