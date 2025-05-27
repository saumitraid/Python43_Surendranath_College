ans='y'
while(ans=='y' or ans=='Y'):
    n1=int(input("Enter 1st Number:-"))
    n2=int(input("Enter 2nd Number:-"))
    print("Before swapping n1=%d and n2=%d"%(n1,n2))
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
    print("After swapping n1=%d and n2=%d"%(n1,n2))
    ans=input("Do you wnat to continue? Y/n")
