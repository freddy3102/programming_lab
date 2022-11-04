
b=int(input("enter the final year"))
for i in range(2022,b+1):
    if i%4==0:
        if i%100==0:
            if i %400==0:
                print(i)
        else:
            print(i)

