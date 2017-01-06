print("Hello and welcome to Skybank")
name = input("Please enter your first name: ") #First name input
name = name+" "+input("Please enter your second name: ") #Second name input

print("Welcome",name) #Full name input
print("Please enter your 3 digit pin. e.g. ***")
pin = 123 #Pin code
attempt = 0
gotit = False


while gotit == False:
    guess = int(input("Please enter your pin:"))
    print("------------------------------")

    if guess == pin:
        print("Correct, Welcome",name ,"what service would you like?")
        print("------------------------------")
        gotit = True
    else:
        attempt =+1
        print("Wrong", attempt, "guesses left")
        print("------------------------------")
        if attempt == 3:
            gotit = True
            print("Account Locked")
            print("------------------------------")



