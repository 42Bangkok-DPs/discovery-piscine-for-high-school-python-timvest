A = input("Give me a number: ")
B = float(A)

if B.is_integer():
    print(f"{B} is a integer.")
else:
    print(f"{B} is a decimal.")