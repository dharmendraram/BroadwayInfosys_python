"""
WAP to sum all the digits of a three-digit number
input:573
output:15
"""


number=573

def sum_three_digits(data):
    new_numb=str(data)
    sum=0
    for each in new_numb:
        sum += int(each)
    return sum


result =sum_three_digits(number)
print(result)