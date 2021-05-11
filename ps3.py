# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
from copy import deepcopy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


wordlist = load_words()


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    words = word.lower()
    y = 0
    for letters in words:
        # print(letters)
        for v in SCRABBLE_LETTER_VALUES:
            if letters == v:
                y = y + (SCRABBLE_LETTER_VALUES[v])
    # print(y)

    value = (7 * len(word)) - (3 * (n - len(word)))
    # print(value)
    temps = 0
    if value > 1:
        x = y * value
        # print("x: "+ str(x))
        # print("bad")

    else:
        x = y * 1
        # print(x)
        # print("good")

    return x


# (get_word_score("weed",6))


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hands):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    string = ""
    for letter in hands.keys():
        for j in range(hands[letter]):
            string = string + " " + letter
    return string

    # print()                              # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
# print(display_hand({'a': 1, 'j': 1, 'e': 1, 'f': 1, 'r': 1, 'x': 1, '*': 1}))

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))
    y = "*"

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n - 1):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(n - 1, n):
        x = y
        hand[x] = hand.get(x, 0) + 1

    return hand


# print(deal_hand(7))

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    words = word.lower()
    new_hand = deepcopy(hand)
    # print(hand)
    # print(new_hand)
    for letters in words:
        for k in new_hand:
            if k == letters and new_hand[k] > 0:
                new_hand[k] -= 1
    return new_hand
    # for k in new_hand:
    #     if new_hand[k] == 0:
    #          del new_hand[k]
    # return (new_hand)


# print(update_hand( {'j':2, 'o':1, 'l':1, 'w':1, 'n':2} , "JOlly"))


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    hand2 = deepcopy(hand)  # copy and lowercase dictionary
    words = deepcopy(word)
    words2 = words.lower()  # copy and lowercase word
    # print(words)
    y = 0
    y2 = 0
    vowels = ["a", "e", "i", "o", "u"]
    if words2 in word_list:
        for letters in words2:
            for k in hand2:
                if k == letters:
                    hand2[k] -= 1
                    y += 1
                    if hand2[k] < 0:
                        # print(hand2)
                        # print(y)
                        return False
    else:  # words2 not in word_list
        for each_word in word_list:
            if len(each_word) != len(words2):
                pass
            elif len(each_word) == len(words2):
                for i in range(len(words2)):
                    # print(words2)
                    # print(each_word)
                    if words2[i] == each_word[i]:
                        # print(each_word)
                        # print(words2[i])
                        y2 += 1
                        # print(y2)
                    elif words2[i] == "*" and each_word[i] in vowels:
                        y2 += 1

                    else:
                        continue
                if y2 == len(words2):
                    for letters in words2:
                        for k in hand2:
                            if k == letters:
                                hand2[k] -= 1
                                y += 1
                                if hand2[k] < 0:
                                    return False
                    return True
                else:
                    y2 = 0

                    #
            # if each_word[0:x] == words2[0:x] and each_word[x+1:] == words2[x+1:]:
            # #
            # #     #if each_word[x] in vowels:
            # #     #print(each_word)
            # #     #print(each_word[x])
            # #     if (each_word[x]) not in vowels:
            # #         #print(each_word[x])
            # #         return False
            # #     else:
            # #         return True
            # #     #new_matches.append(each_word)
            # # elif each_word[0:x] == words2[0:x]:
            # #     print(each_word[x])
            # #     print('hit')

    if y == len(word):
        # print(y)
        return True
    else:
        # print(y)
        return False


# print(is_valid_word('oar',{'o': 1, 'o': 1, 'o': 1, 'i': 1, 'r': 1, 'a': 1, '*': 1},wordlist))

def calculate_handlen(hand):
    x = len(hand)
    return x


