##Adam Cohill
#M02 Programing assignment
#4.1,4.2,6.1,6.2,6.3

#4.1
secret = 8
guess = 9

def guessMac():

    if secret > guess:
        print ("Too low")
    elif secret < guess:
        print("Too high")
    else:
        print("You got it!")

#4.2
small = True
green = False

def fruitMac():
    if small and not green:
        print("Its a cherry")
    elif small and green:
        print("Its a pea")
    elif not small and not green:
        print("Its a pumpkin")
    else:
        print("Its a watermelon") 

#6.1
def TTDloop():
    print(list(range(3,-1, -1)))
        
#6.2
def guessMac2():
    guess_me = 7
    number = 1
    while True:
        if number < guess_me:
            print("Too low")
            number += 1
        elif number == guess_me:
            print ("Found it")
            break
        else:
            print("OOPS")
            break    

def TTDloop2():
    guess_me = 5
    for number in range (10):
        if number < guess_me:
            print("Too low!")
        elif number == guess_me:
            print("GOT IT!!")
            break
        elif number > guess_me:
            print("oops")
            break      
        
    
                
    
    
guessMac()                
fruitMac()
TTDloop()
guessMac2()
TTDloop2()