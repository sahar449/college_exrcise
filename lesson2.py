name = input('please insert your name: ')
if len(name) >= 4:   # len(str) = מחזיר את האורך של המחרוזת
    print(name[0:4])

print("the last char of the name is :", name[-1])

# -------------

age = input('please enter your age : ')
if age.isnumeric():   # str.isnumeric() = בודק האם החחרוזת מכילה רק ספרות ולכן אפשר להמירה למספר
    age = int(age)
    print(5)
else:
    print('invalid age')


num = int(input('enter num :'))
print(num % 10)  # מודולו 10 מחזיר את הספרה האחרונה במספר (הספרה החלשה)
print(num // 10)  #  דיב 10 מחזיר הכל ללא הספרה האחרונה (מוחק אותה)


# -----

if (num > 20 and age > 20) or len(name) > 5:
    print("hello")


# ---------- תירגול 2 -------------


s = input("please enter string : ")
length = len(s)
middle = length // 2
middleChar = s[middle].upper()

o = s[0:middle] + middleChar + s[middle+1:]
print(o)


# ----------

grade = int(input("enter your grade : "))
year = int(input("enter your year : "))

EXCELLENT_RATE = 92
VG_RATE = 75
GOOD_RATE = 65

if year == 3 or year == 4:
    EXCELLENT_RATE += 5
    VG_RATE += 5
    GOOD_RATE += 5

if grade >= EXCELLENT_RATE:
    print ('excellent')
elif grade >= VG_RATE:
    print('very good')
elif grade >= GOOD_RATE:
    print('good')
else:
    print('weak')

# ---------
donuts = int(input('number of donuts: '))
if donuts < 5:
    print('number of donuts: little ')
elif donuts < 10:
    print('number of donuts: middle ')
else:
    print('number of donuts: a lot!')

# ---------
age = int (input('please write you age : '))
creditCard = int(input('the price is : '))
member = input('y or n : ')



