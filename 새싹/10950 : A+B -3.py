t = int(input())

for _ in range(t):  #t만큼 반복 변수가 없으므로 언더바(_)로 표시한다
    a, b = map(int,input().split())    #for문 안에서 반복되도록 해야 한다
    print(a+b)
