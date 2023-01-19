def factorial(n): #재귀함수 사용
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))
