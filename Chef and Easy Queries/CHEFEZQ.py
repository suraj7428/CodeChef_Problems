
for _ in range(int(input())):
    n,k=map(int,input().split())
    q=list(map(int,input().split()))
    a=0;d=0
    for x in range(n):
        a=a+q[x]

    if k == 1:
        print(a+1)
    elif k > 1:
        
        if k < a:
            a=a//k
            print(a+1)
        else:
            print(1)
            