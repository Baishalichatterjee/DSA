n=int(input());
m=int(input());
a = list(map(int,input().split()));
b = list(map(int,input().split()));
ans = [];
i=0;
j=0;
while i<n and j<m:
    if a[i] < b[j]:
        ans.append(a[i]);
        i+=1;
    else:
        ans.append(b[j]);
        j+=1;
while i<n:
    ans.append(a[i]);
    i+=1;
while j<m:
    ans.append(b[j]);
    j+=1;
k=len(ans);
if k%2 == 0:
    res = (ans[k//2] + ans[k//2 - 1])//2;
else:
    res = ans[k//2];
print(res);