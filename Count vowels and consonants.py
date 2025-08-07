def count_Vowels_Consonants(text):
    vowels="aeiouAEIOU"
    vowel_count=0
    consonant_count=0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    print(f"The Vowels are {vowel_count} and Consonants are {consonant_count} in {text}")

text=input("Enter the Text: ")
count_Vowels_Consonants(text)