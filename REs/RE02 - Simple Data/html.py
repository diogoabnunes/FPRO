#Use Spyder3 to create a file called html.py and write a program that asks a
# user to input a tag h and a string text  and prints an HTML valid element
# of the form <tag>text</tag>.

#For example, for a user input tag h1 and a text “I’m an HTML text”,
# the output must be “<h1>I’m an HTML text</h1>”

#Then, run the program for a user input tag b and html’s as text
#<b>html's</b>

h = input("Tag: ")
text = input("String Text: ")
print("<" + h + ">" + text + "</" + h + ">")

# copy of the result

#Tag: b
#
#String Text: html's
#<b>html's</b>

# copy of the program

#h = input("Tag: ")
#text = input("String Text: ")
#print("<" + h + ">" + text + "</" + h + ">")