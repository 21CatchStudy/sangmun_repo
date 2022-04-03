#insertion sort, count sort(x), selection sort, quick sort(x) 

n=int(input())
num=[]

for _ in range(n):
    x = int(input())
    num.append(x)

for i in sorted(num):
    print(i)
