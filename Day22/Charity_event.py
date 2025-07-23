mod = 10**9+7;
n=int(input());
total=0;
for i in range(1,n+1):
    chocolate = i;
    left = i-1 if i>1 else n;
    right = i+1 if i<n else 1;
    if left%5==0 or right%5==0:
        chocolate+=2;
    total+=chocolate%mod;
print(total);