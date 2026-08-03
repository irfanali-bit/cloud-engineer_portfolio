age = int(input(" your age"))
if(age >= 18):
 print("can vote")

 # Example 2: voting
 num = 7
 
 if(num % 2 == 0):
  print("even")
 else:
  print('odd')

 password = "irfan1"
 if len(password) >= 8:
   print("strong password")
else:
   print("weak password")

email = "irfanali@gmail.com"
if"@gmail.com" in email:
    print("valid email")
else:
    print("invalid")

marks = 90
if(marks >= 90):
    print("grade A")

salary = 50000
if(salary >= 30000):
   print("bonus approved")

temperature = 40
if(temperature >= 35):
   print("very hot")


username = 'irfanali'
if len(username )>= 8:
   print("strong username")


marks = 45
if(marks >= 33):
   print("pass")
else:
   print("fail")   

balance = 1000
withdraw = 1500
if(withdraw <= balance):
   print("transaction successful")
else:
   print("insufficient balance")

signal = 'green'

if(signal == "red"):
   print("stop")
elif(signal == "yellow"):
   print("wait")
elif(signal == "green"):
   print("go")
else:
   print("invalid signal")


username= "irfan"
password = "python121"
if(username == "irfan" and password == "python121"):
   print("login successful")
else:
   print("invalid username and password")
