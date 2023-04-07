import random
count = 2
response = input("Wanna Roll A Dice?(YES/NO): ")
choice = input("Do you want CLASSIC DICE or NUMBERED DICE?(C/N): ")

def diceRoll():
    num = random.randint(1,6)
    print("Dice is Rolling...")
    print()
    print("[       ]")
    print("[  ",num,"  ]")
    print("[       ]")
    print()

def diceRollPattern():
    num = random.randint(1,6)
    if(num == 1):
        print("Dice is Rolling...")
        print()
        print("[       ]")
        print("[  ","•","  ]")
        print("[       ]")
        print()
    if(num == 2):
        print("Dice is Rolling...")
        print()
        print("[ ","•","    ]")
        print("[        ]")
        print("[    ","•"," ]")
        print()
    if(num == 3):
        print("Dice is Rolling...")
        print()
        print("[","•","    ]")
        print("[  ","•","  ]")
        print("[    ","•","]")
        print()
    if(num == 4):
        print("Dice is Rolling...")
        print()
        print("[","•"," ","•","]")
        print("[       ]")
        print("[","•"," ","•","]")
        print()
    if(num == 5):
        print("Dice is Rolling...")
        print()
        print("[","•"," ","•","]")
        print("[  ","•","  ]")
        print("[","•"," ","•","]")
        print()
    if(num == 6):
        print("Dice is Rolling...")
        print()
        print("[","•"," ","•","]")
        print("[","•"," ","•","]")
        print("[","•"," ","•","]")
        print()                

if(response == 'yes'):
     if(choice == 'c'):
        diceRollPattern()
     elif(choice == 'n'):
         diceRoll()   
     count -= 2
elif(response == 'no'):
    print("Thank You For Playing!") 
      

while count < 2:
    response2 = input("Press R to Roll Again, Press E to Exit: ")
    if(response2 == 'r'):
      if(choice == 'c'):
        diceRollPattern()
      elif(choice == 'n'):
        diceRoll()
    elif(response2 == 'e'):
        print("Thank You For Playing!") 
        count += 2           