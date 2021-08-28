# cook your dish here
for _ in range(int(input())):
    n=input()
    c=list(map(int,input().split()))
    b1=[];b2=[]
    c.sort()
    m=max(c)
    b1.append(m)
    p=c.index(m)
    c.pop(p)
    for x in range(int(n)-1):
        m=max(c)
        if sum(b1) > sum(b2):
            b2.append(m)
            p=c.index(m)
            c.pop(p)
        elif sum(b1) <= sum(b2):
            b1.append(m)
            p=c.index(m)
            c.pop(p)
    if sum(b1) >= sum(b2):
        print(sum(b1))
    else:
        print(sum(b2))
