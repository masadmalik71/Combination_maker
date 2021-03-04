from replit import clear
import re

def fact_maker(n):
  fact_of_n = 1
  if n == 0:
    return fact_of_n
  else:
    for i in range(n, 0,-1):
      fact_of_n *= i
    return fact_of_n

ender = False
while not ender:
  clear()
  input_chekcer = False
  while not input_chekcer:
    n = input("Enter value of n: ")
    r = input("Enter value of r: ")
    n_list = re.findall("[0-9]", n)
    r_list = re.findall("[0-9]", r)

    if len(n_list) == 0 and len(r_list) == 0: 
      clear()
      print("You entered the wrong input. Please enter again.")
    else:
      n = int(''.join(n_list))
      r = int(''.join(r_list))
      n_r = n-r
      if r > n:
        clear()
        print("You entered the wrong input. Please enter again.")
      elif r < n:
        input_chekcer = True

    if n == 0:
      n = 1
      input_chekcer = True
    if r == 0:
      r = 1
      input_chekcer = True


  n = fact_maker(n)
  r = fact_maker(r)
  n_r = fact_maker(n_r)


  d = r*n_r
  c = n / d
  print(c)


  ending1 = False
  while not ending1:
    ending = input("Do wish to you use it agaian: Type 'y' or 'n': ")
    ending_list = re.findall("y|n", ending)
    if len(ending_list) > 0:
      ending = ''.join(ending_list)
      if ending == 'n':
        table_again1 = True
        ender = True
      if ending == 'y':
        ending1 = True
    else:
      clear()
      print("You entered the wrong option.")