# print("this is a sample string")

# name = "Zen"
# print("My name is", name)

# name = "Zen"
# print("My name is " + name)

# print("Hello " + 42)			# output: TypeError
# print("Hello " + str(42))		# output: Hello 42

# total = 35
# user_val = "26"
# # total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61
# print(total)

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

# Practice Challenge: Correct the errors!
# first_name = "Alana"
# last_name = "Da Silva"
# age = 36
# profession = "Software Developer"
# years_experience = 5
# greeting = "Hello my name is " + first_name + " " + last_name
# print(greeting)
# # Desired output: Hello my name is Alana Da Silva
# print("I am " + str(age) + " years old") 
# # Desired output: I am 36 years old
# print("I work as a {}.".format(profession))
# # Desired output: I work as a Software Developer.
# exp_string = "I have worked in the field for {} years."
# print(exp_string.format(years_experience))
# # Desired output: I have worked in the field for 5 years.
# print("I started in the field when I was " + str(age - years_experience) + " years old.")
# # Desired output: I started in the field when I was 31 years old.

# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27

# x = "hello world"
# print(x.title())
# # output:
# "Hello World" # .title capitalizes the first letter of each word

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)

# drawers = ["documents", "envelopes", "pens"]
# # access the drawer with index of 0 and print value
# print(drawers[0])  #prints documents
# # access the drawer with index of 1 and print value
# print(drawers[1]) #prints envelopes
# # access the drawer with index of 2 and print value
# print(drawers[2]) #prints pens
# # replace "documents" with "tchotchkes"
# drawers[0] = "tchotchkes"
# print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
# # stores the value "tchotchkes" in a temporary variable.
# top_contents = drawers[0]
# # Replaces the value at index 1
# # with whatever value is stored at index 0
# drawers[1] = drawers[0]
# print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

# # play around with the drawers!
# drawers = ['documents', 'envelopes', 'pens']
# # Print the second value from the list (envelopes)
# print(drawers[1])
# # Change "pens" to "useless manuals"
# drawers[2] = 'useless manuals'
# print(drawers)
# # Change the first value to whatever is the second value
# drawers[0] = drawers[1]
# print(drawers)
# # What should the list look like now?
# # Print the list! Does it match your prediction? Yep!

# nums = [1,2,3,4,5]
# # Challenge: Append some values to the list!
# nums.append(99)
# print(nums)
# nums.append(143)
# print(nums)
# # Note - append can only take one value it seems...

# words = ["start","going","till","the","end"]
# # Sub-ranges (portions) of the list
# print(words[1:]) # prints ['going', 'till', 'the', 'end'] (Seems to be inclusive of number if on the left of :)
# print(words[:4]) # prints ['start', 'going', 'till', 'the']  (Seems to be exclusive of number if on the right of :)
# print(words[2:4]) # prints ['till', 'the']
# # Making a copy of a list
# copy_of_words = words[:] # THIS IS SUPER USEFUL & EASY when copying lists!
# copy_of_words.append("dojo") # only appends to the copy
# print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
# print(words) # prints ['start', 'going', 'till', 'the', 'end']

# my_list = [1, 'Zen', 'hi']
# print(len(my_list))
# # output
# 3

# x = 12
# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")
# # because x is not greater than 50, the second print statement is the only one that will execute
# x = 55
# if x > 10:
# 	print("bigger than 10")
# elif x > 50:
# 	print("bigger than 50")
# else:
# 	print("smaller than 10")
# # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
# if x < 10:
# 	print("smaller than 10")
# # nothing happens, because the statement is false   

# for i in range(5):
#     print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# for i in range(2, 7):
#     print(i)
#Output:
# 2
# 3
# 4
# 5
# 6

# for i in range(2, 16, 3):
#     print(i)
# Output:
# 2
# 5
# 8
# 11
# 14

