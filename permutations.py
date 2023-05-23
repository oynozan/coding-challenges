s = int(input())
odds = []
final = []
result = ""
if (s < 4 and s != 1):
	print("NO SOLUTION")
else:
	for i in range(1,s+1):
		if i%2==0:
			final.append(i)
		else:
			odds.append(i)
	final += odds

	for j in final:
		if j != final[-1]:
			result += str(j) + " "
		else:
			result += str(j)

	print(result)