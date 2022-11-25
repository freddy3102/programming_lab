def list_sum():
	a=input("enter numbers:")
	a=a.split()
	b=[]
	for i in a:
		b.append(int(i))
	print("List sums to",sum(b))
list_sum()
