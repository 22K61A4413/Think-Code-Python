import string  
text = input("Enter the text: ")
no_punc = text.translate(str.maketrans('', '', string.punctuation))
print(f"The text without punctuations: {no_punc}")
