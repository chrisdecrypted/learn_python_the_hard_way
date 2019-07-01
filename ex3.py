# Learn Python the Hard W,ay
# Accessed from https://learnpythonthehardway.org/python3/
# Exercise 3: Numbers and Math
# Christopher Murray
# 6/30/2019

print("I will now count my chickens:")

# order of operations PEMDAS
# 'really' PE(M&D)(A&S)
print("Hens", 25 + 30 / 6)
# The first action here is the division of 30/6 (5). Then 25+5 = 30.0
# Becuase it is a division symbol isntead of the modulus the number is made a float AKA double 
print("Roosters", 100 - 25 * 3 % 4)     
# 25 * 3 = 75
# 75 % 4 = 3 

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 -7?", 5 -7)

print("Oh, that's why it's False.")

print ("How about some more.")  

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)