# for x in range(0, 10, 2):
#     print(x)
# # output: 0, 2, 4, 6, 8
# for x in range(5, 1, -3):
#     print(x)
# # output: 5, 2

# # Challenge: Write a for loop to print all integers from 1 to 20, including 20.
# for x in range(1, 21):
#     print(x)

# Looping Over Lists & Strings

# For Loops through Strings
# Since a loop can be used on any sequence, you can access each value of a string individual with loop.
# for x in 'Hello':
#     print(x)
# # output: 'H', 'e', 'l', 'l', 'o'

# # For Loops through Lists
# # If we want to iterate through a list, we could use the range function and send in the length of the list as the stopping value, but if we are not interested in the index values and want to just see the values of each item in the list in order, we can actually loop to get the values of the list directly!
# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz
    
# # OR 
    
# for v in my_list:
#     print(v)
# # output: abc, 123, xyz

# countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]
# # Challenge 1: Fix the range!
# for integer in range(0, len(countries)):
# # Challenge 2: print the index here
#     print("Index:", integer)
# # Challenge 3: print the country here
#     print("Country:", countries[integer])
# # Looping over values only...
# # Challenge 4: print the country here
# for country in countries:
#     print("Country: " + country)

# for count in range(0,5):
#     print("looping =", count)

# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1

# For Loops through Strings
# for x in 'Hello':
#     print(x)
# # output: 'H', 'e', 'l', 'l', 'o'

# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz
# # OR 
# for v in my_list: QUESTION: IS "v" a built-in for python?
#     print(v)
# # output: abc, 123, xyz

# While Loops
# While loops are another way of looping while a certain condition is true.
# Remember this for loop?
# for count in range(0,5):
#     print("looping =", count)
# # We can rewrite it as a while loop:
# # count = 0
# while count <= 5: #ACTUALLY NEED TO BE <5
#     print("looping =", count) 
#     # *WAS STUCK IN NEVERENDING LOOP!!! NOT SURE WHAT HAPPENED OR HOW TO KILL IT*
#     # count += 1

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

# # Example of BREAK
# for val in "string":
#     if val == "i":
#         break
#     print(val)
# # output: s, t, r
# # Notice that when the loop got to the letter "i", we stopped looping.

# # Example of CONTINUE
# for val in "string":
#     if val == "i":
#         continue
#     print(val)
# # output: s, t, r, n, g
# # notice, no i in the output, but the loop continued after the i

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
#     if y == 0:
#         break
# else:		# only executes on a clean exit from the while loop (i.e. not a break)
#    print("Final else statement")
# # output: 3, 2, 1

# # Functions
# def add(a,b):	# function name: 'add', parameters: a and b
#     x = a + b	# process
#     return x	# return value: x
# # #tested below, it works!
# # print(add(3,6))
# # OR
# new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
# print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

# def say_hi(name):
#     print("Hi, " + name)
# # invoking the function 3 times, passing in one argument each time
# say_hi('Michael')
# say_hi('Anna')
# say_hi('Eli')

# def say_hi(name):
#     return "Hi " + name
# greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
# print(greeting) # this will output 'Hi Michael'

# def add(a, b):
#     x = a + b
#     return x
# sum1 = add(4,6)
# sum2 = add(1,4)
# sum3 = sum1 + sum2
# print(sum1)
# print(sum2)
# print(sum3)

# # Challenge 1:
# #   Fill in the missing code for the full_name function.
# #   Be sure to add the 2 parameters (and name them appropriately)
# #   Return the full name to get the desired output!
# def full_name(first,last):
#     print(first, last)
# name1 = full_name("Eddie", "Aikau")
# print(name1) # should print Eddie Aikau # WHY IS THIS SAYING "NONE"?

# # Challenge 2: 
# #   Call the function again using your own name and print the results!
# name2 = full_name("Izzy", "Murillo")
# print(name2) # WHY IS THIS SAYING "NONE"?

