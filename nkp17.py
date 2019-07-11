nu=int(input())
su=0
temp=nu
while(temp>0):
  dig=temp%10
  su=su+dig ** 3
  temp=temp//10
if(su==nu):
  print("yes")
else:
  print("no")