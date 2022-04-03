n = int(input())
glass = []
#n + 1 번째 줄까지 포도주 잔의 양의 순서
for i in range(1, n+1) :
    glass.append(list(map(int, input().split())))

max_glass = 0
for i in range(1, n+1) :
    max_glass = 1

#포도양을 최대로 구할수 있는 부분
for i in range(1, n+1) :
    if i < max_glass :
         max_glass[i] = max_glass[i - 1]

    else :
         max_glass[i] = (max_glass[i - 2]) - (max_glass[i - 3])
    
    
print(max_glass[n])

---------------------------------------------------

n=int(input())
array=[0]*10000
for i in range(n):
  array[i]=int(input())

d=[0]*10000
d[0]=array[0]
d[1]=array[0]+array[1]
d[2]=max(array[2]+array[0], array[2]+array[1], d[1])
for i in range(3,n):
  d[i]=max(array[i]+d[i-2], array[i]+array[i-1]+d[i-3], d[i-1])

print(max(d))
