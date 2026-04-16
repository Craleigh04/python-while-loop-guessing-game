secret_number = 777 
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number= int(input("Try to guess the hidden number: HINT(its a positive integer)"))

while number != 777:
    if number % 2 == 0:
        print ("You entered an even number")
        
    else:
            print ("You entered an odd number")
    
    print ("Ha ha! You're stuck in my loop!") 
    number= int(input("Try again to guess the hidden number: HINT(its a positive integer)"))
    
print ("Well done, muggle! You are free now.")