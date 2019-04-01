#Gideon Essel and Ronald Martinez
#CECS 100
#We prompt user for gender
print("What is your gender")


#Lead in input to dual statement
gender = input("Are you a female?: ")

#if answer is yes then we use the statement below to calculate BMR of female

if 'yes':
    print( "How much do you weigh in pounds?")

    weight = int(input('weight:'))

    print('What is your height in inches?')
      
    height = int(input('height:'))

    print('How many years in age are you?')

    age = int(input('age:'))

    BMR =(655 + ( 4.3 * weight)+ (4.7 * height)-(4.7 * age))

    print("Your BMR is", BMR)
    
#Otherwise we skip down to use this statemnt to calculate
else :
    print( "How much do you weigh in pounds?")

    weight = int(input('weight:'))

    print('What is your height in inches?')
      
    height= int(input('height:'))

    print('How many years in age are you?')

    age = int(input('age:'))

    BMR =(66 + ( 6.3 * weight)+ (12.9 * height)-(6.8 * age))

    print("Your BMR is", BMR)
    
