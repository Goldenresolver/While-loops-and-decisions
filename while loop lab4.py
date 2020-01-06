#Jason Polanco
#11/8/19
# A program that prompts user for age and marital stauts, using a menu
# Intro
# declare and intialize variables
#use while loops for input validation
#Use a decision structure

def main():
    uAge=0
    uMarried=int(2)
    uSingle= int(1)
    AUTOAGE=int(25)
    LEGALAGE= int(16)
    userInput=0

    less25NoMarry=float(800.00)
    less25YesMarry = float(700.00)
    great25NoMarry= float(500.00)
    great25YesMarry=float(450.00)

    print("\nWelcome to Broward College Auto insurance")

    

    print("""\nPlease choose your maritial status:
            1) Married
            2)Single""")

    uAge= int(input("\nPlease enter your age: "))

    userInput=int(input("\nPlease select one of the options: "))

    
    if uAge <= LEGALAGE:
    
        if uAge <=AUTOAGE:
            if userInput==uSingle:
                print(" You qualify here is your rate",less25NoMarry)

            else:
                print("Your rate is", less25YesMarry)

    elif uAge >=AUTOAGE:
            if userInput==uMarried:
                print("Your rate is",great25YesMarry)

            else:
                print("Your rate is", great25NoMarry)

    else:
        print("Age is not legal for insurance nor for driving")


main()

























    
    
    
    


    
