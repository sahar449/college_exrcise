
numbers = [54,354,2.3]
minimum = numbers [0]
for element in numbers:
	if element < minimum:
		minimum = element
print(minimum)

# question 2
A = [351,44]
sum = 0
counter = 0
for element in A:
	sum = sum + element
	counter = counter + 1
print(sum / counter)

# question 3
B = [4,8,12,15]
for i in range(2, len(B)) :
	if B[i] == B[i-1] + B[i-2]:
		print("True")
	else:
		print(i)
# question 7


def sum_according_to_advisor (lst):
	result = [0, 0, 0, 0]
	for x in lst:
		if x %2 == 0:
			result [0] = result[0] + x
		elif x %3 == 0:
			result [1] = result[1] + x
		elif x %5 == 0:
			result[2] = result[2] + x
		else:
			result[3] = result[3] + x

	return result


A = [1, 2, 3, 10, 20, 55]
B = [2, 3]

res1 = sum_according_to_advisor(A)
res2 = sum_according_to_advisor(B)

print(res1)

# question 8

def sumOfDigits(n):
	result = 0
	while n > 0:
		result += n % 10
		n = n // 10

	return result


def final_digit_sum(num):
	while num > 9:
		num = sumOfDigits(num)

	return num


print(final_digit_sum(9875))

# -------------



