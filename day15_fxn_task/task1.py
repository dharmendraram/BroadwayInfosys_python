'''
Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

'''

simple_list=[1,2,3,3,3,3,4,5]

def get_unique():
    result=set(simple_list)
    print(list(result))
get_unique()


def get_data(element):
    unique_list=[]
    for each in element:
        if each not in unique_list:
            unique_list.append(each)
    return unique_list
        
result = get_data(simple_list)
print(result)


def get_data(element):
    unique_list=[]
    [unique_list.append(each) for each in element if each not in unique_list]
    return unique_list
        
result = get_data(simple_list)
print(list(result))


"""
15. Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
"""

# data1=[1,2,3]
# data2=[4,5,6]
# def display(lst1,lst2):
#     result = map(lambda x, y: x + y, lst1, lst2)
#     print(list(result))
# display(data1,data2)

# def add_two_lists(lst1,lst2):
#     result=[]
#     for index,value in enumerate(lst1):
#         s=value + lst2[index]
#         result.append(s)
#     return result

# data1=[1,2,3]
# data2=[4,5,6]
# r=add_two_lists(data1,data2)
# print(r)



data1=[1,2,3]
data2=[4,5,6]
def add_two_lists(lst1,lst2):
    iterable=zip(lst1,lst2)
    result=map(lambda x:sum(x), iterable)
    return list(result)
res=add_two_lists(data1,data2)
print(res)