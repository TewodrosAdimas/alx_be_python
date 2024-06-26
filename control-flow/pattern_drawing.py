row = column =int(input("Enter the size of the pattern: "))
while row>0:
    for col in range(0,column):
        print("*", end="")
    print()
    row-=1