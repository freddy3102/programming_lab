dict1={}
n=int(input("No of items in 1st Dictionary : "))
for i in range(n):
	key=input("Enter Key : ")
	value=input("Enter Value : ")
	dict1[key]=value
dict2={}
m=int(input("No of items in 2nd Dictionary : "))
for i in range(m):
	key=input("Enter Key : ")
	value=input("Enter Value : ")
	dict2[key]=value

print(dict1)
print(dict2)

dict3={**dict1,**dict2}

for i,j in dict3.items():
	if i in dict1 and i in dict2:
		dict3[i]=[dict1[i],j]

print("After Merging Dict1 with Dict2")
print(dict3)
