from math import factorial
n=int(input("Enter the Number = "))
b=int(input("Enter the Row = "))
if(n>0):
      for i in range(n):
          for j in range(n-i+1):
              print(end=" ")
          for j in range(i+1):
              print(factorial(i)//(factorinal(i)*factorial(i-j)),end=" ")
          print()
      if(b>0):
          a=0
          for i in range(n):
              for j in range(i+1):
                  if(i==b-1):
                      a+=factorial(i)//(factorial(j)*factorial(i-j))
          print("Sum of Numbers= ",a)
      else:
          print("Invalid Input")
else:
    print("Invalid Input")
            
