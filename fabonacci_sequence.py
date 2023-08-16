n=int(input("Enter the no.of terms:-"))
def fabanacci_series(n):
    n1=0
    n2=1
    print(n1,n2,end=" ")
    for i in range(2,n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")
fabanacci_series(n)
