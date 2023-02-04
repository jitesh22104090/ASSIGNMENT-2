a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))

if a>b+c|b>c+a|c>a+b:
    print("no triangle cannot be formed")
else:
    print("triangle can be formed")
