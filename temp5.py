import sys

def input_v(t):
    while True:
        x=input(t)
        try:
            x = int(x)
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")
            
    return(x)
    

while True:
    t_conversion=input("Fahrenheit(f), Celcius(c) or Quit(q): ")

    if t_conversion=="q":
       sys.exit()
    elif t_conversion=="f":
         f=input_v("Give Fahrenheit: ")
         r=(f-32)/1.8
    elif t_conversion=="c":
         c=input_v("Give Celcius: ")
         r=(c*1.8)+32
    else:
         print("Invalid Input")
         continue
    print(r)
