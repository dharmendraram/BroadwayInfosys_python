# def is_vowel(char):
#     if char.lower() in ('a', 'e', 'i', 'o', 'u'):
#         return True
#     else:
#         return False
    
# chk = input("Enter Character to check: ")

# result = is_vowel(chk)

# print(result)


datas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

vowels=["a","e","i","o","u"]

result = filter(lambda char: char in vowels,datas)

print(list(result))