a=int(input())
s=0
f=1
b=a
while b>0:
    digit=b%10
    s+=digit
    f*=digit
    b=b//10
if s==f:
    print("spy num")
else:
    print("Not spy num")
