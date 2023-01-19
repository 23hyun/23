while True:  #True 대신 1로 해도 된다
    a,b=map(int,input().split())
    
    if a==0 and b==0:      #a와 b가 0이면 반복문을 탈출하고 a+b를 출력한다
        break
    print(a+b)
