def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s_to_t = {}
    map_t_to_s = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        # check s -> t mapping
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t

        # check t -> s mapping
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s

    return True



str1 = input("Enter the string1: ")
str2 = input("Enter the string2: ")
result = isIsomorphic(str1, str2)

if result:
    print("The given two strings are Isomorphic")
else:
    print("The given strings are not Isomorphic")
