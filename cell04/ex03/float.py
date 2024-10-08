A = input("Give me a number: ")
B = float(A)#by doing this we change the string into float(floating point num).

if B.is_integer():
    print("This number is a integer.")
else:
    print("This number is a decimal.")
