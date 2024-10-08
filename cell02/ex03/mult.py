print("Enter your first number:")
first_number = int(input())
print("Enter your second number:")
sec_number = int(input())
print(first_number,"x",sec_number,"=",int(first_number*sec_number))
num = int(first_number*sec_number)
if num <0:
    print("The result is a negative.")
if num >0:
    print("The result is a positive.")
else:
    print("The result is both a negative and positive.")
