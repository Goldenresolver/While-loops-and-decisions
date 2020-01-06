#Jason Polanco
# 10/25/19
#chap 5 programming excerises # 3

#A program that accepts an exam score as input and prints output
# out the corresponding grade

# declare and intialize variables
fName =""
grade = 0

#declare main
def main():

#Intro
    print("Welcome to grading program!")
    fName=input("\nPlease enter your name: ")
    grade = int(input("\nPlease enter exam score: "))
    


#use a decision structure to determine grades that corelate with exam scores.

    if grade >=90 and grade <=100:
        print("Your letter grade is an A,great job!")

    elif grade >=80 and grade <=89:
           print("Your letter grade is a B,good!")

    elif grade >= 70 and grade<= 79:
            print("Your letter grade is a C, Study a bit more!")

    elif grade >= 60 and grade <= 69:
             print("Your letter grade is a D, Study Harder!")

    else:
        print("Your letter grade is a F, You failed the exam!")
        main()


        
main()
