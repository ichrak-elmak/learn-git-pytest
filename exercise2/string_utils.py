# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"  
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count



def is_palindrome(s: str) -> bool:
    cleaned_str = ""

    for char in s:
        if char != " ":  
            if 'A' <= char <= 'Z':  
                cleaned_str += char.lower()  
            else:
                cleaned_str += char  

    return cleaned_str == cleaned_str[::-1] 




def capitalize_words(s: str) -> str:
    resultat = ""
    new_word = True 
    for char in s:
        if new_word and 'a' <= char <= 'z':  
            resultat += chr(ord(char) - 32)  
        else:
            resultat += char  

        new_word = char == " " 

    return resultat
