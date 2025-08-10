from collections import Counter

text=input("Enter the string: ")
freq=Counter(text)
print("The frequency of the character in the string: ",freq)