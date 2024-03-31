# Adam Cohill
# sdev220 M02 Lab if... else and while
#Purpose:  ask for and accept a student's last name.
#quit processing student records if the last name entered is 'ZZZ'.
#ask for and accept a student's first name.
#ask for and accept the student's GPA as a float.
#test if the student's GPA is 3.5 or greater and, 
#if so, print a message saying that the student has made the Dean's List.
#test if the student's GPA is 3.25 or greater and, 
#if so, print a message saying that the student has made the Honor Roll.
#Your header comments need to contain
#Your name
#The file name for your app
#A brief description of what your app will do


while True:
    Lname = input("Input last name or ZZZ to QUIT: ")
    if Lname == "ZZZ":
        break
    
    Fname = input("Input your first name: ")    
    GPA = float(input("Input your GPA: "))
    if (GPA >= 3.5):
        print("You made the deans list!!")
        
    elif (GPA >= 3.25):
        print("You made the honor roll!!")
    
    else:
        print("DO BETTER!!")
        