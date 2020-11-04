a = 5
b = 7
c = (a**2+b**2)**0.5
print(c)
area = (a+b)/2
print('the area is: ', area)
diameter = a+b+c
print('the diameter is: ', diameter)

# ----------
age = 30
weight = 100
high = 171

bmi = (weight / (high*age))
print("your bmi is: ", bmi)

#-------
movie = "f and f"
actor = "Vin Diesel"
start = 10.5
length = 100
end = start + length
print("the name of the movie is:", movie,"the name of the movie is:",actor, end )

# ----------
a = 3
b = 4
c = 2*((a**2-(b/2)**2))**0.5
area = (b*c)/2
diameter = a*4
print(c, area, diameter)

#---------------
some_str = "dsafdabfdacg"
if some_str [5] == "a" and some_str [6] == "b" and some_str [-2] == "c":
    print ("yes")
else:
    print ("no")

# ----------------

x = 3
y = 4
z = 1
if (x+y) > z and (x+z) > y and (y+z) > x:
    print((((x+y+z)*(x+y-z)*(y+z-x)*(z+x-y))**0.5)/4)
else:
    print ("this is not a triangle")

z = 3
print (x+z+y)

#--------------

a1 = 10
a2 = 20
n = 4
q = a2/a1
an = a1 * q**(n-1)
print (n*an)


#----------------
(donuts) = int(input("please enter number of donuts : " ))
if donuts <= 5:
    print("number of donuts :" "low" )
elif donuts <= 10:
    print ("number of donuts :" "medium" )
else:
    print ("number of donuts :" "high" )

#--------------

grade = int(input ("please enter your grade : "))
year = int (input ("please enter your year : "))
if grade >= 92 and year == 1 or year == 2:
    print ("wonderful")
elif grade >= 97 and year ==3 or year == 4:
    print("wonderful")
elif grade >= 75 and year == 1 or year == 2:
    print ("very good")
elif grade >= 80 and year == 3 or year == 4:
    print("very good")
elif grade >= 65 and year == 1 or year == 2:
    print ("normal")
elif grade >= 70 and year == 3 or year == 4:
    print("normal")
else:
    print ("weak")

#--------------

ticket = input("please enter your kind : ")
price = input("please enter the price : ")
credits = input("please enter your card : ")
if ticket == "men" and price == 40 and credits == "platinum":
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
    print("the price is : " ,(price*0.25))
elif ticket == "old" and price == 30 and credits == "movie":
    print("the price is : " ,(price*0.25))
elif ticket == "older" and price == 20 and credits == "movie":
    print("the price is : ",(price*0.25))
else:
    ticket == "older" and price == 20 and credits == "movie"
print("the price is : " ,(price*0.25))

