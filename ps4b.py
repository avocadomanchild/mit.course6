# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
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
        x = copy.deepcopy(self.valid_words)
        return x

    def orginal_shift(self):
        lower_letters = string.ascii_lowercase
        upper_letters  = string.ascii_lowercase.upper()
        Total_letters = lower_letters+upper_letters
        dict = {}
        for i in Total_letters:
            dict[i] = Total_letters.index(i)
        return dict



    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        if 0 <= shift <= 25: 
            
            lower_letters = string.ascii_lowercase
            upper_letters  = string.ascii_lowercase.upper()
            Total_letters = lower_letters + upper_letters
            dict = {}
            my_dict = {}
            for i in Total_letters:
                dict[i] = Total_letters.index(i)
            #print(dict)
            for j in dict:
                if Total_letters.index(j) + shift > 51:
                    my_dict[j] = Total_letters.index(j) + shift - 52
                else:
                    my_dict[j] = Total_letters.index(j)+ shift
            return my_dict
        else: 
            print("shift must be a number from 0-25")



    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dict = self.orginal_shift()
        my_dict = self.build_shift_dict(shift)
        #print(my_dict)
        #print(type(my_dict.values()))
        string = []
        new_message = ""
        for letters in self.message_text:
            if letters.isalpha() == True and letters in dict:
                 string.append(dict.get(letters))

            else:
                string.append(letters)


        for chars in string:

            if chars in my_dict.values():
                for num in my_dict:
                    #print("str:" + str(chars))
                    #print("num:" + str(my_dict[num]))
                    if my_dict[num] == chars:
                        #print(num)
                        new_message = new_message + num
            else:
                new_message = new_message + chars

        print(string)
        print(new_message)
        return new_message






#c = Message("poop p")
##print(c.build_shift_dict(25))
#print(c.orginal_shift())
#print(c.apply_shift(25))
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.shift = shift 
        
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encryption_dict = self.build_shift_dict(self.shift)
        return encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        get_message_text_encrypted = self.apply_shift(self.shift)
        return get_message_text_encrypted

    # def __str__(self):
    #     return "message:"+str(self.)
    def change_shift(self, new_shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        if 0 <= new_shift <= 25: 

            self.shift = new_shift 
            print(self.shift)
        else: 
            print("shift must be within 0-25")




#b = PlaintextMessage("none",3)
#print(d.get_shift())

#print((d.get_encryption_dict()))
#print(d.change_shift(3))

class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)


        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value


        '''
        emptylist = [] 
        for i in range(1,26): 
            x = self.apply_shift(i)
            list = x.split()
            emptylist.append(list)
       # print(emptylist)
        y = 0 
        counter = [] 
        #for words in self.valid_words: 
        #     print(words)
        # for message in emptylist: 
        #     print(message)
        #     for word in message: 
        #         print(word)
        #         #print(type(word))
        # if "apple" in x :
        #     print("yes")
        # else: 
        #     print("no")
        # print(type(self.valid_words))

        # print(x)                    
        y = self.get_valid_words()
        #print(y[0:10])
        list2 = [] # list of valid words because they have /n
        
        list3 = [] #counter 
        for words in y: 
            x = words.strip('\n') # this will strip the /n in the list 
            list2.append(x) # putting into new list 
        for message in emptylist: # for loop throught the list of applyed shift to the instance of the object 
            #print(message)
            y2 = 0 
            for word in message:  # for looping if the message has more than one word 
                if word.lower() in list2: 
                    print(word)
                   git add p
        

        maxvalue = max(list3)
        index_postion = list3.index(maxvalue)
        final_position = index_postion + 1
        print(index_postion)
        decrypt_word =  emptylist[index_postion]
        answer = (final_position,decrypt_word)
        #print (answer)
        return answer
        






        
plaintext = PlaintextMessage('my name is ben ', 5)
print('Actual Output:', plaintext.get_message_text_encrypted())

ciphertext = CiphertextMessage('ht iVhZ dn WZi')
# print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())


# d = PlaintextMessage("apple",3)           
# print((d.get_message_text_encrypted()))           
# ciphertext = CiphertextMessage('DSSOH')
# print(ciphertext.decrypt_message())


       
if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
