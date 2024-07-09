# Create a decorator function which when applied to another function (that returns a string), it gives
# the uppercase value

def to_upper(func):
    def inner_fxn(*args, **kwargs):
        
        msg=func(*args,**kwargs)
        return msg.upper()
    return inner_fxn

@to_upper
def display(msg):
    return msg

result = display(msg="hello world")
print(result)