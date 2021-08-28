# cook your dish here
for _ in range(int(input())):
      n=int(input())
      # f=0
      # for a in range(1,10):
      #       for b in range(1,10):
      #             if ((a&b)+(a|b))==n:
      #                   f=1
      #                   print(a,b)
      #                   break
      #             else:
      #                   f=0
      #       if f == 1:
      #             break
      # if f == 0:
      #       print(-1)
      for i in range(1,n+1):
          a=i
          b=n-i
          if (a&b)+(a|b) == n:
              f=0
              print(a,b)
              break
      if f : print(-1)