# print(calculate_handlen({'n': 1, 's': 1, '*': 1, 't': 1, 'o': 1, 'w': 1, 'e': 2}))

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # print(hand)

    y = 0

    while all(x == 0 for x in hand.values()) != True:
        print("Current Hand:" + str(display_hand(hand)))
        word = (input("Enter word, or " + " !! " + " to indicate that you are finished:").strip())

        if word == "!!":
            print("Total Score: " + str(y))
            return y
            break

        elif is_valid_word(word, hand, word_list) == True:
            hand = (update_hand(hand, word))
            print("Current Hand:" + str(display_hand(hand)))
            n = calculate_handlen(hand)
            points = (get_word_score(word, n))
            y = y + points
            print(str(word) + " earned " + str(points) + ". Total: " + str(y) + " points")
            # return y

        elif is_valid_word(word, hand, word_list) == False:
            hand = (update_hand(hand, word))
            print("That is not a valid word. Please choose another word.")
        else:
            print("Please enter a letter in the hand")
    print()
    print("Ran out of letters. Total Score: " + str(y))
    return y


# play_hand(deal_hand(7), wordlist)

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not muteta hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)

    """
    alletters = VOWELS + CONSONANTS
    # print(alletters)
    # print(hand)
    if letter not in hand.keys():
        pass
        # substitute_hand(hand, letter)

        # return hand

    elif letter in hand.keys():  # if letter in the hand
        x = alletters.replace(letter, '')  # this function takes out the the letter that the use inputted
        # print(x)
        matching = ""
        for letters in hand.keys():
            for chars in x:
                if letters == chars:
                    matching = matching + chars
        # print(matching) # takes out the letters that are in the hand

        for char in matching:
            x = x.replace(char, "", 1)
        # print('x = '+str(x))
        randoml = random.choice(x)
        # print(randoml)

        # a = hand
        for letters in hand.keys():
            if letters == letter:
                a = hand
                a[randoml] = a.pop(letters)
        # print(a)
        return a
        # x = random.choice(allletters)

        # for letters in hand.keys():
        #     print(letters)

        # return x
    # for letters in hand.keys():
    #     if letters == letter:
    #         random.choice


# print(substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l'))

def replay_loop(replay, hand, word_list):
    while replay > 0:
        replays = input("Would you like to replay the hand:")
        if replays == "yes":
            print(hand)
            y3 = play_hand(hand, word_list)
            replay -= 1
            return y3
        elif replays == "no":
            break
        else:
            print("Please input yes or no")
    return -1


def subs_loop(subs, hand, word_list):
    while subs > 0:
        print("Current hand: " + str(display_hand(hand)))
        letter = input("Would you like to substitute a letter:").strip(" ").lower()
        if letter == "yes":
            new_letter = (input("Which letter would you like to replace:").strip(" ")).lower()
            x2 = (substitute_hand(hand, new_letter))
            if x2 == None:
                print("Please enter a letter in the hand!")
                continue
            else:
                #print(x2)
                subs -= 1
                score = play_hand(x2, word_list)
                return score
        elif letter == "no":
            print("you suck")
            break
        else:
            print("Please input yes or no")
    return -1


def play_game(word_list):
    try:
        print('''This game is like words with friends without the friends.
In this game the computer will generate a series of letters and you goal is create words that will produce the most points!
Each hand has a at least 3 vowels and 3 constants and one letter is an asterisk *. The asterisk can be used as a free letter
but you can only be used to replace a vowel when entering a hand. You are also given one replay to redo a hand and one substitution 
through out the whole game. 
 ''')
        number_hands = int(input("Enter total number of hands:"))

        # print(number_hands)
        total_score = 0
        replay = 1
        subs = 1

        while number_hands > 0:
            hand = (deal_hand(HAND_SIZE))
            x = str(display_hand(hand))
            print("Number of Hands: " + str(number_hands))
            print("Number of Replays: " + str(replay))
            print("Number of Substitution: " + str(subs))
            print("Current Hand: " + x)
            print("Current Score: " + str(total_score))
            # print(y)
            # if replay == 1 and subs == 1:
            if subs == 0 and replay == 0:
                print("0")
                score1 = play_hand(hand, word_list)
                number_hands -= 1
                total_score = total_score + score1
            elif subs == 0 and replay == 1:
                print("1")
                score1 = play_hand(hand, word_list)
                replay_score = replay_loop(replay, hand, word_list)
                if replay_score == -1 :
                    total_score = total_score + score1
                    #print("Current Score " + str(total_score))
                    number_hands -= 1
                else:
                    if replay_score > score1:
                        total_score =  total_score + replay_score
                        #print("Current Score " + str(total_score))
                        replay -= 1
                        number_hands -= 1
                    else:
                        total_score = total_score + replay_score
                        #print("Current Score " + str(total_score))
                        replay -= 1
                        number_hands -= 1
            elif subs == 1 and replay == 0:
                print("2")
                subs_score = subs_loop(subs, hand, word_list)
                if subs_score == -1:
                    score1 = play_hand(hand, word_list)
                    number_hands -= 1
                    total_score = total_score + score1
                    #print("you are here ")
                    #print("Current Score " + str(total_score))
                else:
                    number_hands -= 1
                    subs -= 1
                    total_score = total_score + subs_score
                    #print("Current Score " + str(total_score))

            elif subs == 1 and replay == 1:
                print("3")
                subs_score = subs_loop(subs, hand, word_list)
                if subs_score == -1:     # if the user says no
                    score1 = play_hand(hand, word_list)
                    #total_score = total_score + score1
                    #print("you are here ")
                    replay_score = replay_loop(replay, hand, word_list) # ask the user to replay
                    if replay_score == -1:
                        total_score = total_score + score1
                        #print("Current Score " + str(total_score))
                        #print("first situation")
                    elif subs_score > replay_score:
                        total_score = total_score + replay_score
                        #print("Current Score " + str(total_score))
                        replay -= 1
                    else:
                        total_score = total_score + replay_score
                       # print("Current Score " + str(total_score))
                        #print("second situation")
                        replay -= 1
                    number_hands -= 1
                else:
                    subs -= 1 # if they dont want to sub
                    replay_score = replay_loop(replay, hand, word_list)
                   # print("current Score " + str(total_score))
                    if replay_score == -1:
                        total_score = total_score + subs_score
                        #print("Current Score " + str(total_score))
                        #print("first situation2")
                    elif subs_score > replay_score:
                        total_score = total_score + subs_score
                        #print("Current Score " + str(total_score))
                        replay -= 1
                    else:
                        total_score = total_score + replay_score
                        #print("Current Score " + str(total_score))
                       # print("second situation3")
                        replay -= 1
                    number_hands -= 1

    except ValueError:
        print("Please enter an integer")
        play_game(word_list)

    print("Final Score: " + str(total_score))

    # user_yn = (input("Would you like to substitute a letter:").lower())

    """
    Allow the user to play a series of hands


* Asks the user to input a total number of hands

* Accumulates the score for each hand into a total score for the 
entire series

* For each hand, before playing, ask the user if they want to substitute
one letter for another. If the user inputs 'yes', prompt them for their
desired letter. This can only be done once during the game. Once the
substitue option is used, the user should not be asked if they want to
substitute letters in the future.

* For each hand, ask the user if they would like to replay the hand.
If the user inputs 'yes', they will replay the hand and keep 
the better of the two scores for that hand.  This can only be done once 
during the game. Once the replay option is used, the user should not
be asked if they want to replay future hands. Replaying the hand does
not count as one of the total number of hands the user initially
wanted to play.

    * Note: if you replay a hand, you do not get the option to substitute
            a letter - you must play whatever hand you just had.

* Returns the total score for the series of hands

word_list: list of lowercase strings
"""


# print("play_game not implemented.")  # TO DO... Remove this line when you implement this function

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)


