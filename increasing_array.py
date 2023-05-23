size = int(input())
l = list(map(int,input().split()))
result = 0
for i in range(1,size):
	if l[i] < l[i-1]:
		result+=l[i-1]-l[i]
		l[i]+=l[i-1]-l[i]
print(result)