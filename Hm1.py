#מעוויין

def line (a,b):
    c =  2*((a**2-(b/2)**2))**0.5
    return c

print(line(3,4))
print(line(7,10))


# a = 3
# b = 4
# c = 2*((a**2-(b/2)**2))**0.5
# print("The lenght of c is : " , c)
#
# Aera = (b*c)/2
# print ("Area is : " , Aera)
#
# d = a*4
#
# print(d)

some_str = "sdafsdaf"
if some_str[5] == "a" and some_str[6] == "b" and some_str[-2] == "c":
    print("Yes")
else:
    print("No")
some_str1 = "asdfvabco"
if some_str1[5] == "a" and some_str1[6] == "b" and some_str1[-2] == "c":
    print("Yes")
else:
    print("No")
#----------------------------- לא הצלחתחי,הסתכלתי בפתרון 4

x = 5
y = 5
z = 5

if (x+y) > z and (x+z) > y and (y+z) > x:
    print("Area: ", (((x+y+z)*(x+y-z)*(y+z-x)*(z+x-y))**0.5)/4)
    print("Circumference: ", x+y+z)
else:
    print("Cannot create triangle from those edges")

# #---------------- 5

def number4 (a1, a2, n):
    q = a2/a1
    return a1*(q**(n-1))


print(number4(3,15,5))

def number4a (a1, a2, n):
    q = a2/a1
    for i in range(n-1):
        a1 = a1*q
    return a1

print(number4a(3,15,5))
#---------------------


def blood (donor, recipient):
    bloodTypes = ["O","A","AB","B"]
    if donor not in bloodTypes or recipient not in bloodTypes:
        return "Invalid Input"

    if donor == recipient or recipient == "AB" or donor == "O":
        return "Yes"
    else:
        return "No"


# donor = input("Enter the type Blood of donor: ")
# rec = input("Enter the type Blood of recipient: ")
# print("The result is: ", blood(donor, rec))

#---------------
def number6 (str1: str):
    if str1 is None or len(str1) < 2:
        return False

    return len(str1) % 2 == 0 and str1[0] == str1[-1] and str1[1] == str1[-2] and str1[len(str1)//2-1] in ["G", "g"]


print(number6("abgtba"))

def number7 (str1: str):
    result = str1[-1] + str1[1]
    if str1[2].isdigit():
        result = result + str(int(str1[2])+1)
    else:
        result = result + str1[2]

    result = result + str1[3:-1]
    result = result + str1[0]
    return result


print(number7("Tg5yp"))

# question 6
donor = input("please enter you donor : ")
recipient = input("please enter you recipient : ")

types = ["AB", "A", "B", "O"]
if donor not in types or recipient not in types:
    print("Invalid Input")


if donor == recipient or recipient == "AB" or donor == "O":
    print("Yes")
else:
    print ("No")
# question 6

str1 = "asdgfdag"
if len(str1)%2 == 0 and str1[0] == str1[-1] and str1[1] == str1[-2] and str1[(len(str1)+1) // 2] in ["g", "G"]:
    print("Yes")
else:
    print ("No")

#-----------
myList = [2, 2, 3, 10]
print(sum(myList))
