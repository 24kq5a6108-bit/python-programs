a=int(input("Enter a num: "))
def is_palindrome(a):
    b=a
    rev=0
    while a>0:
        digit=a%10
        rev=rev*10+digit
        a=a//10
    if b==rev:
        print("palindrome")
    else:
        print("Not palindrome ")
        
def is_prime(a):
 if a<=1:
     print("Not prime num")
 else:
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            print("Not Prime num")
            break
    else:
        print("Prime num")
        
def is_armstrong(a):
    b=a
    c=len(str(a))
    s=0
    while a>0:
        digit=a%10
        s+=digit**c
        a=a//10
    if b==s:
        print("Armstrong")
    else:
        print("Not Armstrong")
        
def is_magic(a):
    while a>9:
        s=0
        while a>0:
            digit=a%10
            s+=digit
            a=a//10
        a=s
    if a==1:
        print("Magic num")
    else:
        print("Not Magic num")
        
def is_spy(a):
    s=0
    f=1
    while a>0:
        digit=a%10
        s+=digit
        f*=digit
        a=a//10
    if s==f:
        print("Spy num")
    else:
        print("Not spy num")
        
is_palindrome(a)
is_prime(a)
is_armstrong(a)
is_magic(a)
is_spy(a)
