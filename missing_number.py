sayi1 = int(input())
list1 = input()
result = False

list1 = list(map(int, list1.split()))
list1.sort()
if sayi1 == 2 and list1[0] == 2:
	print(1)
else:
	for i in range(len(list1)-1):
		if list1[i]+1 != list1[i+1]:
			print(list1[i]+1)
			result = True
			break
	if (not result): print(sayi1)