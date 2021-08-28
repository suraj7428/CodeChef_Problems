# d1,v1,d2,v2,p=map(int,input().split())
# days=0
# if d1 != 1 or d2!=1:
#     for _ in range(1,min(d1,d2)):
#         days+=1
# if d1<d2:
#     for _ in range(0,d2-d1):
#         p=p-v1
#         days+=1
#         d1+=1
    
# elif d2 < d1:
#     for _ in range(0,d1-d2):
#         p=p-v2
#         days+=1
#         d2+=1
# if d1 == d2:
#         while p>0:
#             p=p-(v1+v2)
#             days+=1    
# # while p > 0:
# #     p=p-(v1+v2)
# #     days+=1
# print(days)


d1,v1,d2,v2,p=map(int,input().split())
days=0
# if (p<=v1 or p<=v2):
#       if d1<d2:
#             print(v1)
#       elif d1>d2:
#             print(v2)
#       elif d1==d2:
#             print(max(v1,v2))
if p<=v1 and p<=v2:
      if v1<v2:
            while p>0:
                  days+=1
                  p-=v1
      elif v2<=v1:
            while p>0:
                  days+=1
                  p-=v2
      
      #print(min(d1,d2))
else:
    if d1 != 1 or d2!=1:
        for _ in range(1,min(d1,d2)):
            days+=1
    if d1<d2:
        for _ in range(0,d2-d1):
            p=p-v1
            days+=1
            d1+=1
            if p <1:
                print(days)
    elif d2 < d1:
        for _ in range(0,d1-d2):
            p=p-v2
            days+=1
            d2+=1
            if p<1:
                print(days)
    if d1 == d2:
        while p>0:
            p=p-(v1+v2)
            days+=1    
        print(days)