import random
import string
from hangman_2 import words

def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = 6

    while len(word)>0 and lives >0:
        print('you have',lives,' lives left and you have used these letters:',' '.join(used_letter))

        word_list = [letter if letter in used_letter else '_' for letter in word]
        print('Current word:',' '.join(word_list))


        user_input = input('Guess a letter:').upper()

        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
                print('')
            else:
                lives = lives-1
                print('Your guess',user_input,'is not in the word. You have',lives,'guess remaining \n')

        elif(user_input in used_letter):
            print('You already guessed that letter.Guess something else')

        else:
            print('This is not a valid letter.')

    if lives==0 :
        print('you are dead. The word was ',word)
    else:
        print('YAY! you guessed the word')

if __name__ == '__main__':
    hangman()







