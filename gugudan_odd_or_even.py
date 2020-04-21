# def odd_even(a):
#     if a % 2 == 0:
#         print("짝수")
#     if a % 2 == 1:
#         print("홀수")

# odd_even(2)

# 실습2번
odd_num = [1,3,5,7,9]
even_num = [2,4,6,8]

def gugudan_odd():
    for i in odd_num:
        for j in range(1,10):
            print("%d x %d = %d" % (i,j,i*j))
def gugudan_even():
    for i in even_num:
        for j in range(1,10):
            print("%d x %d = %d" % (i,j,i*j))   

def gugudan_odd_or_even(a):
    if a % 2 == 0:
        print(gugudan_even())
    if a % 2 == 1:
        print(gugudan_odd())

gugudan_odd_or_even(4)


# 실습 3번
def num_mul(p):
    num_p = range(1,(p+1))
    for r in num_p:
        for q in range(1,10):
            print("%d x %d = %d" % (r,q,r*q))
num_mul(5)
