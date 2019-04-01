
#Part A function   
def validate(val,begRange,endRange):
    #Checks if val is within range and returns True if it is
    if val >= begRange and val <= endRange:
        return True
    else:
        return False
        print(val,"is an invalid entry")
   

#part B
def getIntVal(begin,end):
    #Displays range
    print("Pick a number from", begin, "to", end)
    
    val = int(input("What is your number choice?: "))

    
    while val < begin or val > end:
        print("Invalid entry")
        val = int(input("What is your number choice?: "))

    validate(val, begin, end)#Validates if val is in range
    
    return val    
    

#Part C
def pattern1():

    intV = getIntVal(1, 15)#Calls getintVal
    #Decreasing loop for asterisks 
    for row in range(intV, 0 ,-1):
        for column in range(row, 0, -1): 
            print('*', end='')#end ="" acts as a terminator
        print()


#Part D
def pattern2():
  
    val = getIntVal(1, 15) #Calls getintVal
    
    #Loop for pound symbols   
    for row in range(val):
        print('#', end='')
        for column in range(0,(row)): 
            print(' ',end='')#Spaces pound sign by one as loop continues
        print('#')


#Part E
def turtleloop():
    import turtle

    for t in range(8):
        #Moves turtle a specified amount
        turtle.forward(200)
        #Specific angle determines specific star shape
        turtle.right(135)
        
def print_menu():
    print("Welcome to my artistic function. Please make a selection:")
    print("a. Draw the * pattern")
    print("b. Draw the # pattern")
    print("c. Draw a shape using a turtle library")
    
    
#Part F   
def main():
    position = True

    while position == True: #Used to loop code based on truth condition
        
        print_menu()
        choice = input("Make a choice: ")
        
#Cycles back to function begining if input doesnt match defined parameters
        while not(choice == "a" or choice == "b" or choice == "c"):
            print("Invalid entry")
            print_menu()
            choice = input("Make a selection: ") 
        
        
        #If/Elif statements to check different inputs
        if choice == "a" or choice == "A":
            pattern1()
            
        elif choice == "b" or choice == "B":
            pattern2()
            
        elif choice == "c" or choice == "C":
            turtleloop()
            
        #Asks if user wants to run again
        print("Do you want to run it again")
        decision = input("Yes or No: ")

        

        #If input doesnt fit defined parameter it asks user input again
        while not(decision == "Yes" or decision == "No" or decision == "no" or decision == "yes"):
             print("Invalid entry")
             print("Do you want to run it again")
             decision = input("Yes or No: ")

        #Predefined parameter of Yes or No
             #Yes loops it and No exits to the last line 

        if decision == "Yes" or decision == "yes":
            position = True
            
        elif decision == "No" or decision == "no":
            position = False
            
    print("Thank you for using our drawing services. Goodbye!")

main()





