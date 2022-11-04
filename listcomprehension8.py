#list of positive numbers
a=list(map(int,input("enter the numbers with space").split(" ")))
b=[x for x in a if x>0]
print(b)
#square of n numbers
a=list(map(int,input("enter the numbers with space").split(" ")))
b=[x*x for x in a]
print(b)
#list  of vowels
a=list(input("enter the word").lower())
c=['a','e','i','o','u']
b=[x for x in a if x in c]
print(b)
#list ordinal value
a=list(input("enter the word"))
b=[ord(x) for x in a]
print(b)
