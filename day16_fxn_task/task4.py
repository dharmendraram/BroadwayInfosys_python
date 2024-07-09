'''
Write a Python program to create a dictionary from a string. Track the count of the letters from the string.
Input = “broadway”
Output = {“b”: 1, “r”: 1, “o”: 1, “a”: 2, “d”: 1, “w”: 1, “y”: 1}

'''
inp_str="broadway"

letter_count={}

for letter in inp_str:
    if letter in letter_count:
        letter_count[letter]+=1
    else:
        letter_count[letter]=1
print(letter_count)


def get_char_count(data):
    letter_count={}
    for letter in inp_str:
        if letter in letter_count:
            letter_count[letter]+=1
        else:
            letter_count[letter]=1
    return letter_count
result=get_char_count(inp_str)

print(result)
