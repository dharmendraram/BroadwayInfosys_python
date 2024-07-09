"""
1.
Write a Python program to combine two dictionaries by adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200, 'd':400}
output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""

def is_combine_dictionaries(d1, d2):
    combined = {} 
    for key in d1:
        combined[key]=d1.get(key,0) + d2.get(key,0)
    return combined

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = is_combine_dictionaries(d1, d2)
print(result)

"""
2. Write a Python program to count the number of even and odd numbers in a
series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
def odd_even_count(numbers):
    even_count=0
    odd_count=0
    for number in numbers:
        if number % 2 ==0:
            even_count +=1
        else:
            odd_count +=1
    print(f"Number is even:- {even_count}")
    print(f"Number is odd:- {odd_count}")
    
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd_even_count(numbers)

"""
3. Write a Python program that iterates the integers from 1 to 50. For multiples
of three print "Fizz" instead of the number and for multiples of five print
"Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz
…
"""

for each in range(1,51):
  if each % 15 == 0:
    print("FizzBuzz")
  elif each % 3 == 0:
    print("Fizz")
  elif each % 5 == 0:
    print("Buzz")
  else:
    print(each)



"""
Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
  """

def is_top_three_items_display(data):
  res={}
  for key in data:
    if key <="item3":
      res[key]=data[key]
  return res

datas={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
result=is_top_three_items_display(datas)
print(f"Top Three Items:-{result}")  

