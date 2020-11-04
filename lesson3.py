

lst = []
lst = [1, "gerge", 6, True]
lst.clear()
lst.append(5)
lst = list(range(1, 11))
print(lst)
print("The length of the list is : ", len(lst))
print("The sum of list is: ", sum(lst))

sum = 0
for num in lst:
    sum += num

print(sum)

sum = 0
for i in range(0, len(lst)):
    sum += lst[i]

print(sum)

# -----
lst = list(range(0, 101,5))
print(max(lst))

maximum = lst[0]
for num in lst:
    if num > maximum:
        maximum = num

print(maximum)

# --------
B = [2, 1, 3, 4, 9, 13]
answer = True
for i in range(2, len(B)):
    if B[i] != B[i-1] + B[i-2]:
        answer = False
        break

print(flg)

