num = int(input())
result = ""

while num != 1:
	result += str(num)+" "
	if (num%2)==0:
		num = num // 2
	else:
		num = num * 3 + 1

print(result+"1")