import math

s = 0
for element in range(0, 100):
    if element % 3 == 0:
        s = s + element

print(s)

# -------
s = 0
for element in range(0, 100, 3):
    s = s + element

print(s)

# -------
print(sum(range(0, 100, 3)))


def someFunc(lst):
    lst[0] = 999999


# Python  Memory Model
myList = [1, 2, 3]
s2 = myList.copy()
s2.append(500)
print(myList)
print(math.pi)

s1 = [1, 2, 3]
s2 = [1, 2, 3]
isEquals = s1.__eq__(s2)
print(isEquals)


# --------
def polindrom(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False

    return True


print(polindrom("r"))


# --------
def validate_password(pass1: str, pass2: str):
    if pass1 == pass2 and len(pass1) > 6:
        existsLetter = False
        existsNum = False
        for i in range(len(pass1)):
            if pass1[i].isdigit():
                existsNum = True
            elif pass1[i] >= "a" and pass1[i] <= "z" or pass1[i] >= "A" and pass1[i] <= "Z":
                existsLetter = True

        if existsLetter and existsNum:
            return True

    return False


print(validate_password("1234567", "1234567"))


# -------
def mySum(x, y):
    return x + y


print(mySum(100, 200))


# ------
def sumFrom(x):
    sum = 0
    for element in range(x):
        sum = sum + element

    return sum


print(sumFrom(5))


# ---
def power(x, y):
    return x ** y


print(power(2, 5))


# ----------
def sumBetween(x, y):
    return sum(range(x, y + 1))


print(sumBetween(2, 5))


# ---------
def list (x,y):
    sum = 0
    counter = 0
    for element in len(list):
        sum = sum + element
        counter = counter + 1
        return (sum / counter)

    x = [4,1]
    y = [5,2]

    print(x)
