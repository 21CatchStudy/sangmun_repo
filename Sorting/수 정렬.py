#insertion sort, count sort(x), selection sort, quick sort(x) 

array = []
a = int(input())

# a = 5 


#선택정렬 
for i in range(a) :
    array.append(int(input()))
# a = 1,2,3,4,5,5

array = sorted(set(array))
    
#리스트를 오름차순    



array = sorted(set(array))
for i in array :
    print(i)
