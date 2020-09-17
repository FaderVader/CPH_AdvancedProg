def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x   
    x = "hello" # will now modify the closured x
  myfunc2() 
  return x

print(myfunc1())  #hello


def myfuncA():
  x = "John"
  def myfuncB():
    x = "hello"   # will not modify x of closure
  myfuncB()
  return x

print(myfuncA())   #John