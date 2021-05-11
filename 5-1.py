# 분리언 boolean type
# 참(true)과 거짓(false) 표현

x = True  # ""을 사용안해도 True, False이 나옴
y = False
print(x)
print(y) 

a = 3
b = 4
if a>b: # :을 사용하면 들여쓰기가 된것은 이 문장 아래 있는 것이다 
    print("a가 크다") # False이기 때문에 출력이 않됨 
if b>a:
    print("b가 크다")