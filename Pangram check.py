import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)  # set of all letters a-z
    return alphabet <= set(sentence.lower())
str=input("Enter the sentence: ")
result=is_pangram(str)
if result==True:
    print(f"The given sentence: {str} is pangram")
else:
    print(f"The given sentence: {str} is not pangram")