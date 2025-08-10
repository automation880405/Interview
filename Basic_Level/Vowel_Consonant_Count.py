#Write a program to count the number of vowels and consonants in a string.

def count_vowel_consonant(word):
    #Intialize vowel count

    vowel = 0
    consonant = 0
        #define sets of vowels

    set_vowel = ("aeiouAEIOU")
        # Iterate through characters in the string
    for char in word:
        if char.isalpha():
            if char in set_vowel:
                vowel += 1
            else:
                consonant += 1
    return vowel, consonant

# Example usage
string = input("Enter a string: ")
vowels, consonants = count_vowel_consonant(string)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
