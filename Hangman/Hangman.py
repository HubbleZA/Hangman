import random
import re

word = open(r"H:\OneDrive\Programme\Python for Everybody\Hangman\Hangman\Lists\words.txt","r")
listwords = word.readlines()
word.close()
listeasy =[]
listmed = []
listhard = []
listbad = []
guess_word_list = []
guessed_words = []
message_list = []
hang = 0
hangdiff = 0
again = "Y"

num_words = len(listwords)
number=0
#Splitting words based on their length
while True:
    sort_word = (listwords[number])
    wordlen = (len(sort_word))
    sort_word = sort_word[0:wordlen]
    sort_word = sort_word.upper()
    if len(sort_word) >= 4 and len(sort_word) < 7:
        listeasy.append(sort_word)
    else:
        if len(sort_word) >= 7 and len(sort_word) < 10:
            listmed.append(sort_word)
        else:
            if len(sort_word) >= 10:
                listhard.append(sort_word)
            else:
                listbad.append(sort_word)
    number += 1
    if number >= num_words:
        break
#setting words to uppercase
diffeasy = "easy"
diffmed = "medium"
diffhard = "hard"
diffeasy = diffeasy.upper()
diffmed = diffmed.upper()
diffhard = diffhard.upper()
while True:
    if again == "Y":
#clearing all lists and variables
        hang = 0
        guess_word_list = []
        guessed_words = []
#user input their difficulty choice
        while True:
            diff = input("Please enter a difficulty you would like to play on([e]asy/[m]edium/[h]ard): ")
            diff = diff.upper()
            if diff == diffhard or diff == "H":
                break
            else:
                if diff == diffeasy or diff == "E":
                    break
                else:
                    if diff == diffmed or diff == "M":
                        break
                    else:
                        print("You did not enter a valid response. Please try again")
                        continue
#choosing a word based on your difficulty
        if diff == diffeasy or diff == "E" :
            the_word = random.choice(listeasy)
            hangdiff = 6
        else:
            if diff == diffmed or diff == "M" :
                the_word = random.choice(listmed)
                hangdiff = 7
            else:
                if diff == diffhard or diff == "H" :
                    the_word = random.choice(listhard)
                    hangdiff = 8
                else:
                    print("Please enter the correct input")
                    exit()
#Saving Lists to text files
        with open(r'H:\OneDrive\Programme\Python for Everybody\Hangman\Hangman\Lists\listeasy.txt','w') as f:
            for item in listeasy:
                f.write("%s" % item)
        with open(r'H:\OneDrive\Programme\Python for Everybody\Hangman\Hangman\Lists\listmed.txt','w') as f:
            for item in listmed:
                f.write("%s" % item)
        with open(r'H:\OneDrive\Programme\Python for Everybody\Hangman\Hangman\Lists\listhard.txt','w') as f:
            for item in listhard:
                f.write("%s" % item)
        f.close()
        guess_num = 0
        the_word = the_word.strip()
        the_word_list = list(the_word)
        the_word_len = len(the_word_list)
#Putting word into a list
        while True:
            guess_word = the_word_list[guess_num]
            guess_word_list.append("-")
            guess_num += 1
            if guess_num >= the_word_len:
                break
            else:
                continue
        print("-" * 50)
        guess_word = "".join(guess_word_list)
        print("The word is: " + guess_word + " . The word is " + str(the_word_len) + " characters long.")
        guessed_words.sort()
        print("You have guessed the following letters: " + "".join(guessed_words))
        print("You have made " + str(hang) + "/" + str(hangdiff) + " errors. You have " + str(hangdiff-hang) + " guesses left")
        while True:
#Death if you make more than 5 errors
            if hang >= hangdiff:
                print("-" * 50)
                print("You have died!")
                print("The word is: " + the_word)
#would you like to play again
                while True:
                    print("-" * 50)
                    again = input("Would you like to play again(Y/N): ")
                    again = again.upper()
                    if not re.match(r'[y,n,Y,N]+',again):
                        print("Please enter Y or N")
                        continue
                    elif len(again) != 1:
                        print("Please enter Y or N")
                        continue
                    else:
                        break
                break
            else:
#message that you have won
                if guess_word_list == the_word_list:
                    print("-" * 50)
                    print("-" * 50)
                    print("-" * 50)
                    print(the_word + " is the word well done")
#Would you like to play again
                    while True:
                        print("-" * 50)
                        again = input("Would you like to play again(Y/N): ")
                        again = again.upper()
                        if not re.match(r'[y,n,Y,N]+', again):
                            print("Please enter Y or N")
                            continue
                        elif len(again) != 1:
                            print("Please enter Y or N")
                            continue
                        else:
                            break
                    break
                else:
#User input Letter(Making sure it is only 1 letter and an actual letter)
                    while True:
                        print("-" * 50)
                        letter = input("Please guess a letter from a to z : " )
                        letter = letter.upper()
                        if not re.match(r'[a-zA-Z]+', letter):
                            print("Please enter a letter")
                            continue
                        elif len(letter) !=1:
                            print("Please enter only 1 letter")
                        elif letter in guessed_words :
                            print("You have already guessed " + letter + " pick another letter")
                            continue
                        else:
                            break
#Seeing if letter is in the word
                    guess_num = 0
                    while True:
                        if guess_word_list[guess_num] == "-":
                            if the_word_list[guess_num] == letter:
                                guess_word_list[guess_num] = letter
                                guess_num += 1
                                message_list.append(1)
                            else:
                                guess_word_list[guess_num] = "-"
                                guess_num += 1
                                message_list.append(2)
                        else:
                            guess_num += 1
#checking if guessed letter is in the word and adding it to the guessed list
                        if guess_num >= the_word_len:
                            if 1 in message_list :
                                print("-" * 50)
                                print(letter + " is in the word!!")
                                message_list = []
                            else:
                                print("-" * 50)
                                print(letter + " is not in the word.")
                                hang += 1
                                message_list = []
                            guess_word = "".join(guess_word_list)
                            print("The word is: " + guess_word + " . The word is " + str(the_word_len) + " characters long.")
                            guessed_words.append(letter)
                            guessed_words.sort()
                            print("You have guessed the following letters: " + "".join(guessed_words))
                            print("You have made " + str(hang) + "/" + str(hangdiff) + " errors. You have " + str(hangdiff-hang) + " guesses left")
                            break
                        else:
                            continue
                    continue
    else:
#Thank you for playing
        print("-" * 50)
        print("-" * 50)
        print("-" * 50)
        print("-" * 50)
        print("-" * 50)
        print("-" * 50)
        print("-" * 50)
        print("Thank you for playing")
        wait = input("Press Enter to Exit")
        break
