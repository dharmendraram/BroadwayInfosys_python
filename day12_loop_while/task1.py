# '''
# WAP to delete all the occurrences of a specified character in a given string 
# S = “All the occurrences of a specified character in a given string”
# Input = “a”
# Output = “ll occurrences of  specified chrcter in  given string”

str="All the occurrences of a specified character in a given string"
inp=input("Enter the character: ")
result=""
for s in str.lower():
    if s==inp.lower():
        continue
    result +=s
print(result)
