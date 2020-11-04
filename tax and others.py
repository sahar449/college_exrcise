tax
salary = int(input(("please enter your salary : ")))
if salary <= 4000:
    print(salary*0.9)
elif salary <= 8000:
    print(4000*0.9 + (salary-4000)*0.8)
elif salary <= 12000:
    print(4000*0.9 + 4000*0.8 + (salary-8000)*0.7)
else:
    print(4000*0.9 + 4000*0.8 + 4000*0.7 + ((salary-12000)*0.6))

#----------
def factorial (n):
    s = 1
    for i in range(1, n+1):
        s = s * i
    return s

print(factorial(5))





#---------
lst = [0,1,2,3,4]
for i in range(len(lst)):
    lst[i] = lst[i] * 100
lst[2] = 315
lst[4] = lst[4] + 150
print(sum(lst))


# #-----------
# lst = [0,1,2,3,4],[0,1]
# for i in range(len(lst)):
#     lst[i] = lst[i] * 100
#     for j in range(len(lst)):
#         lst[j] = lst[j] * 100
# lst[2, 0] = 31
# lst[4, 1] = lst[4, 1] + 150
# print(lst)

i = 1
while i <=10:
    i= i + 1
    print(i)
