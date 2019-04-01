def file():
    import random

    #opens our file

    infile = open ("out.txt",'w')

    #generates a list of random numbers

    for i in range(10):

        digit = random.randint(1,100)

        digit = str(digit)

        infile.write(digit + "\n")

file()

