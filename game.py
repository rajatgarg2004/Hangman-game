import random   
def hangman(life):    
    print("\nWrong guess\n")
    if life==4:
        print('______\n|   0\n|\n|\n|\n|______\n')
    elif life==3:
        print('______\n|   0\n|   |\n|\n|______\n')
    elif life==2:
        print('______\n|   0\n|  \|/\n|\n|\n|______\n')
    elif life==1:
        print('______\n|   0\n|  \|/\n|   |  \n|\n|______\n')
    else:
        print('______\n|   0\n|  \|/\n|   |  \n|  / \   \n|______\n')
  
def decision():
    print("Do you want to play again? Y/N")
    d = input()
    if d =='Y':
        play()
    elif d == 'N':
        print("Bye Bye")
    else:
        print("Please type Y or N ")
        decision()

def check(x_letters,x_letter):
    flag=0
    for i in x_letters:
        if i==x_letter:
            flag=1
    if flag==1:
        return False
    else:
        return True
        
        
def Guess(dashes,words):
    end,life =0,4
    wrong_l = []
    all_letters=[]
    while(end==0):
        flag=0
        print("Guess a letter")
        letter = input()  
        if check(all_letters,letter):
            all_letters.append(letter)
        else:
            print("You have already typed this letter, Choose another letter")
        
        for i in range(0,len(words)):
            if letter == words[i]:
                dashes[i] = words[i]
                flag=1                
        if dashes==words:
            print("Congratulations!!! You guessed it right, The word was " + ''.join([str(elm) for elm in words]))
            end=2
            decision()
            break                            
        elif flag==0:
            hangman(life)
            wrong_l.append(letter)
            
            print("Wrong letters: "+ ','.join([str(elem) for elem in wrong_l]))
            if life==0:
                print("You lost!!!")
                end=2
                print("The word was " + ''.join([str(elem) for elem in words]))
                decision()
                break
            life=life-1
            print(' '.join([str(elem) for elem in dashes]) +"\n")            
        else:
            print(' '.join([str(elem) for elem in dashes]))
            print("\nWrong letters: "+ ','.join([str(elem) for elem in wrong_l]))
            
import wordList as wL                  
def play():
    word = list(random.choice(wL.final_list))
    dash = [ "_" for x in range(0,len(word)) ]
    for i in dash:
        print(i,end=" ")
    Guess(dash,word)
  
name = input("Enter Your Name: ")
print("Hi, " + name + " Let's play Hangman.\n ")
print("   ******RULES******\n  1. A word will be selected randomly.\n  2. You have to guess the word by typing one letter in each turn and you have 4 lives.\n  3. After 4 wrong guesses, the man will be hung and you'll lose the game.\n  4. If you type the wrong letter again, you'll lose another life.\n  5. If you type the right alphabet again, You will not lose a life.\n  6. Press 1 to continue or 2 to exist ")
num = int(input())
if num==1:
    play()
else:
    print("Bye, "+ name)
