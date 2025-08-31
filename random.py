import time 

name = input(" Enter your name : ")
print(f"Hello {name} welcome  . ")
print()
time.sleep(1)
word = 'secret'
guesses = ''
turn = 10
while turn > 0:
    failed = 0 
    for char in word : 
        if char in guesses : 
            print(char,end=" ")
        else : 
            print(" _ ",end = " ")
            failed += 1
    print()
    if failed == 0:
        print("You won the game ")
        break 
    guess = input("Enter a character : ")
    guesses +=guess 
    if guess not in word :
        turn -= 1  
        print("Wrong")
        print(f"You have {turn} turns to guess a word ")
    if turn == 0 :
        print("You lose the game . ")




