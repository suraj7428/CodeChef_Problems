for _ in range(int(input())):
    n,k,x,y=map(int,input().split())
    f="NO"
    c=x
    #for b in range(n*2):
    while f=="NO":
        if x <= n:
            
            if x == y:
                f="YES"
            x=x+k
        elif x > n:
            x=x-n
        if c == x :
            break
    print(f)
    
