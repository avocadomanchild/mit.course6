# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from typing import AbstractSet, final
from ps4a import vowel_permutation   # type: ignore
import copy 


### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
    
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text # this is intizaling the message of an object 
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
                
    def build_transpose_dict(self, permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # VOWELS_LOWER = 'aeiou'
        # VOWELS_UPPER = 'AEIOU'
        # CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
        # CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
        #this is another method to put two list together and insert into a dicitonary 
        # d = {} 
            # for k, v in zip(name_list, num_list):
        # d[k] = v
        # this is another medthod in one line lol 
        #d = {k: v for k, v in zip(name_list, num_list)
        
        try:
            permutations = permutation.lower()
            upper_letters= copy.deepcopy(permutation).upper()
            TOTAL_CONSONANTS = CONSONANTS_LOWER + CONSONANTS_UPPER
            TOTAL_VOWELS = VOWELS_LOWER + VOWELS_UPPER
            for chars in permutations:
                if chars not in TOTAL_VOWELS:
                    return str("Permutation must be a string that contains the all the vowels , ex.'aioue'. Y is not a vowel in this object" )
            if chars in permutations:
                d1 = {}
                for letters in TOTAL_CONSONANTS: 
                    d1[letters] = letters 
                d2 = dict(zip(VOWELS_LOWER,permutations))
                d3 = dict(zip(VOWELS_UPPER,upper_letters))
                d4 = {**d1,**d2,**d3}
                return(d4)
            elif len(permutations) != 5: 
                return str("You must include all the vowels your input. Y is not consider a vowel in this object ")
            else: 
                return str("Please enter a string of vowels in any permutation of a e i o u ")
        
        except AttributeError: 
             return str("Please enter a string of vowels in any permutation of a e i o u, ex.'aioue'.")

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message = "" 
        for letters in self.message_text: 
            if letters in transpose_dict: 
                for chars in transpose_dict: 
                    if transpose_dict[chars] == letters: 
                        encrypted_message = encrypted_message + chars 
            else:
                encrypted_message = encrypted_message + letters 
        
        return encrypted_message
    
     
                

            
        
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self,text)
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        list_perm = vowel_permutation("aeiou")    # this creates all permuations of vowels 
        #enc_dict = message.build_transpose_dict(permutation)
      
        
        orginal_perm = "aeiou"
        dictionary = [] 
        
        for i in list_perm:   # creates multiple dictionaries with the keys of the aeiou 
            d = dict(zip(orginal_perm,i))
            dictionary.append(d)
        #print("this is possiable combinations"+ str(dictionary))
        # calling the object that we created 
        transposed_mess = message.apply_transpose(enc_dict) # #My numi os Binjumon Cheng und O loki roci und pozzu!

        list_words = [] # this is the list of all the messages that have been compared to the dictionaries that we created 
        for dicts in dictionary:
            new_message = ''
            for letters in transposed_mess:
                y = 0 
                for j,k in dicts.items():
                    if letters == j:
                        new_message = new_message + k
                        break 
                    else:
                        y = y + 1 
                if y == 5:
                    new_message = new_message + letters
            list_words.append(new_message)
        
        no_punc       = [x.translate(str.maketrans('', '', string.punctuation)) for x in list_words ] # this takes the punctuation out 
        words_in_mess = [x.split(" ") for x in no_punc] # this makes each letter into a list of lsit 
       
        # print(words_in_mess)
        #list_of_messages =list(map(lambda x : [x],no_punc))
        #print(list_of_messages)
        #print(no_punc)
        poss_words = self.get_valid_words() 
        poss_words2 = [x.strip('\n') for x in poss_words]
        #print(poss_words2)
 

        counter1 = []
        for mess in words_in_mess: 
            y = 0 
           # print(mess)
            for word in mess: 
                #print(word)
                if word in poss_words2:
                    y += 1
            counter1.append(y)
        print(counter1)
        print(len(counter1))

        maxvalue = max(counter1)
        index_position = counter1.index(maxvalue)
        # this is finding the position of the permuation that you want 
        
        if maxvalue == 0: 
            return str("orginal message" + str(transposed_mess) + "no good combination")
        else: 
            return (list_words[index_position])



        #     for words in mess: 
        #         print("here" + str(words))
        # #         if words in self.valid_words: 
        # #             y += 1
        # #     counter1.append(y)
        # # print(counter1)

    
            

        










        # 	list_Of_decrypt_message.append(new_mess)
          
       	# for i in dictionary 
        # 	new_message = ""
        #   	for letters in words
        # 			for chars in i 
		# 							if chars == letters: 
        #       			 new_mess == new_mess + j 
        #         	else 
        #         		new_mess == new_mess + letters 
        #   	list_Of_decrypt_message.append(new_mess)
            
            
            
        #     listofmess = [] 
            
            
        #     for i in listofmess 
        #     	x = i.split()
        #       	for words in x: 
        #           if words in valid_wordslist : 
        #             y  += 1 




                # new_message = "" 
        # for words in transposed_mess:
        #     for letters in words:
        #         for i in newlist:
        #             for j,k in i.items(): 
        #                 if letters == i.get(j):
        #                      new_message = new_message + j 
        #                 else:
        #         	         new_message = new_message + letters
        # list_of_decrypt_message.append(new_message)
        # print(list_of_decrypt_message)
              
        





        



if __name__ == '__main__':
    message = SubMessage("hello ben eat chicken and rice!")
    permutation = ("euoia")
    enc_dict = message.build_transpose_dict(permutation) 
    print(enc_dict) 
    print(message.apply_transpose(enc_dict))
    message2 = EncryptedSubMessage("ebn")
    print(message2.decrypt_message())
    

#     # Example test case
#     message = SubMessage("Hello World!")
#     permutation = "eaiuo"
#     enc_dict = message.build_transpose_dict(permutation)
#     print("Original message:", message.get_message_text(), "Permutation:", permutation)
#     print("Expected encryption:", "Hallu Wurld!")
#     print("Actual encryption:", message.apply_transpose(enc_dict))
#     enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
#     print("Decrypted message:", enc_message.decrypt_message())
     
#     #TODO: WRITE YOUR TEST CASES HERE

