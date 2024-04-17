#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')


print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")
try:
  print("\ninput value 'a'")
  a = input()
  a = float(a)

  print("\ninput value 'b'")
  b = input()
  b = float(b)

  print("\ninput value 'c'")
  c = input()
  c = float(c)

  x = (-(b) + (b**2 - 4*a*c)**0.5) / 2 * a
  x = float(x)
  y = (-(b) - (b**2 - 4*a*c)**0.5) / 2 * a
  y = float(y)
  os.system('cls')
  print(f"\n\n the roots are {x} and {y}")
  input()
except:
  print("you entered an invalid variable")
  input()