#import math
#print(math.pi)
#name=False
#if name:
   # print("you are abel; go in")
#else:
    #print("who the f**K are you?")
    
    #Arthimetic operation
#num1=float(input("enter the first number:"))
#operator=input("enter an operator:")
#num2=float(input("enter the second number:"))
#if operator=="+":
    #result=num1+num2
#elif operator=="-":
#    result=num1-num2
#elif operator=="*":
#    result=num1*num2
#elif operator=="/":
#    result=num1/num2
#else: 

#weight conversion

#weight=float(input("enter your weight:"))
#unit=input("enter your unit:")
#if unit=="kgs":
#    weight=weight*2.205    
#elif unit=="Lbs":
#    weight=weight/2.205  
#else:
#   print("you have entered an invalid unit!")    
#print(f"your weight in {unit} is {round(weight, 0)}{unit}")

#Temprature conversion
#temprature=float(input("enter the temprature:"))
#unit=input("enter the unit:")
#if unit=="c":
#    fahrenheit=9/5*temprature+32
#    kelvin=273+temprature
#    print(f"your temprature in fahrenheit is {round(fahrenheit, 2)} degree fahrenheits")
#print(f"your temprature in kelvin is {round(kelvin, 2)} degree kelvin")
    
#elif unit=="f":
#    celcius=5/9*temprature-32
#    kelvin=273+celcius
#    print(f"your temprature in celcius is {round(celcius, 2)} degree celcius")
#    print(f"your temprature in kelvin is {round(kelvin, 2)} degree kelvin")
#    
#elif unit=="k":
#    celcius=temprature-273
#    fahrenheit=9/5*celcius+32
#    print(f"your temprature in celcius is {round(celcius, 2)} degree celcius")
#    print(f"your temprature in fahrenheit is {round(fahrenheit, 2)} degree fahrenheits")
#else:
#    print("you have entered an invalid unit")   

#logical operators
#temp=24
#is_sunny=False
#if temp<=0 or is_sunny:
#    print("your schedule is cancelled")
#elif temp>=25 or not is_sunny:
#    print("its better to be home")
#else:
#    print("your program is still scheduled")
#if temp>=25 and is_sunny:
#    print("it is hot outside")
#elif temp<25 and not is_sunny:
# print("it is warm outside")
#else:
#    print("it is cold outside")
#print(not is_sunny)

#conditional expession= a one line shortcut for if else statement(ternary operator)
#age=24
#a=7
#b=9
#min_no=a if a<b else b
#print(f"the min_no is {min_no} and the max_no is {max_no}")
#status="old" if age>=40 else "young"
#print(status)
#access_level="user"
#user_role="admin" if access_level=="admin" else "access denied"
#print(user_role)

#string methods
#print(help(str)) 
#name=input("enter your full name: ")
#result=len(name)
#print(result)
#occurence=name.find("e")
#occurence=name.rfind("g")
#print(name.find(" "))
#name=name.capitalize(0,5)
#name=name.upper()
#name=name.lower()
#name=name.isdigit()
#name=name.isalpha()
#name=name.isalnum()
#print(name)

#phone_no=input("enter your phone no: ")
#phone_no=phone_no.count("_")
#phone_no=phone_no.replace("7", "9")
#print(phone_no.replace("_", ""))
#user_name=input("enter your name ")
#if len(user_name)<=12 and user_name.find(" ")==-1 and user_name.isalpha() :
#    print(f"welcome {user_name} ")
#else:
#    print("Oops you have entered an invalid user_name")
#if len(user_name)>=12:
#    print("your name can not be more than 12 characters")    
#elif not user_name.isalpha():
 #   print("your name needs to be only characters")
#else:
 #   print(f"welcome {user_name}")
 
  #string indexing
#name="abel_tegegne"
#print(name[-3])
#print(name[9])
#print(name[::3])
#last_4digits=name[-4:]
#print(last_4digits)
#print(name[::-1])
#print(name[::1])
 
#phone_no="911271347"
#print(phone_no[6])
#print(phone_no[1::])
#print(len(phone_no))
#print(phone_no[1:9]) 
#print(phone_no[:9])   
#print(phone_no[-7])    
#print(phone_no[-9:-1])
#print(phone_no[2:6])
#print(phone_no[::2])
#print(phone_no[::-1])
#print(phone_no[-4:])

