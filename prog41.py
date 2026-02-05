print("Enter an item on your grocery list, then the bot will give you the [taxes aren't included].")
reciept = 0

while True:
    item = float(input("\nEnter an item price on the list: "))

    if item == 0:
        break
    else:
        reciept = reciept + item

print("\nYour total bill is (without taxes): ", reciept)