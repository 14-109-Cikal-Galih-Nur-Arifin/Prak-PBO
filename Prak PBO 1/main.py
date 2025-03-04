height = int(input("Height: "))

for i in range(height): 
    print(" " * (height - i - 1) + "*" * (2 * i + 1))