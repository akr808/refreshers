'''Refreshing concepts on decorators'''

def function_decorator(calling_fun_name,name,*args,**kwargs):
    print("Before param function call")
    calling_fun_name(name,args,kwargs)
    print("After the param function is called")

def fun_type1(*args,**kwargs):
    print("This is an empty function withnout any parameter")

def fun_type2(name:str,*args,**kwargs)->None:
    print("Welcome {0} to this class, this is a function with a string paramater".format(name))


if __name__ == '__main__':
    '''The empty function is called'''
    function_decorator(fun_type1,'')

    '''The parameterised function is called'''
    function_decorator(fun_type2,name='akr')