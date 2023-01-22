# day 3.5 - love calculator 

print("Welcome to Pyton Pizza")

print("small pizza: $15")
print("medium pizza: $20")
print("large pizza: $25")

size = input("which size will it be? S, M or L? ")

print("add pepperoni for small pizza: +$2")
print("add pepperoni for medium or large pizza: +$3")

add_pepperoni = input("would you like to add some pepperoni? Y/N")

extra_cheese = input("would you like some extra cheese for $3? Y/N")

final_bill = 0

if size == "S":
  final_bill += 15
if size == "M":
  final_bill += 20
if size == "L":
  final_bill += 25

if add_pepperoni == "Y":
  if size == "S":
    final_bill += 2
  if size == "M" or size == "L":
    final_bill += 3

if extra_cheese == "Y":
  final_bill += 3

print(f"your final bill is {final_bill}")