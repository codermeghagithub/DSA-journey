# /creating decoretors
# 
# def greet(fx):
#   def mfx():  #  you have to give this function within the decoretor func because this inside func have  return .So yes — if you don't define and return a function inside the decorator — it's not a proper decorator.


#     print("GoodMorning")
#     fx()
#     print("Thanks for using this function.")
#   return mfx  
  
# @greet   #creating a decorator
# def hello():
#   print("Hello Everyone")

#   def add(a,b):
#     print(a+b)
# hello()



# 2.
# if you want to work this add function so you have to use *args and **kwargs
# def greet(fx):
#   def mfx(*args,**kwargs):
#     print("Good Morning")
#     fx(*args,**kwargs)
#     print("Thanks for using this function.")
#   return mfx  
  


# @greet   #creating a decorator
# def hello():
#   print("Hello Everyone")
# @greet
# def add(a,b):
#     print(a+b)

# hello()
# add(2,5)


# One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:

# import logging
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
# @log_function_call
# def my_function(a, b):
    # return a + b


# In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.

# prac  1:
# def megha(fm):
#   def rit(*args,**kwargs):
#     print("Godd afternoon")
#     fm(*args,**kwargs)
#     print("Godd")

#   return rit  


# @megha 
# def mul(a,b):
#   print (a*b)
# def wel():
#   print("Hi welcome everyone ") 
# mul(4,6)  

