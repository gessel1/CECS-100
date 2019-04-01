#Gideon and Ronald
#CECS 100

#Prompt user for the charge of the food
print("What is the price of the food")

#user inputs here. Redefine string as input for later use
food_price = int(input('Price:'))

#Percentage tip comes from the given price times .18(18 percent)
percent_tip = food_price * .18

#Sales tax comes from the given price
sales_tax = food_price * .07

#We calculate the total price by adding the food price as well as percent tip
#and sales tax
total_price = (food_price + percent_tip + sales_tax)

print("Your total price is $",total_price)
