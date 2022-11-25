def fib(n):
    i=0
    a,b=0,1
    while i<=n:
        print (b,end=' ')
        a,b=b,a+b
        i=i+1

n=int(input("Enter a number:"))
fib(n)
print()
