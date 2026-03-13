a=int(input("Enter a num:"))
c=0
while a>0:
    digit=a%10
    c+=digit
    a//=10
print(c) 
