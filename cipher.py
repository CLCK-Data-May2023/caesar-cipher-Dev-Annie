phrase = input('Type in your secret message here\n')

encryption = phrase.maketrans("abcdefghijklmnopqrstuvwxyz", "efghijklmnopqrstuvwxyzabcd")
output = phrase.translate(encryption)
print("Your message : ", phrase)
print("Your secret message becomes: ", output)

