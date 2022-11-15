'''Refreshing concepts on decorators'''
'''Author:akr'''

def function_decorator(calling_fun_name,*args,**kwargs):
    print("Before param function call")
    calling_fun_name(*args,**kwargs)
    print("After the param function is called")

def fun_type1(*args,**kwargs):
    '''A function that just prints a text'''
    print("This is an empty function withnout any parameter")

def fun_type2(*args,**kwargs)->None:
    '''A function that accepts a param and prints a message'''
    print("Welcome {name} to this class, this is a function with a string paramater".format(**kwargs))


if __name__ == '__main__':
    #Main method to call the decorator function


    #The empty function is called
    function_decorator(fun_type1,'')

    #The parameterised function is called
    function_decorator(fun_type2,name='akr')
