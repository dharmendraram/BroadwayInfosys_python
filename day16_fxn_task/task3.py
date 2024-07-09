"""
“Python + is + an + awesome + language”.
Split the given string to get a list and join to get another string
“Python is an awesome language”
"""

s = "Python + is + an + awesome + language"
sp=s.split("+")

print(sp) #['Python ', ' is ', ' an ', ' awesome ', ' language']

result="".join(sp)

print(result)  # "Python is an awesome language"