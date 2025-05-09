def main():
    word = input("Enter your name: ")
    remove_vowels(word)

def remove_vowels(word):
    vowels = "aeiouAEIOU"
    word_copy = word[:]
    for letter in word_copy:
        if letter in vowels:
            word = word.replace(letter,"")
    
    print(word)

main()
