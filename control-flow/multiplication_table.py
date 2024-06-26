number = int(input("Enter a number to see its multiplication table: "))
for num in range(1,11):
    mul = num * number
    print(f"{number} * {num} = {mul}" )