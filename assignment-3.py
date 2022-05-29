#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Assignment 3

This assignment covers your mastery over the basic constructs of
    Python. It engages your ability to transform
    data without affecting anything outside the program.

If you can do this assignment, then you can feel confident in your
    Python abilities.
'''


# In[ ]:


def shift_letter(letter, shift):
    '''Item 1. 
    Shift Letter. 12 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Write your code below this line


# In[ ]:


al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = ''
rem = 0
fil = 0
check = al.index(letter)
total = check + shift
def shift_letter(letter, shift):
    for i in range (len(al)):
        if al[i] == letter:
            if  total > len(al):
                rem = len(al)-check
                fil = shift - rem
                
                new = al[fil]
            else:
                new = al[i + shift]
    return new


# In[ ]:


letter = input("Enter Letter: ")
shift = int(input("Enter Number: "))

put = shift_letter(letter, shift)

print(put)


# In[ ]:


def caesar_cipher(message, shift):
    '''Item 2.
    Caesar Cipher. 18 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    
    bghn
    # Write your code below this line


# In[43]:


al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = []
rem = 0
fil = 0
new = ''
def caesar_cipher(message, shift):
    newl= list(message)
    
    for i in range (len(al)):
        for j in range (len(newl)):
            if al[i] == newl[j]:
                check = al.index(newl[j])
                total = check + shift
                if  total > len(al):
                    rem = len(al)-check
                    fil = shift - rem
                
                    n.append(al[fil])
                else:
                    n.append(al[i + shift])
    new = ''.join(n)
    return new


# In[44]:


message = input("Enter Message: ")
shift = int(input("Enter Number: "))

put = caesar_cipher(message, shift)

print(put.upper())


# In[27]:


def shift_by_letter(letter, shift_letter):
    '''Item 3.
    Shift By Letter. 12 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Write your code below this line


# In[48]:


al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = 0
new = ''
def shift_by_letter(letter, shift_letter):
    x = al.index(letter)
    shift_letter = al.index(shift_letter)
    num = x + shift_letter
    new = al[num]
    return new


# In[49]:


letter = input("Enter letter: ")
shift_letter = input("Enter shift letter: ")

put = shift_by_letter(letter, shift_letter)
print(put)


# In[28]:


def vigenere_cipher(message, key):
    '''Item 4.
    Vigenere Cipher. 18 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Write your code below this line


# In[55]:


al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = 0
new = ''
z = []
def vigenere_cipher(message, key):
    newl= list(message)
    keyl= list(key)
    
    for i in range (len(newl)):
        x = al.index(newl[i])
        shift_letter = al.index(keyl[i])
        num = x + shift_letter
        z.append(al[num])
    new = ''.join(z)
    return new


# In[58]:


message = input("Enter message: ")
key = input("Enter key: ")
if len(key) > len(message):
    print("Invalid Key")
elif " " in key:
    print("Invalid Key")
else:
    put = vigenere_cipher(message, key)
    print(put.upper())

