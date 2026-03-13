a=int(input())
if a<=1:
  print(a,"Not Prime")
else:
  for i in range(2,int(a**0.5)+1):
    if a%i==0:
      print(a,"Not prime")
  else:
    print(a,"Prime")
