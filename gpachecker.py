"""
Joseph Feldman
GPA Checker
This app will ask students for information and determine if they have made the Dean's List or the Honor Roll.
"""

while True:

    lastname = input("What is your last name? ")
    
    if lastname != "ZZZ":
        firstname = input("What is your first name? ")
        gpa = float(input("What is your GPA? "))

    else:
        exit()

    if gpa == 3.5 or gpa > 3.5:
        print(firstname + " " + lastname + ", you have made the Dean's List.")
    
    elif gpa == 3.25 or gpa > 3.25 and gpa < 3.5:
        print(firstname + " " + lastname + ", you have made the Honor Roll.")
    
    else:
        print(firstname + " " + lastname + ", you should study more.")