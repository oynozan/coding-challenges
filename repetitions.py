a=input()
record = 1
records = []
for i in range(len(a)-1):
	if a[i] == a[i+1]:
		record+=1
	else:
		records.append(record)
		record = 1
records.append(record)
records.sort()
print(records[-1])