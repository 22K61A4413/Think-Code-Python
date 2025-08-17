str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
anagram_check=sorted(str1)==sorted(str2)
if anagram_check==True:
    print(f"The given two strings: {str1},{str2} is an anagrams")
else:
    print(f"The given two strings: {str1},{str2} is not an anagrams")