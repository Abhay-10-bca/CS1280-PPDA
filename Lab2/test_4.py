def outer_function():
  global a
  a = 20
  print("a =", a)
a=10
outer_function()
print("global value of a=", a)
