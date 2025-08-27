def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
        

people = int(input("How many people are in the group? "))
names = []
for i in range(people):
    name = input(f"Enter the name of person {i+1}: ").strip()
    names.append(name)

total_bill = get_float("Enter the total bill amount:")
share = round(total_bill / people,2)

print("\nBill Split Summary")
print("-"*30)
print("Total Bill Amount: ",total_bill)
for name in names:
    print(f"{name} owes: {share}")
print("-"*30)