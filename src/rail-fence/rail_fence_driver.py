from rail_fence import *

word = "defend the west wall"
print("Original word: " + word)
encrpyted_word = Encrypt(word, 2)
print("Encrypted word: " + encrpyted_word)
decrpyted_word = Decrypt2(encrpyted_word,2)
print("Decrypted word: " + decrpyted_word)
