ticket = input("please enter your kind : ")
price = float(input("please enter the price : "))
credits = input("please enter your card : ")
if ticket == "child":
    print("child cant have a credit card")
elif ticket == "men" and price == 40 and credits == "platinum":
   print ("the price is : free ")
elif ticket == "old" and price == 30 and credits == "platinum":
   print ("the price is : free ")
elif ticket == "older" and price == 20 and credits == "platinum":
    print("the price is : free ")
elif ticket == "men" and price == 40 and credits == "gold":
   print("the price is :"  ,(price*0.5))
elif ticket == "old" and price == 30 and credits == "gold":
   print("the price is : " ,(price*0.5))
elif ticket == "older" and price == 20 and credits == "gold":
   print("the price is : " ,(price*0.5))
elif ticket == "men" and price == 40 and credits == "movie":
    print("the price is : " ,(price*0.75))
elif ticket == "old" and price == 30 and credits == "movie":
    print("the price is : " ,(price*0.75))
elif ticket == "older" and price == 20 and credits == "movie":
    print("the price is : ",(price*0.75))
else:
    print ("you have a wrong in type")

#-----------
# question 6
donor = input("please enter you donor : ")
recipient = input("please enter you recipient : ")
if donor == "ab" and recipient == "ab" or donor == "a" and recipient == "a" or donor == "o" or recipient == "o" or donor == "b" and recipient =="b":
    print("yes")
elif recipient == "ab" and donor != "a" or "b" or "o":
    print("no")
elif donor == "o" and recipient != "a" or "b" or "ab":
    print("no")
else:
    print ("invalid input")

#------------