# # set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
# be_cheerful() # output: good morning (repeated on 2 lines)
# be_cheerful("tim")# output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")# output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)# output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)# output: good morning michael (repeated on 5 lines)
# Note: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")# output: good morning kb (repeated on 3 lines)

# def multiply(num_list, num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # # output:
# # >>>[2,4,10,16]

# def multiply(num_list, num): #don't go inside the function until the function is called
# a = [2,4,10,16]
# b = multiply(a,5) # now our function executes; what is a function call equal to?
# print(b) # and the resulting value is printed

# def multiply(num_list, num): #QUESTION#
#     print(num_list, num)
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # # output:
# # >>>[2,4,10,16] 5
# # >>>[2,4,10,16]

# def multiply(num_list,num):  #QUESTION#
#     print(num_list, num)
#     for x in num_list:
#         print(x)
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # # output:
# # >>>[2, 4, 10, 16] 5
# # >>>2
# # >>>4
# # >>>10
# # >>>16
# # >>>[2, 4, 10, 16]

# def multiply(num_list,num):
#     print(num_list, num) # output should be [2,4,10,16] 5
#     for x in num_list:
#         print(x)
#         x *= num
#         print(x)
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # # output:
# # >>>[2,4,10,16] 5
# # >>>2
# # >>>10
# # >>>4
# # >>>20
# # >>>10
# # >>>50
# # >>>16
# # >>>80
# # >>>[2, 4, 10, 16]

# def multiply(num_list,num):
#     print(num_list, num) # output should be [2,4,10,16] 5
#     for x in num_list:
#         print(x)
#         x *= num
#         print(num_list)
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # # output:
# # >>>[2, 4, 10, 16] 5
# # >>>2
# # >>>[2, 4, 10, 16]
# # >>>4
# # >>>[2, 4, 10, 16]
# # >>>10
# # >>>[2, 4, 10, 16]
# # >>>16
# # >>>[2, 4, 10, 16]

# def multiply(num_list,num):
#     for x in range(len(num_list)):
#         num_list[x] *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # # output:
# # >>>[10,20,50,80]

# #literal notation
# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# print(person)
# # Create a another person dictionary called person_2 and print it to the terminal
# person2 = {"first": "Izzy", "last": "Murillo", "age": 26, "is_organ_donor": True}
# print(person2)
# capitals = {} #create an empty dictionary then add values
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# print(capitals) # output > {'svk': 'Bratislava', 'deu': 'Berlin', 'dnk': 'Copenhagen'}
# # Add 2 key-value pairs to this dictionary.
# capitals["phi"] = "Manila"
# capitals["spn"] = "Barcelona"
# # print the capitals dictionary to see how it changed!
# print(capitals)
# print(person["first"])
# print(person["age"])
# print(person2["first"])
# print(capitals["phi"])
# value_removed = capitals.pop("spn")
# print(capitals)
# del capitals["phi"]
# print(capitals)
# new_info = capitals.get("deu")
# print(new_info)
# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"
# # Changes person's "last" value to "Bobada"
# person["last"] = "Bobada"
# print(person)

# countries_so_far = {"Mexico": 1, "Morocco": 1}
# new_visits = ["Albania", "Mexico", "Togo", "Morocco"]
    
# # To add Albania to the list
# countries_so_far["Albania"] = 1
# # To add 1 to the Mexico tally
# countries_so_far["Mexico"] += 1 # Changes Mexico tally to 2!
# # your code here to finish updating your travel log!
# countries_so_far["Togo"] = 1
# countries_so_far["Morocco"] += 1
# print(countries_so_far)

# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(each_key)
# # output: name, language

# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(my_dict[each_key])
# # output: Noelle, Python


## **********************LOOPING THROUGH DICTIONARIES - HELPFUL!!! ***************

# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#      print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#      print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#      print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}
print(users[0]["last"]) # prints Lovelace
print(resume_data["skills"][1]) # back-end
print(users[2]["first"]) # Eric

