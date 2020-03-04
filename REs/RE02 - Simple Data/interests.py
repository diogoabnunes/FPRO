#The formula for computing the final amount if one is earning compound
# interest is given on Wikipedia as:
#A = P 1+rnnt
#Where:
#P = principal amount (the amount that the interest is provided on)
#r = the interest rate
#n = the frequency that the interest is paid out (per year)
#t = the number of years that the interest is calculated for
#Use Spyder3 to create a file called interests.py and write a program that
#replaces these letters with something a bit more human-readable,
# and calculate the final amount (A) at the end of the second year,
# for some varying amounts of money (P) at realistic interest rates (r): 
#P = 1000, n = 2, and r = 1%
#P = 650, n = 1 and r = -0.05%
#Values of P, n and r introduced by the user
#

#Then, run the program,
# and copy the result followed by your program (the content of the file interests.py) here:

P = 1000
n = 2
r = 1/100
t = 1
A = P * (1 + (r/n))**(n*t)
print(A)
P = 650
n = 1
r = -0.05/100
A = P * (1 + (r/n))**(n*t)
print(A)
P = int(input("P: "))
n = int(input("n: "))
r = input("r (in percentage): ")
r = float(r)
r = r/100
t = int(input("t: "))
A = P * (1 + (r/n))**(n*t)
print(A)

#1020.1505006249996
#649.3501625000001
#
#P: 1000
#
#n: 12
#
#r (in percentage): 5
#
#t: 15
#2113.7039324385305

#P = 1000
#n = 2
#r = 1/100
#t = 2
#A = P * (1 + (r/n))**(n*t)
#print(A)
#P = 650
#n = 1
#r = -0.05/100
#A = P * (1 + (r/n))**(n*t)
#print(A)
#P = int(input("P: "))
#n = int(input("n: "))
#r = input("r (in percentage): ")
#r = float(r)
#r = r/100
#t = int(input("t: "))
#A = P * (1 + (r/n))**(n*t)
#print(A)