#--------
def find_minimun (lst1, lst2):
    s = 0
    counter = 0
    for i in range(len(lst1)):
        s = s + lst1[i]
        counter = counter + 1
    lst1 = s /counter
    for j in range(len(lst2)):
        s = s + lst2[j]
        counter = counter + 1
    lst2 = s / counter

    return min(lst1, lst2)

new_lst1 = [1, 2]
new_lst2 = [2, 3]
print(find_minimun(new_lst1, new_lst2))

#-------------

def if_all_letter_are_the_same (letters):
    for i in range(len(letters)-1):
        if letters[i] != letters[i+1]:
            return False
    return True

def if_all_letter_are_the_same (letters):
    firstChar = letters[0]
    for i in range(1, len(letters)):
        if firstChar != letters[i]:
            return False
    return True




print(if_all_letter_are_the_same("dsaf"))
print(if_all_letter_are_the_same('aa'))

#------------------
def max_grade_of_students (grades, students):
    maxi = grades[0]
    for i in range(len(grades)):
        if maxi < grades[i]:
            maxi = grades[i]
    for j in range(len(students)):
        students[j] == maxi

    return students[j]


grades = [80, 10, 90, 92]
students = ['moshe', 'jakov', 'omer', 'idan']
print(max_grade_of_students(grades, students))


def factor_grades (grades):
    factor = 5
    for i in range(len(grades)):
        if grades[i] > 60:
            factor = grades[i] + factor
    return factor
grades = [10,60,70]
print(factor_grades(grades))

#---------------

def k_indetical_letters (rep_str, k):
   for i in range(len(rep_str)-k):
       kLetters = rep_str[i: i+k]
       if if_all_letter_are_the_same(kLetters):
            return kLetters

   return None

print(k_indetical_letters("asd0",4))
print(k_indetical_letters("aaaasdafsdafsdafsaaadf",3))
print(k_indetical_letters("g",4))

#------------------------
def switch_list(lst,i,j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

l = [100, 200, 55, 66 ,10.1]
switch_list(l, 1, 4)
print(l)


def sumNumDigits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10

    return s


def checkID(id):
    if id < 100000000 or id > 999999999:
        return False

    s = 0
    while id > 0:
        digit = id % 10
        if digit % 2 == 0:
            s += sumNumDigits(digit*2)
        else:
            s += digit
        id = id // 10

    return s % 10 == 0


print(checkID(387654321))

def fibo (numbers):
    for i in range(len(numbers)):
        if numbers[i-1] == numbers[i-2] and numbers[i-3]:
            return False

    else:
        return True

numbers = [1, 2, 3]
print(fibo(numbers))
print(fibo([1, 2, 3, 5]))


#------------
def mean_if_bigger_then_3 (lst):
    s = 0
    counter = 0
    for i in range(len(lst)):
        s = s + lst[i]
        counter = counter + 1
    if lst[i] > 3:
        return s/ counter

print(mean_if_bigger_then_3([4, 5]))
print(mean_if_bigger_then_3([1, 2, 3]))

