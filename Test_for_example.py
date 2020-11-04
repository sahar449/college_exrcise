# question 3a
def check_if_sorted (lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False

    return True

print(check_if_sorted([1,3,5]))
print(check_if_sorted([5,1,5.6]))


# question 3b
def insert_numbers(lst, numbers):
    if (check_if_sorted(lst) == False):
        print("Error - your list is not sorted")
        return

    for i in range(len(numbers)):
        for j in range(len(lst)):
            if numbers[i] > lst[j] and (j == len(lst)-1 or numbers[i] < lst [j+1]):
                lst.insert(j+1, numbers[i])
                break



lst = [1, 5, 10]
insert_numbers(lst, [8, 80])
print(lst)

def float_to_time(f):
    hour = int(f)
    minutes = (f - hour) * 60

    return (hour, minutes)


print(float_to_time(7.375))


#----------
s = 1
for i in range(5, 60):
    if s > 40000000000:
        break
    s = s * i

print(s)
#-----------------
def find_number (people,tele):
    for i in range(len(people)):
        print(people[i], tele[i])


tele_people = [['moshe', 'osher'], ['052', '050']]


print(find_number(tele_people[0], tele_people[0]))

# ---------------
def find_number1 (people,tele):
    print(people[0], tele[1])

peopel = ['or', 'dor']
tele = ['053', '056']

print(find_number1(peopel,tele))

#-------
def pitago (a, b):
    c = a**2 + b**2
    return c

print(pitago(5,5))
print(pitago(1,1))
#----------


def all_letter_the_same (letters):
    for i in range(len(letters)):
        if letters[i] != letters[i+1]:
            return True

print(all_letter_the_same("a1"))
