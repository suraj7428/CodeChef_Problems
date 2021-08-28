# # cook your dish here
# for _ in range(int(input())):      
#       a,b=map(int,input().split())
#       c=0
#       for x in range(1,a+1):
#           for y in range(1,b+1):
#               if (x+y)%2==0:
#                   c+=1
#       print(c)

for _ in range(int(input())):
      a,b=map(int,input().split())
      c=0
      if a%2==0:
          Ao=a//2
          Ae=a//2
      else:
          Ae=a//2
          Ao=Ae+1
      if b%2==0:
          Bo=b//2
          Be=b//2
      else:
          Be=b//2
          Bo=Be+1
      c=(Ao*Bo)+(Ae*Be)
      print(c)