a=input('enter the values')
count=0
for i in range(0,len(a)+1):
	if a[i]==a[i+1]:
		count=count+1
	else:
		i=i+1
	i=i+2
	print(count)

