# ------
def sumFrom(x):
    sum = 0
    for element in range(x):
        sum = sum + element

    return sum


print(sumFrom(5))
#-------------------

def list (lst1, lst2):
    sum = 0
    counter = 0
    for element in range(list):
        sum = sum +element
        counter = counter + 1
    return sum / counter



#------------
lst1 = [1,2]
s = 0
counter = 0
for element in lst1:
    s = s + element
    counter = counter + 1

print(s / counter)

#--------
def pitagores (a, b):
    return a**2+b**2

a = 3
b = 4
print(pitagores(a, b))
#----------
a = 5
b = 8
print(pitagores(a, b))

#---------
def cal (lst1 , lst2):
    mean1 = sum(lst1) / len(lst1)
    mean2 = sum(lst2) / len(lst2)
    return min(mean1, mean2)


lst1 = [5,10]
lst2 = [1,2]
print(cal(lst1,lst2))


#-------------

def getMaximum (lst):
    maxim = lst[0]
    for element in lst:
        if element > maxim:
            maxim = element

    return maxim


lst = [34,324]
print(getMaximum(lst))

#-----------------


def findMaxStudents (grades, names):
    maxGrade = getMaximum(grades)
    students = []
    for i in range(len(grades)):
        if grades[i] == maxGrade:
            students.append(names[i])

    return students

grades = [10,20,55,54,86,24,86]
names = ["moshe","or","efi","sami","shlomo","ron","eran"]
print(findMaxStudents(grades, names))

#---------
def factorAndGrades (grades , factor):
    for i in range(len(grades)):
        if grades[i] > 60:
            grades[i] = grades[i] + factor
            if grades[i] > 100:
                grades[i] = 100


grades = [50, 61, 99, 100, 60]
factorAndGrades(grades, 10)
print(grades)


#--------------
def iflAllLetterAreTheSame (str1):
    for i in range(len(str1)):
        if str1[i] != str1[i-1]:
            return False

    return True


print(iflAllLetterAreTheSame("aaaavaaa"))
print(iflAllLetterAreTheSame("aaaaaaaab"))
print(iflAllLetterAreTheSame("baaaaaaa"))
print(iflAllLetterAreTheSame("aaaaaaaa"))



