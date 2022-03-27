#https://www.acmicpc.net/problem/1181

N = int(input())
word = []

for _ in range(N):
    word.append(input())

    
word = list(set(word)) #set으로 중복x 
word.sort(key=lambda x : (len(x),x)) #sort 정렬 lambda 선언

print("\n".join(word)) #줄바꿈
