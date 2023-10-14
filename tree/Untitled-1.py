num = int(input("Enter the height of the Christmas tree: "))
for i in range(1,num+1):
    print(" "*(num+1*-i+5) + "*"*(2*i-1))