def count_vowels(str):
    str=str.lower()
    vowels="aeiou"
    if str=="":
        return 0
    else:
        if str[0] in vowels:
            return 1+ count_vowels(str[1:])
        else:
            return count_vowels(str[1:])
input=input("Enter a string: ")
result=count_vowels(input)
print(f"The vowel count in {input} is {result}")

