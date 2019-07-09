i,j=map(int,input().split())
if j<=100000:
     for k in range(i+1,j):
           if(k%2!=0):
                 print(k)
