


lst = []
lst.append(10)
lst.append(20)
lst.insert(1, "Some String")
lst.remove(10)
print(lst)


mySet = {5, 20, 30}
if 5 in mySet:
    print("Has 5")
# --------------

def OmerList (lst):
    result = []
    for x in lst:
        if x %2 == 0:
            result.append(x)

    return result


print(OmerList([645,4654,2]))

#-------
def azert (n) :
    result = 1
    while n > 1:
        result = result * n
        n = n - 1

    return result


print(azert(5))







