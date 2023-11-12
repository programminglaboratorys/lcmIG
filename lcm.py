import time
import math



def timeit(func):
  def wrapper(*args,**kw):
       start = time.time()
       returned_value = func(*args,**kw)
       end = time.time()
       print(f"function {func.__name__} ended in:",end - start)
       return returned_value
  wrapper.__name__
  return wrapper



@timeit
def lcm1(n):
 result = 1
 for i in range(1, n+1):
  result = result * i // math.gcd(result, i)
 return result

from sympy import lcm
@timeit
def lcm2(n):
 result = 1
 # Calculate the LCM of all numbers from 1 to 250000
 for i in range(1, n+1):
  result = lcm(result, i)
 return result


from functools import reduce
@timeit
def lcm3(n):
  return reduce(lambda a,b:a * b // math.gcd(a, b), range(1,n+1, 1))

from ctypes import CDLL

clib = CDLL('./my_c_library.dll')
@timeit
def lcm4(n):
  return clib.range_lcm(1,n+1)


lcm1(250000)
lcm2(250000)
lcm3(250000)
lcm4(250000)
"""
import sys
import json
sys.set_int_max_str_digits(719400000)
with open("tmp_.txt","w+") as f: f.write(str(big_string))
"""