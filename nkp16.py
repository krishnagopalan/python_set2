start,end=int(input().split())
for i in range(start+1,end):
	for j in range(2, i):
		if i % j  == 0:
			break
	else:
		string+=str(i)+" "
print(string.strip())