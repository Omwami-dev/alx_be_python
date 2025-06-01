size = input("Enter the size of the pattern: "))
i = 1
while i <= size:
    j = i
    while j <= size:
        print("*",end=" ")
        j += 1
    print()
    i += 1
