# cook your dish here
for _ in range(int(input())):
      n=int(input())
      p=list(map(int,input().split()))
      t=p[0]
      d=0;c=1
      while t>0:
          d+=1
          t-=1
          if c< len(p):
              t=t+p[c]
              p[c]=0
              c+=1
      
      print(d)