a=list(map(int,input().split()))
pos=0
neg=0
for i in range (0,len(a)):
    if a[i]>0:
        pos+=1
    elif a[i]<0:
        neg+=1
print("pos :",pos)
print("neg :",neg)
