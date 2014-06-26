t_conversion=input("Fahrenheit(f) or Celcius(c): ")
if t_conversion=="f":
   f=int(input("Give Fahrenheit: "))
   c=(f-32)/1.8
   print(c)
if t_conversion=="c":
   c=int(input("Give Celcius: "))
   f=(c*1.8)+32
   print(f)


