n=int(input());
arr = list(map(int,input().split()));
cnt=0;
prev_pen = 'G' if arr[0]%2 == 1 else 'R';
for i in range(1,n):
    curr_pen = 'G' if arr[i]%2==1 else 'R';
    if prev_pen=='G' and curr_pen=='R':
        cnt+=1;
    prev_pen=curr_pen;
print(cnt);