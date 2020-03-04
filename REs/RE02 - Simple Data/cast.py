#Use Spyder3 to create a file called cast.py and write a program that asks
#a user to input a number n, calculates the expression n + nn + nnn and prints its value.
#For example, for a user input 5, the output must be 5 + 55 + 555 = 615.
#Then, run the program for a user input 9, 
#and copy the result followed by your program (the content of the file cast.py) here:

number = int(input("Number: "))
n = str(number)
n1 = n + n
n2 = n + n + n 
n = int(number)
ntotal = n + int(n1) + int(n2)
print(ntotal)

# copy of the result

#Number: 5
#615

# copy of the program

#number = int(input("Number: "))
#n = str(number)
#n1 = n + n
#n2 = n + n + n 
#n = int(number)
#ntotal = n + int(n1) + int(n2)
#print(ntotal)