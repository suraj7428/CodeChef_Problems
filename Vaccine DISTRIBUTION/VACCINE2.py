import math
for _ in range(int(input())):
      n,d=map(int,input().split())
      a=list(map(int,input().split()))
      r=[];nr=[]
      for b in a:
          if b <=9 or b >= 80:
              r.append(b)
          else:
              nr.append(b)
      days=0
      days=math.ceil(len(r)/d)
      days=days+math.ceil(len(nr)/d)
      print(days)