n= int(input())
result=1

if n>=0:
    for i in range(1,n+1): #1부터 n+1 까지 출력
        result*=i          #결과는 i를 모두 곱한 값
print(result)
