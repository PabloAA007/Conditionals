# 1. This will print "Oooo needs some work" since is claimin 10 > 10 iot is equal hence should be >= for it to work 
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("Oooo needs some work")

# 2.len is measuring the amount of letter is the word hence 3 < x, this wil prompt "Question 2 works!"
x = 5
y = 10
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")

# 3. This will print "You are of drinking age!" since 19 > 18
age = 19
if age > 18:
    print("You are of drinking age!")
else:
    print("Argggggh! You think you can hoodwink me, matey?! You're too young to drink!")

# 4. And conditional meaning both need to be righ. first is 8 >= 5 wich is true. Second variable 25 < 26. Both are right hence this will print "GOT QUESTION 4!" both questions are correct 
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 4!")
else:
    print("Oh good you can count")

# 5. First conditional 66 > 70 and 16 >= 18, this can't be both are false. Second 66 > 65 and 16 >= 18, this one can't be aso only one will be true. 66 > 60 and 16 >= 18 can't be as opnly one is true. Second one has two or conditions with and conditions within, first conditions 66 > 50 and 16 >= 18 can't be since one is false OR adult_permission = true and 66 > 50, both conditions are met hence this well print "Can ride bumper cars"
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
