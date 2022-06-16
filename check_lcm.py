def lcm(a,b):
      if a > b:
        for i in range(2, a):
         if a % i == 0 and b % i == 0:
            return i
      else:
        for i in range(2, b):
         if a % i == 0 and b % i == 0:
            return i

a=int(input("enter the first number "))
b=int(input("enter the second number "))
print("the lcm of the two numbers is ",lcm(a,b))    
