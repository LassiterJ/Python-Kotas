'''Codingdojo.org FizzBuzz'''
# Problem Description
def has3(number):#Hello.
  number = str(number)
# print number
  i = 0
  while i < len(number):
    variable = number[i]
    if variable == '3':
      return True
    i += 1
  return False
def has5(number):#Hello.
  number = str(number)
# print number
  i = 0
  while i < len(number):
    variable = number[i]
    if variable == '5':
      return True
    i += 1
  return False
index = 0
for i in range(1, 100):
  if i % 3 == 0 and i % 5 == 0:
     print "FizzBuzz"
  elif i % 3 == 0 or has3(i):   
     print "Fizz"
  elif i % 5 == 0 or has5(i):
     print "Buzz"
  else:
     print i




#
