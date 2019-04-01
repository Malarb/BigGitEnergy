#!/usr/bin/env python3

# ssh midn.cyber.usna.edu
# tail -f /var/log/apache2/error.log | grep m206552

import cgi, cgitb
import re

# Function used to make the inputs safe
def escapeChars(input):
    newInput = input
    if "&" in input:
        newInput = newInput.replace("&","&amp")
    if "<" in input:
        newInput = newInput.replace("<","&lt")
    if ">" in input:
        newInput = newInput.replace(">","&gt")
    return newInput

cgitb.enable()
form = cgi.FieldStorage()

print('Content-type: text/html\n\n')

errors = 0
fUSERSa = open("USERS.txt",'a')
fUSERSr = open("USERS.txt",'r')
# Checking first text field is not empty
email = form.getvalue("email")
if email == "":
    print("<p> Please enter a email. </p>")
    errors += 1

# Checking first text area is not empty
textArea = form.getvalue("moment")
if textArea == "":
    print("<p> Please enter your most memorable moment. </p>")
    errors += 1

# Checking that at least one radio button is selected
radio = form.getlist("radio1")
if radio == "":
    print("<p> Please check your potato preference. </p>")
    errors += 1

# Checking hte password is not empty and contains a digit
passWord = form.getvalue("pwd1")
if passWord == "":
    print("<p> Please enter a password. </p>")
    errors += 1
elif re.search('\d', passWord) == None:
    print("<p> Make sure your password has at least one number.")
    errors += 1

# Get the username and read through USERS.txt and put all the usernames into a list
username = form.getvalue("username")
userNameList = []
for line in fUSERSr.readlines():
    splitLine = (line.strip()).split("\t")
    userNameList.append(splitLine[1])

# Check to see if the username is unique, if it is within the list then tell teh user to try a new one
if username in userNameList:
    print("<h3> Your requested username is already taken. Please hit the back button and try a new one. </h3>")
# If there are no errors than express thanks and display the information
# otherwise tell the user to hit the back button
elif errors == 0:
    # Make all the inputs safe
    emailSafe = escapeChars(email)
    usernameSafe = escapeChars(username)
    radioSafe = escapeChars(radio[0])
    textAreaSafe = escapeChars(textArea)
    passWordSafe = escapeChars(passWord)

    print("<h1> Thanks for signing up for the greatest potato website of all time! </h1>")
    print("<h3> Your information is as follows: </h3>")
    print("<p> Email: " + emailSafe + "</p>")
    print("<p> Username: " + usernameSafe + "</p>")
    print("<p> Potato Preference: " + radioSafe + "</p>")
    print("<p> Moment: " + textAreaSafe + "</p>")
    # writes the information in the USERS.txt
    fUSERSa.write(emailSafe + "\t" + usernameSafe + "\t" + passWordSafe + "\t" + radioSafe + "\t" + textAreaSafe + "\n")
else:
    print("<h3> If an error was mentioned above please hit the back button and try submitting the form again. </h3>")
