amt = int(input("Enter an amount: "))

fiveHundereds = amt // 500
remainingAmt = amt % 500
hundereds = remainingAmt // 100
remainingAmt = remainingAmt % 100
twenties = remainingAmt // 20
remainingAmt = remainingAmt % 20
tens = remainingAmt // 10
remainingAmt = remainingAmt % 10
fives = remainingAmt // 5
ones = remainingAmt % 5

print(f"{amt} = {fiveHundereds} + {hundereds} + {twenties} + {tens} + {fives} + {ones}")

