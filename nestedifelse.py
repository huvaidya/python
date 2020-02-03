num = int(input("enter number"))
if num%5 == 0:
   if num%10 == 0:
      print ("Divisible by 5 and 10")
   else:
      print ("divisible by 5 not divisible by 10")
else:
   if num%10 == 0:
      print ("divisible by 10 not divisible by 5")
   else:
      print  ("not Divisible by 5 not divisible by 10")