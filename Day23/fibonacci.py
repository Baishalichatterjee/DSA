def fibonacci(n:int)->int:
    if n==0 or n==1:
        return n;
    else :
        return fibonacci(n-1) + fibonacci(n-2);

n=int(input());
res = fibonacci(n);
print(res);