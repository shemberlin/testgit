def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))

avg(3,4,5)

