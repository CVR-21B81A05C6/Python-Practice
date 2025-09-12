n = int(input("How many numbers? "))

numbers = set()

print("Enter", n, "distinct numbers:")
while len(numbers) < n:
    num = int(input(f"Enter number {len(numbers)+1}: "))
    if num in numbers:
        print("Duplicate! Enter a different number.")
    else:
        numbers.add(num)

total = sum(numbers)
print("Sum of the distinct numbers is:", total)
