
#We want the user input to bring out different outputs


#However make sure to convert the input since this specific statement only works with floats

#For different program results we nest it

#If variable 'user' input matches name variable then we output a day of the week

day = int(input("Pick a number from 1 to 7: "))
#Keep in mind ==  means equal to

#Validates user entry
while day < 1 or day > 7:
    print("Wrong entry. Select a number from 1 to 7 ")
    day = int(input("Number: "))

#Proceeds if entry is valid and process it        
if day == 1:
    print('It is Monday')

elif day == 2:
    print('It is Tuesday')

elif day == 3:
    print('It is Wednesday')

elif day == 4:
    print('It is Thursday')

elif day == 5:
    print('It is Friday')

elif day == 6:
    print('It is Saturday')

else:
    print('It is Sunday')


