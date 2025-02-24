print("welcome to my Quiz Game \n Interesting game to play")
Player = input("Do you want to play the game ?(Yes/No) \n")
if Player.lower() !='yes':
    print("Goodbye!")
    quit()
else:
    print("Welcome to my Quiz Game")

name_of_player = input("enter the name:")
print("Lets start the game", name_of_player)
score = 0

Q1= input("what is CPU stands for?")
if Q1.lower()=='central processing unit':
    print("correct")
    score+=1
else:
    print("wrong")

Q2= input("what is GPU stands for?")
if Q2.lower()=='graphical processing unit':
    print("correct")
    score+=1
else:
    print("wrong")

Q3= input("What is RAM stands for?")
if Q3.lower()=='random access memory':
    print("correct")
    score+=1
else:
    print("wrong")

Q4= input("What is ROM stands for?")
if Q4.lower()=='read only memory':
    print("correct")
    score+=1
else:
    print("wrong")

Q5= input("Mouse is an input device or output device??")
if Q5.lower()=='input device':
    print("correct")
    score+=1
else:
    print("wrong")

print("you got the"+ str(score) +"correct answer")
print("you gyot the"+ str((score/5)*100) + "correct answer")

print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")