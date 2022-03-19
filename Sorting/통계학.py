https://www.acmicpc.net/problem/2108

import sys
from collections import counter
n = int(sys.stdin.readline())
nums = []
for i in range (n) : 
    nums.append(int(sys.stdin.readline())) #임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
nums.sort()
numbers = counter(nums).most_common(2) # 빈도수가 높은 2개의 수
print(round(sum(nums)/ n)) #N개의 수들의 합을 N으로 나눈 값
print(nums[n // 2]) 

if len(numbers) > 1 : # 1이상 일때
    if numbers[0][1] == numbers[1][1]: # 0과1 1과1 사이의 2번째
        print(numbers[1][0]) #2번째인 1 0 을 출력

    else :
        print(numbers[0][0]) #그렇지 않은 경우 가장 빈도수 높은 수를 출력

else :
    print(numbers[0][0])

print(max(nums) - min(nums)) #최댓값 - 최솟값
