num1 = 42 #- variable declaration - Numbers
num2 = 2.3 #- variable declaration
boolean = True # Boolean
string = 'Hello World' # Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionary
fruit = ('blueberry', 'strawberry', 'banana') # Tuples
print(type(fruit)) #- type check
print(pizza_toppings[1]) # List - access value
pizza_toppings.append('Mushrooms') #List - add value
print(person['name']) # Dictionary - access value
person['name'] = 'George' # Dictionary - add value
person['eye_color'] = 'blue' # Dictionary - add value
print(fruit[2]) # Tuples - access value

if num1 > 45: # conditional - if
    print("It's greater")
else: # conditional - else
    print("It's lower")

if len(string) < 5: # conditional - if - length check
    print("It's a short word!")
elif len(string) > 15: # conditional - else if - length check
    print("It's a long word!")
else: # conditional - else
    print("Just right!")

for x in range(5): # for loop - stop
    print(x)
for x in range(2,5): # for loop - start - stop
    print(x)
for x in range(2,10,3): # for loop - start - stop - increment
    print(x)
x = 0 # variable declaration - number
while(x < 5): # while loop - stop
    print(x)
    x += 1 # increment

pizza_toppings.pop() # List - delete value
pizza_toppings.pop(1) # List - delete value

print(person) # Dictionary - access value
person.pop('eye_color') # Dictionary - delete value
print(person) # Dictionary - access value

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional - if
        continue #continue
    print('After 1st if statement')
    if topping == 'Olives': # conditional - if
        break #break

def print_hello_ten_times(): #function
    for num in range(10): # for loop - stop
        print('Hello')

print_hello_ten_times() 

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)