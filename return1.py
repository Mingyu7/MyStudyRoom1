def ogamdo(num):
    for i in range(1,num+1):
        print('제 {0}의 아해'.format(i))
        if i ==5:
            return ##반환 데이터없이는 함수 종료 의미로 사용

def print_something(*args):
    for s in args:
        print(s)
                ##함수를 중간에 종료 시킬 필요없을때는 return 생략함

ogamdo(3)
print_something(1,2,3,4)
print('\n')
def scope_test():
    global a # global 하면 지역변수의 생성을 막는다  a는 함수안에 전역변수로 사용된다
    a = 1
    print('a: {0}'.format(a))

a=0 
scope_test() #변수 a를 0으로 초기화 했지만 함수 호출되면 함수 a=1 실행되서 1로 출력
print('a: {0}'.format(a))