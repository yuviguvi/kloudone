
import random
words= ("girl",
       "boy",
       "world",
       "pen",
       "chair",
       "glass",
       "java",
       "cab",
        "fire",
        "god",
        "hack",
        "work",
         )
notwords=("rigl",
          "yob",
          "dlrow",
          "nep",
          "riach",
          "ggals",
          "avaj",
          "bac",
          "irfe",
          "dog",
          "cahk",
          "rowk",)
          
crctword=random.choice(words)
if crctword==words[0]:

    i=0

elif crctword==words[1]:

    i=1

else:

    i=2

great=crctword

findword=""

while crctword:
    var=random.randrange(len(crctword))

    findword+=crctword[var]

    crctword=crctword[:var]+crctword[(var+1):]
print(

    """

         FINDING WORD GAME!!

"""

)
print("GAME START :", findword)
user=input("\nFIND ANSWER: ")
a=0
while user!=great and user!="":
    print("WRONG")
    user=input("FIND ANSWER:")
    a+=1

while user!=great and user!="":
    user=input("FIND ANSWER:")
    
if user==great:

     

    print("CORRECT")

else:

    print("WRONG!")
    a+=1
print("**************GAME OVER**************")
input("\n\npress Enter to exit")
