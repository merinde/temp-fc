import sys

t_conversion=input("Fahrenheit(f) or Celcius(c): ")

if t_conversion=="f":
   f=int(input("Give Fahrenheit: "))
   r=(f-32)/1.8
elif t_conversion=="c":
     c=int(input("Give Celcius: "))
     r=(c*1.8)+32
else:
   print("Incorrect input")
   sys.exit()
print(r)
