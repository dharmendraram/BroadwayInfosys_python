# *args, **args are the arbitrary arguments in python function

# def addition(*args):
#     print(type(args))
#     print(args)
# addition(1,2)
# addition(1,2,3)
# addition(1,2,3,4)
# addition(1,2,3,4,5)


# def addition(*args):
#     result=0
#     for each in args:
#         result +=each
#         print(result)
# addition(1,2)
# addition(1,2,3)
# addition(1,2,3,4)
# addition(1,2,3,4,5)


# def addition(*args):
#    print(sum(args))
# addition(1,2)
# addition(1,2,3)
# addition(1,2,3,4)
# addition(1,2,3,4,5)

# def addition(**kwargs):
#     print(kwargs)
# addition(a=1,b=2)
# addition(a=1,b=2,c=3)
# addition(a=1,b=2,c=3,d=4)
# addition(a=1,b=2,c=3,d=4,e=5)

# def addition(**kwargs):
#     sum=0
#     for key,value in kwargs.items():
#         sum +=value
#         print(sum)
# addition(a=1,b=2)
# addition(a=1,b=2,c=3)
# addition(a=1,b=2,c=3,d=4)
# addition(a=1,b=2,c=3,d=4,e=5)

def addition(**kwargs):
    result=kwargs.values()
    print(sum(result))
addition(a=1,b=2)
addition(a=1,b=2,c=3)
addition(a=1,b=2,c=3,d=4)
addition(a=1,b=2,c=3,d=4,e=5)
