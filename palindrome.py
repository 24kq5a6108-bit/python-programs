a=int(input("num:"))
b=a
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a//=10
if b==rev:
    print("Palindrome")
else:
    print("Not palindrome")
