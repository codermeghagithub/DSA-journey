
def func():
  try:
    neumenator=float(input("Enter  a number: "))
    deno=float(input("Enter  a number: "))
    div=neumenator/deno
    print(div)
    return 1
  except ZeroDivisionError:
    print("denominator is zero")
    return 0
  finally:
    print("this blok always executed")  
x=func()
print(x)