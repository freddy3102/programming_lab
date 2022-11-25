def fact(n):
    i=1
    prod=i
    while i<=n:
        prod*=i
        i=i+1
    return prod
n=int(input("Enter a number:"))
print("factorial is",fact(n))
