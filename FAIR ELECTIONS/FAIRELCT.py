for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sa=sum(a);sb=sum(b)
    c=0
    if sa<=sb:
        while sa<=sb:
              if max(b)>min(a):
                    i=a.index(min(a))
                    j=b.index(max(b))
                    a[i],b[j]=b[j],a[i]
                    sa=sum(a)
                    sb=sum(b)
                    c+=1
              else:
                  c=-1
                  break
    elif sa>sb:
        c=0
    print(c)