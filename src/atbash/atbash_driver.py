from atbash import *

word = "abcdefghijkl !!/||mnopqrstuvwxyz"
print("Original word: " + word)
encrpyted_word = Encrypt(word)
print("Encrypted word: " + encrpyted_word)
decrpyted_word = Decrypt(encrpyted_word)
print("Decrypted word: " + decrpyted_word)