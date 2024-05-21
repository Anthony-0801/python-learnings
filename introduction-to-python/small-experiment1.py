name= input ("Please enter your name: ")
age= input ("Please enter your age: ")
address= input ("Please enter your address: ")
print (name, age, address)


# You're building 10 ships per month and that cost at least 20,000,000 plus with the maintenance of 1,000,000 insurance.
# Now you sell each ship at the price of 3,000,000. Determine if you have "Profit" to be gained, "Loss", or "Broke Even"

total_cost = 21000000
sold = input()
total_profit = int(sold) * 3000000

if total_cost > total_profit:
  print("Loss")
elif total_cost < total_profit:
  print("Profit")
elif total_cost == total_profit:
  print("Broke Even")
