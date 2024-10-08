A = 0
while A <= 10:#up to 10
    B = 0#inside the loop for the conditions
    print(f"Table de {A}", end=' ')#end to go to next line
    while B <= 10:
        print(A * B, end=' ')
        B += 1
        if B > 10:
            break 
    print()
    A += 1  #num goes by 1 