#format specifiers
#price1=2450087.46587
#price2=-1800
#price3=2800.442897
#print(f"price1 is ${price1:.2f}")
#print(f"price2 is ${price2:.2f}")
#print(f"price3 is ${price3:.2f}")
#print(f"price1 is ${price1:15}")
#print(f"price2 is ${price2:15}")
#print(f"price3 is ${price3:15}")
#print(f"price1 is ${price1:015}")
#print(f"price2 is ${price2:015}")
#print(f"price3 is ${price3:015}")
#print(f"price1 is ${price1:<15}")
#print(f"price2 is ${price2:<15}")
#print(f"price3 is ${price3:<15}")
#print(f"price1 is ${price1:>15}")
#print(f"price2 is ${price2:>15}")
#print(f"price3 is ${price3:>15}")
#print(f"price1 is ${price1:<015}")
#print(f"price2 is ${price2:<015}")
#print(f"price3 is ${price3:<015}")
#print(f"price1 is ${price1:>015}")
#print(f"price2 is ${price2:>015}")
#print(f"price3 is ${price3:>015}")
#print(f"price1 is ${price1:^15}")
#print(f"price2 is ${price2:^15}")
#print(f"price3 is ${price3:^15}")
#print(f"price1 is ${price1:+15}")
#print(f"price2 is ${price2:+15}")
#print(f"price3 is ${price3:+15}")
#print(f"price1 is ${price1:<+15}")
#print(f"price2 is ${price2:<+15}")
#print(f"price3 is ${price3:<+15}")
#print(f"price1 is ${price1: }")
#print(f"price2 is ${price2: }")
#print(f"price3 is ${price3: }")
#print(f"price1 is ${price1:,}")
#print(f"price2 is ${price2:,}")
#print(f"price3 is ${price3:,}")
#print(f"price1 is ${price1: ,}")
#print(f"price2 is ${price2: ,}")
#print(f"price3 is ${price3: ,}")
#print(f"price1 is ${price1:+,.1f}")
#print(f"price2 is ${price2:+,.1f}")
#print(f"price3 is ${price3:+,.1f}")

#while loop
#name=input("enter your name: ")

#while name=="":
#   print("you have not entered your name")
#   name=input("please enter your name: ")
#else:
#    print(f"welcome {name}")

#age=int(input("enter your age: "))

#while age < 0:
 #   print("sorry your age can not be negative")
  #  age=int(input("please re-enter your age: "))

#print(f"you are {age} years old")

#num=float(input("enter a # between 1 and 10: "))
#while num<1 or num>10:
 #   print(f"{num} is not valid")
  #  num=float(input("re-enter your number: "))

#print(f"your # is {num}")

#compound interest calculation
#principal=0
#rate=0
#duration=0

#while True:
#    principal=float(input("enter your principal: "))
#    if principal<0:
#     print("principal can not be less than zero")
#    else:
#        break
#while True:
#    rate=float(input("enter your rate: "))
#    if rate<0:
#       print("rate can not be less than zero")
#    duration=int(input("enter your duration: "))
#if duration<0:
#     print("duration can not be less than zero")
#    else:
#        break

#total_amount=principal*pow(1+rate/100, duration)

#print(f"your total after {duration} year/s is ${total_amount:.2f}")

#for loops
#    print(x) 
#print("HAPPY NEW YEAR!")

#for counter in range(0,10):
#   print(counter) 
#print("HAPPY NEW YEAR!")
       
#for counter in reversed(range(0,10)):
#    print(counter) 
#print("HAPPY NEW YEAR!")

#for counter in range(0,10,2):
#   print(counter) 
#print("HAPPY NEW YEAR!")

#for counter in reversed(range(0,10,2)):
#   print(counter) 
#print("HAPPY NEW YEAR!")

#phone_no="911271347"
#for x in phone_no:
#    print(x)

#phone_no="911271347"
#for x in reversed(phone_no):
#    print(x)

#for x in range(1,20):
#    if x==14:
#        continue
#    print(x)

#for x in range(1,20,3):
#   if x==14:
#        continue
#   print(x)

#for x in reversed(range(1,20,2)):
#  if x==15:
#       continue
#   if x==11:
#       break
#   print(x)

for counter in range(10,1,-2):
   print(counter) 
print("HAPPY NEW YEAR!")







    
        
 


       
    
    
















