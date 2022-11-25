import math

def perf_square(start,stop):
    new_list=[a for a in range(start,stop) if all(int(b)%2==0 for b in str(a))]
    sqr_list=[]
    for i in new_list:
        if int(math.sqrt(i)) * int(math.sqrt(i))==i:
            sqr_list.append(i)
    print("perfect squares are:")
    for e in sqr_list:
        print(e)
start=int(input("Enter the start range:"))
stop=int(input("Enter the stop range:"))
perf_square(start,stop)
