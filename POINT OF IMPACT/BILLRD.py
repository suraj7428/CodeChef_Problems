for _ in range(int(input())):
    n,k,x,y=map(int,input().split())
    p=[]
    l=[]
    if x>y:
        y+=n-x
        x=n
        if (x==0 and y==n)or(x==n and y==0):
            print(x,y)
        else:
            l=[x,y]
            p.append(l)
            if k==1:
                print(x,y)

        x,y=y,x
        if (x==0 and y==n)or(x==n and y==0):
            print(x,y)
        else:
            l=[x,y]
            p.append(l)
            if k==2:
                print(x,y)

        x,y=y,x
        x=n-x
        y=n-y
        if (x==0 and y==n)or(x==n and y==0):
            print(x,y)
        else:
            l=[x,y]
            p.append(l)
            if k==3:
                print(x,y)

        if (x==0 and y==n)or(x==n and y==0):
            print(x,y)
        else:
            x,y=y,x
            l=[x,y]
            p.append(l)
            if k==4:
                print(x,y)

        if k>4:
            k=k%4
            c=p[k-1]
            print(*c)
    elif x<y:
        x+=n-y
        y=n
        if (x==0 and y==n)or(x==n and y==0):
            print(x,y)
        else:
            l=[x,y]
            p.append(l)
            if k==1:
                print(x,y)

        x,y=y,x
        if (x==0 and y==n)or(x==n and y==0):
            print(x,y)
        else:
            l=[x,y]
            p.append(l)
            if k==2:
                print(x,y)

        x,y=y,x
        y=n-y
        x=n-x
        if (x==0 and y==n)or(x==n and y==0):
            print(x,y)
        else:
            l=[x,y]
            p.append(l)
            if k==3:
                print(x,y)

        if (x==0 and y==n)or(x==n and y==0):
            print(x,y)
        else:
            x,y=y,x
            l=[x,y]
            p.append(l)
            if k==4:
                print(x,y)

        if k>4:
            k=k%4
            c=p[k-1]
            print(*c)
    elif x==y:
        print(n,n)
