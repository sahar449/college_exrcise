

def find_minimum(lst):
    minimum = lst[0]
    for element in lst:
        if element < minimum:
            minimum = element
        return minimum


    print(find_minimum([1, 4, 2.3]))


def find_minimun2(lst):
        minimum = lst[0]
        i = 1
        while i < len(lst):
            if lst[i] < minimum:
                minimum = lst[i]
            i += 1

        return minimum


# ----------------
# ליצור רשימה של מספרים
# לחשב את ערכם הממוצע של המספרים חיבור של המספרים חלקי כמות המספרים
def find_mean(lst1):
    s = 0
    counter = 0
    for element in lst1:
        s = s + element
        counter = counter + 1
    return s / counter

print(find_mean([5,6]))

#---------------------
# לעשות רשימה במשתנה B
# לבדוק האם כשמחברים שתי מספרים עוקבים מגיעים את המספר השלישי, אם לא להדפיס את המספר השלישי

def is_all_letter_the_same (str_a):
    for i in range(len(str_a)):
        if str_a[i] != str_a[i-1]:
            return False
    else:
        return True

str_a = "dsafadsf"
print(is_all_letter_the_same(str_a))
str_a = "aa"
print(is_all_letter_the_same(str_a))

# def find_maximum (lst):  לא הצלחתי,לדבר עם עומר
#     maximum = lst[0]
#     for element in lst:
#         if element < maximum:
#             maximum = element
#         return maximum
#
#
# print(find_maximum([5, 6]))
#-----------
# maxi = 1, element = 5

def find_minimum(lst):
    minimum = lst[0]
    for element in lst:
        if element < minimum:
            minimum = element
        return minimum

print(find_minimum([1, 4, 2.3]))

#לעשות פונקציה עם שתי רשומות
# למצוא את המספר הכי גדול ברשימה
# def max_number1 (lst1, lst2):
#     max_number = lst1[0], lst2[0]
#     for i in range(len(lst1)):
#         if max_number < i:
#             max_number = i
#     for j in range(len(lst2)):
#         if max_number < j:
#             max_number = j
#     return max_number
#
# max_number = [0],[1]
# print(max_number1(max_number))

# לעשות פונקציה שמחברת את כל המספרים, עד שמגיעים למספר אחד

def final_digit_sum (num):
    while num > 9:
        num = sumDigits(num)

    return num


def sumDigits(num):
    s = 0
    while num != 0:
        s += num % 10
        num = num // 10
    return s

print("Sum: ", final_digit_sum(9785))


# לעשות ממוצע של שתי רשימות ואז להחזיר את המספר הנמוך מביניהם
def mean_func (lst1, lst2):
    mean1 = calc_list_mean(lst1)
    mean2 = calc_list_mean(lst2)
    return min(mean1, mean2)

def calc_list_mean(lst):
    s = 0
    counter = 0
    for element in lst:
        s = s + element
        counter = counter + 1

    return s / counter


def calcListMean(lst):
    return sum(lst) / len(lst)


lst1 = [4, 5]
lst2 = [5, 6]
print(mean_func(lst1, lst2))


# מתוך רשימה של ציונים למצוא את הציון הכי גבוהה
def max_grade (lst):
    maxi = lst[0]
    for i in range(len(lst)):
       if maxi < lst[i] :
            maxi = lst[i]

    return maxi


lst = [10,11]
print(max_grade(lst))

def max_grade_for_each (lst):
    maxi = lst[0]
    for element in lst:
        if maxi < element:
            maxi = element

    return maxi
lst = [5,6]
print(max_grade_for_each(lst))

#--------------
def oppsit (num):
    strNum = str(num)
    dotIndex = strNum.index(".")
    strNum = strNum[dotIndex+1:len(strNum)] + "." + strNum[0:dotIndex]
    return float(strNum)


print(oppsit(11.62))