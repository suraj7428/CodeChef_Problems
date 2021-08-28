# cook your dish here

for _ in range(int(input())):
    n=int(input())
    data = list(range(1,n+1))
    def permutation(lst): 
    	if len(lst) == 0: 
    		return [] 
    	if len(lst) == 1: 
    		return [lst] 
    	l = [] 
    	for i in range(len(lst)): 
    	    m = lst[i] 
    	    remLst = lst[:i] + lst[i+1:] 
    	    for p in permutation(remLst): 
    		    l.append([m] + p) 
    	return l 
    for b in permutation(data):
        m=0
        for c in range(len(b)-1):
            if b[c]&b[c+1]!=0:
                m+=1
            elif b[c]&b[c+1]==0:
                break
        if m == len(b)-1:
            print(*b)
            break
    if m < len(b)-1:
        print(-1)