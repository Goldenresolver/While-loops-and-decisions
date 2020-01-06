#Jason Polanco
#11/13/19
#This program get input for 3 tests and calculates
#an average and grade

import bobfile


#functions definitions
#return type: None
#parameters: None
#purpose: This function displays in an intro to the user
def PrintIntro():
    print("WELCOME TO THE FUNCTION PROGRAM!\n\n")



#return type: 1 string

#parameters: none

#purpose: This function prompts the user for a name
def GetName():
    # declare a local variable
    #string tempName
    # only declare and intialize when starting 
    tempName=""

    #prompt the user for tempName
    tempName= input("Enter your name: ")

    #return strng tempName
    return tempName

#return type: 1 int
#parameters: none
#purpose: This function prompts the user for an age and validates
#that the age is positive.

def GetAge():
    #declare and local variable
    #int tempAge
    tempAge=0

    while tempAge <=0:
            tempAge= int(input("Enter your age: "))

            if tempAge <=0:
                print("Invaild, Age must be positive.\n")
                
    return tempAge

#return type:1 float
#parameters: None
#purpose: This function prompts the user for a grade and validates that
#grade is between 0 and 100.
def GetGrade():
    #declare a local variable
    #float tempGrade
    tempGrade= -1.0

    while tempGrade < 0 or tempGrade > 100:
            tempGrade = float(input("Enter a grade: "))

            if tempGrade < 0 or tempGrade >100:
                print("Invalid. Grade must be between 0 and 100.\n")

    return tempGrade

#return type: 1 float
#parameters:
#purpose: This function calculates and returns the average of the
#three parameters that are passes to the function
def CalcAverage(num1,num2,num3):
    #Since nothing needs to be stored locally you can do the math directly
    #In the return statement
    
    return (num1+num2+num3/3)

#return type: 1 string
#parameters: 1 float
#purpose: This function returns the letter grade that
#corresponds with the user's numeric grade
# no need to declare and intilizing becuase we are passing varuiables
# from functions
def LetterGrade(numbergrade):
    if numbergrade >=90:
        return"A"
    elif numbergrade >=80:
        return "B"
    elif numbergrade >=70:
        return "C"
    elif numbergrade >= 60:
        return "D"
    else:
        return "F"
    

def main():

    #declare local variables
    #string userName
    userName=""
    #int userAge
    userAge = 0

    #float grade1,grade2,grade3
    grade1=grade2=grade3=0.0
    #float averageGrade=0.0
    averageGrade=0.0

    #invoke(call) PrintIntroFunction
    PrintIntro() #"stand alone" statement

    #call GetName function and store the results of the function in userName
    userName = GetName()

    #call GetAge function and store the results
    userAge= GetAge()

    #call GetGrade three times to store grade1,grade2 and grade 3
    grade1=GetGrade()
    grade1=GetGrade()
    grade1=GetGrade()

    # call CalcAverage to store the average of the three grades in averageGrade
    averageGrade = CalcAverage(grade1,grade2,grade3)
    #only use this for a one-time use only
    #print("Your average is", CalcAverage(grade1,grade2,grade3))

    #assign the correct letter grade to letter
    letter =LetterGrade(averageGrade)

    #display letter
    print("Your letter grade =", letter)

    #call DisplayUserInfo
    bobfile.DisplayStudentInfo(userName,userAge,averageGrade,letter)
    
    
    

main()
