#import sys
print("Welcome to the Ceasar Cipher!")

phrase = input('Type in your secret message here\n')

encryption = phrase.maketrans("abcdefghijklmnopqrstuvwxyz", "fghijklmnopqrstuvwxyzabcde")
output = phrase.translate(encryption)
print("Your message : ", phrase)
print("Your secret message becomes: ", output)

#sys.exit("Congratulations on making a secret message. Goodbye")