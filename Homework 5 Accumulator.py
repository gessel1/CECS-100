position = True

while position == True:
    print("Enter the upper limit of the sequence")
    decision = int(input('Your answer: '))


    while decision < 0:
        print("Please enter a positive value: ")
        decision = int(input('Your answer: '))

    else:
        sum = 0
        for x in range(1,decision,1):
            sum += x/(decision - x)
            
        print("The total is",format(sum,'.2f'))

    print("Do you want to run it again?")
    choice = input("Yes or No: ")

    if choice != "Yes" and choice != "yes" and choice != "Y" and choice != "y" :
        position = False
        
print("Until next time!")
    
    




