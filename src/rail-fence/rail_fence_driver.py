from rail_fence import *

word = "defend"
print("Original word: " + word)
encrpyted_word = Encrypt(word, 2)
print("Encrypted word: " + encrpyted_word)
decrpyted_word = Decrypt(encrpyted_word,2)
print("Decrypted word: " + decrpyted_word)