from rail_fence import *

word = "defend"
print("Original word: " + word)
encrpyted_word = Encrypt(word, 5)
print("Encrypted word: " + encrpyted_word)
decrpyted_word = Decrypt(encrpyted_word,5)
#print("Decrypted word: " + decrpyted_word)