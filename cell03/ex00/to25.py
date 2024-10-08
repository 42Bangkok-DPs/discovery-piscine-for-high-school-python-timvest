print("Enter a number less than 25")
A = int(input())
if A >25:
    print("Error")
while (A < 25):
    A = A + 1
    print("Inside the loop, my variable is",A)