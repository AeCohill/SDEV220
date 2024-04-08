#7.4 Make a list called things with these three strings
#as elements: "mozzarella", "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]
#7.5 Capitalize the element in things that refers to a person 
#and then print the list. Did it change the element in the list?
## yes it did
things[1] = things[1].capitalize()
print(things)
 #7.6 Make the cheesy element of things all 
 # uppercase and then print the list.
for i in range(len(things[0])):
    things[0] = things[0].upper()

print(things)
##7.7 Delete the disease element from things,
##collect your Nobel Prize, and print the list.
del things[2]
print(things) 
## 9.1 Define a function called good() 
# that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good():
    list = ['Harry', 'Ron', 'Hermione']
    print(list)
good()
#9.2 Define a generator function called get_odds()
# that returns the odd numbers from range(10). 
# Use a for loop to find and print the third value returned.
def get_Odds(first=0, last=11, step=1):
    ranger = range(first, last, step)
    odd_count = 0
    for x in ranger:
        if x % 2 != 0:
            odd_count += 1
            if odd_count == 3:
                print(x)
                break

get_Odds()




