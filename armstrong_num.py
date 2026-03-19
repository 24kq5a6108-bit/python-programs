a=int(input())
b=a
c=len(str(a))
s=0
while a>0:
    digit=a%10
    s+=digit**c
    a=a//10
if b==s:
    print("Arm")
else:
    print("Not arm")
