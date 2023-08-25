n=int(input("Enter the no.of terms:- "))
def fabanacci_generator(n):
    n1=0
    n2=1
    for i in range(n):
        yield n1
        n3=n1+n2
        n1=n2
        n2=n3
fab_gen=fabanacci_generator(n)
for num in fab_gen:
    print(num)