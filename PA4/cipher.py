# assignment: programming assignment 4
# author: Alejandra Sicairos
# date: 11/28/20
# file: cipher.py is a program that (put the description of the program)
# input: user imput that are specifically 
# output:string message

# read text from a file and return text as a string
def readfile():
   file_handler1 = input('Please enter a file for reading: ')
   try:
      file1 = open (filename2, "r")
      for line in file1:
         file1.write(text)
   except IOError:
      print ('file cannot be opened')
   else:
      file1.close()
   return message

# write a string (message) to a file
def writefile():
   file_handler = input('Please enter a file for writing: ')
   try:
      file = open (filename2, "w+")
      for line in file:
         file.write(text)
   except IOError:
      print ('file cannot be opened')
   else:
      file.close()
   return message

# make a list (tuple) of letters in the English alphabet
def make_alphabet():
   alphabet = ()
   for i in range(26):
       char = i + 65
       alphabet += (chr(char),)
   #print (alphabet)
   return alphabet

# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols
def encode(plaintext):
   plaintext = plaintext.upper()
   shift = 3
   ciphertext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in plaintext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + shift) % length]
               ciphertext.append(letter)
               found = True
               break
       if not found:
           ciphertext.append(char)
   return ciphertext

# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols
# check how the function encode() is implemented
# your implementation of the function decode() can be very similar
# to the implementation of the function encode()
def decode(plaintext):
   shift = -3
   plaintext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in ciphertext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i - shift) % length]
               plaintext.append(letter)
               found = True
               break
       if not found:
           plaintext.append(char)
   return plaintext

# convert a list into a string
# for example, the list ["A", "B", "C"] to the string "ABC" or
# the list ["H", "O", "W", " ", "A", "R", "E", " ", "Y", "O", "U", "?"] to the string "HOW ARE YOU?"
def to_string(text):
   s = ""
   return(s.join(text))

done = False
while not done:
   print("Would you like to encode or decode the message?")
   choice = input("Type E to encode, D to decode, or Q to quit: ")

   if choice == "e" or choice == "E" or choice == "d" or choice == "D":
      readfile()
      writefile()
   if choice == "q" or choice == "Q":
      break
      if choice ==  "e":
         encode(message)
      else:
         decode(reading_file)
   print(f"Ciphertext: n/{ciphertext}")
   print(f"Plaintext: n/{plaintext}")

print("Goodbye!")
