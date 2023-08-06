#import sys
#print("Welcome to the Ceasar Cipher!")

phrase = input('Please enter a sentence\n')

encryption = phrase.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "fghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcde")
output = phrase.translate(encryption)
print("The encrypted sentence is:",output)

#sys.exit("Congratulations on making a secret message. Goodbye")