
 #Test of the program
 
#program reads and displays contents of myfile
def display():
    #Open a file named myfile.txt.
    infile = open('myfile.txt','r')

    #Reads file contents
    file_contents = infile.readline()
    n = file_contents.rstrip('\n')
    print( n,  n*5 )
    
    #Closes the file
    infile.close()

    #Prints the data that is in memory
    print(file_contents)
  
 

def dis():
    #program reads and displays contents of myfile
    #Open a file named myfile.txt.
    infile = open('my.txt','r')

    #Reads file contents
    file_contents = infile.readline()
    
    #Closes the file
    infile.close()

    #Prints the data that is in memory
    
    print(file_contents)

def output():
    #Takes numbers from txt file
    infile = open('my.txt','r')
    
    #Reads file contents
    mine = infile.readlines()

    #Closes the file
    infile.close()
    index = 0

    #Uses loop to output values into index
    while index < len(mine):
        mine[index] = int(mine[index].rstrip('\n'))
        index +=1
    print(mine)
    

    #squares each of the numbers in the index
    for n in range(index):
        mine[n]=int(mine[n])**2
    print(mine)
    print("Gideon Essel and Ronald Martinez")

    #makes a new txt file with the squared numbers
    outfile=open('my2.txt','w')
    for item in mine:
        outfile.write(str(item) + '\n')
    outfile.close()
output()
