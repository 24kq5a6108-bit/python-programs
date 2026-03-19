a=int(input())
while a>9:
    s=0
    while a>0:
        digit=a%10
        s+=digit
        a=a//10
    a=s
if a==1:
    print("1")
else:
    print("0")
