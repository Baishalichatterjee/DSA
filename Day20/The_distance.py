def maximumstr(st):
    n=len(st);
    cnt=0;
    for i in range(0,n-1):
        for j in range(i+1,n):
            if st[i] != st[j]:
                temp = abs(i-j);
                cnt = max(cnt,temp);
    return cnt;

st = input();
result = maximumstr(st);
print(result);