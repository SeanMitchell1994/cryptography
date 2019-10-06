from caesar import *

word = "defend the east wall of the castle"
print("Original word: " + word)
encrpyted_word = Encrypt(word, 3)
print("Encrypted word: " + encrpyted_word)
decrpyted_word = Decrypt(encrpyted_word,3)
print("Decrypted word: " + decrpyted_word)