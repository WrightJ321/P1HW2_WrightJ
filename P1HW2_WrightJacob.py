# Family Vacation budget tool(This program calculates and displays travel expenses)
#9/08/2023
# CTI-110 P1HW2 - Travel Expense
# Wright, Jacob
# Budget=3000.00, Destination=California, Transportation=plane, Gas=200,hotel=750, food=320.00
print("What will your budget be for this trip?") 
# budget is 3000
budget = int(input())
print("Where will you be traveling to?")
# destination is California
Destination = input()
print("Will you be traveling by plane or car?")
# traveling by plane but user may spend money on rental car
transportation = input()
if (transportation == "plane"):
  print("Great!")
else:
  print("Road trips create the best memories!")
print("About how much are you willing to pay for gas?")
# cost of gas is 200 via possible rental car
gas = int(input())
print("Almost done! How much are you willing to spend on a hotel?")
# hotel cost is 750
hotel = int(input())
print("Finally! How much are you going to need for food and drinks?")
# food cost is 320
food = int(input())
print("------Travel Expenses------")
print("Trip location:", Destination)
print("Chosen budget:", budget)
print("Fuel cost:", gas)
print("Hotel:", hotel)
print("Food:", food)
print("Total cost of trip to", Destination, "is: $", gas + food + hotel)
remainingbalance = budget - gas - food - hotel
print("Your remaining balance: $", remainingbalance)

