>>> l1 = [[1,2,3],[4,5,6]]
>>> len(l1)
2
>>> l1[0]
[1, 2, 3]
>>> l1[0][0]
1
>>> l1[0][1]
2
>>> l1[0][2]
3
>>> l1[1][0]
4
>>> for i in range(0,2) :
	for j in range(0,3) :
		print(l1[i][j], end = ' ')   # 위치기반
	print()

	
1 2 3 
4 5 6 
>>> l1
[[1, 2, 3], [4, 5, 6]]
>>> for i in l1 :
	for j in i :
		print(j, end = ' ')   # 객체기반
	print()

	
1 2 3 
4 5 6

>>> l2 = [[1,2],[3,4,5],[6,7,8,9]]
>>> for i in l2 :
	for j in i :
		print(j, end = ' ')  # 이런 리스트는 위치기반으로 풀수가 없다. 
	print()                      # range로 열을 고정할 수가 없음. 객체기반으로 풀어야함.

	
1 2 
3 4 5 
6 7 8 9

while 1 : while = true   # 무한반복실행한다는 뜻.


# 세트 : 딕셔너리의 키만 저장해 놓은 자료구조로 값은 중복 저장 될 수 없다.
# 1. 세트 생성
s1 = {1,2,3,3,4}   # 1,2,3,4만 저장됨(중복제거)
l1 = [1,2,2,3,3]
set(l1)   # 리스트의 unique값 출력

# 2. 세트의 집합연산자(리스트, 튜플, 딕셔너리 사용 불가)
s1 = {1,2,3,4}
s2 = {3,4}

s1 & s2               # 교집합(연산자)
s1.intersection(s2)   # 교집합(매서드)

s1 | s2        # 합집합(연산자)
s1.union(s2)   # 합집합(매서드)

s1 - s2             # 차집합(연산자)
s1.difference(s2)   # 차집합(매서드)

>>> {1,2,3,3}
{1, 2, 3}
>>> {'a' : 1, 'b': 2, 'a' : 10}
{'a': 10, 'b': 2}
>>> # 이렇게 같은키를 중복기입하면, 마지막 값이 파싱된다.
>>> # 세트에는 중복저장 불가.

>>> l1 = [1,2,3,3]
>>> set(l1)
{1, 2, 3}

# list comprehension(리스트 내포 표현식)
# 리스트 특성상 벡터연산(반복적용)이 안되는 점을 비교적 간단하게 표현
# else값 생략 가능

# 1. 문법
[리턴값 for 반복변수 in 범위 또는 대상]
[리턴값 for 반복변수 in 범위 또는 대상 if 조건]   # else값 출력 불가
[참리턴값 if 조건 else 거짓리턴값 for 반복변수 in 범위 또는 대상]   # else값 출력 가능

# 2. 기타 반복 적용과 비교
# 예제) l1 = [1,2,3,4,5], l1 + 1 리턴
# 1) for문
>>> l1 = [1,2,3,4,5]
>>> list1 = []
>>> for i in l1 :
	list1.append(i + 1)

>>> list1
[2, 3, 4, 5, 6]

# 2) map
>>> list(map(lambda i : i+1, l1))
[2, 3, 4, 5, 6]

# 3) list comprehension
>>> [i+1 for i in l1]
[2, 3, 4, 5, 6]


# 예제) l1 = [1,2,3,4,5], 짝수만 리턴(else 생략)
# 1) for문
>>> list1=[]
>>> for i in l1 :
	if i % 2 == 0 :
		list1.append(i)

		
>>> list1
[2, 4]

# 2) map
>>> list(map(lambda i : i if i % 2 == 0, l1))
SyntaxError: invalid syntax   # 삼항다항식에서는 else를 생략 불가능. R에서 ifelse와 동일.

>>> list(map(lambda i : i if i % 2 == 0 else None, l1))
[None, 2, None, 4, None]   # 이 표현이 최선이다.

# 3) list comprehension
>>> [i for i in l1 if i % 2 == 0]
[2, 4]


>>> [i for i in l1 if i % 2 == 0 else 0]
SyntaxError: invalid syntax
>>> [i if i % 2 == 0 else 0 for i in l1]
[0, 2, 0, 4, 0]
>>> # 홀수를 0으로 표현.
>>> 
>>> # 삼항연산자, 삼항다항식
>>> a1 = 1
>>> 1 if a1>0 else -1
1


# 예제) l1 = [1,2,3,4,5], 짝수는 1, 홀수는 0 리턴(else 포함)
# 1) for문
>>> l1 = [1,2,3,4,5]
>>> list1 = []
>>> for i in l1 :
	if i % 2 == 0 :
		list1.append(1)
	else :
		list1.append(0)

		
>>> list1
[0, 1, 0, 1, 0]

# 2) map
>>> list(map(lambda i : 1 if i % 2 == 0 else 0, l1))
[0, 1, 0, 1, 0]

# 3) list comprehension
>>> [1 if i % 2 == 0 else 0 for i in l1]
[0, 1, 0, 1, 0]


# 연습문제)
# sal = ['9,900', '25,000', '13,000']
# addr = ['a;b;c', 'aa;bb;cc', 'aaa;bbb;ccc']
# comm = [1000, 1600, 2000]

# 1) sal의 10% 인상값 출력
sal = list(map(lambda x : [int(i.replace(','.''))*1.1 for i in sal], sal))

# for
sal1 = []
for i in sal :
    sal1.append(i*1.1)
	
# map
list(map(lambda i : i*1.1, sal))

# list comprehension
[i*1.1 for i in sal]
[round(int(i.replace(','.''))*1.1) for i in sal]


# 2) addr에서 각 두번째 값(b,bb,bbb) 출력
# for
addr1 = []
for i in addr :
    addr1.append(i.split(';')[1])

# map
list(map(lambda i : i.split(';')[1], addr))

# list comprehension
[i.split(';')[1] for i in addr]


# 3) comm이 1500보다 큰 경우 'A', 아니면 'B' 출력
# for
comm1 = []
for i in comm :
    if i  > 1500 :
        comm1.append('A')
    else :
        comm1.append('B')

# map
list(map(lambda i : 'A' if i > 1500 else 'B', comm))

# list comprehension
['A' if i > 1500 else 'B' for i in comm]


# deep copy : 원본의 객체와 완벽하게 분리되는(메모리상 위치) 형식의 복사
# 파이썬에서는 대체적으로 deep copy 수행이 되지 않으므로 주의
l1 = [1,2,3,4,5]
l2 = l1   # l1과 똑같은 객체 생성

l2[0] = 10   # l2의 첫 번째 원소 변경
l2           # l2 변경 확인
l1           # l2 변경 확인

# 1. deep copy 발생 여부 확인 : 주소가 서로 같다면 얕은복사가 수행된 것.
# 즉, deep copy가 발생하지 않은 것.
id(l1)   # l1 객체의 주소
id(l2)   # l2 객체의 주소
>>> v_comm = comm
>>> comm[0] = 10000
>>> comm
[10000, 1600, 2000]
>>> v_comm
[10000, 1600, 2000]


id(object)   # 주소값을 확인한다. deep copy가 발생하지 않으면 주소가 같다.
>>> id(comm)
1281575699016
>>> id(v_comm)
1281575699016

# 2. deep copy 수행
l3 = l1[:]

>>> v_comm2 = comm[:]
>>> comm[1] = 16
>>> comm

>>> id(comm)
1281575699016
>>> id(v_comm2)
1281578637192
[10000, 16, 2000]
>>> v_comm2
[10000, 1600, 2000]

# zip으로 두개의 변수를 묶었을 때,  zip(l1, l2).
# l1의 원소가 3개(len(l1)=3), l2가 5개(len(l2)=5) 인 경우
# 두 리스트는 원소의 갯수가 작은 쪽에 맞춰서 수행이된다.

>>> f_split = lambda data, sep, vord = 0 : data.split(sep)[vord]
>>> def f_split2(data, sep, vord = 0) :
	return data.split(sep)[vord]

>>> f_split2('a;b;c', ';')
'a'
>>> f_split2('a;b;c', ';',1)
'b'
>>> f_split2('a;b;c', ';', 1)
'b'

>>> def f_split2(data, sep = ';', vord) :
	return data.split(sep)[vord]
SyntaxError: non-default argument follows default argument
>>> # 중간에 디폴트값을 갖게하면 그 이후 옵션들도 디폴트 값을 부여한다.
>>> # 만약 디폴트값을 한개만 넣고 싶으면 해당 옵션을 맨 뒤로 뺀다.
>>> def f_split2(data, sep = ';', vord = 0) :
	return data.split(sep)[vord]

>>> def f_split2(data, vord, sep = ';') :
	return data.split(sep)[vord]


# def를 통한 함수의 정의
def my_func1(x,y,z) :    # 인자의 default값 지정은 중간 인자만은 불가
    return x + y + z     # 이후 선언된 모든 인자가 default값을 갖거나
                         # 맨 마지막 인자만 갖는 형식으로 지정
my_func1(1,2,3)


def my_func1(x,y=0,z) :   # default 값(y=0) 전달 불가
    return x + y + z

def my_func1(x,z,y=0) :   # default 값(y=0) 전달 가능
    return x + y + z

# 예제) 계산기 함수
def f_calc(v1,v2,op='+') :
    if op == '+' :
        result = v1+v2
    elif op == '-' :
        result = v1-v2
    elif op == '*' :
        result = v1*v2
    elif op == '/' :
        result = v1/v2
    else :
        print('type error : 연산불가')

    return result

>>> f_calc(1,2,'**')
type error : 연산불가
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    f_calc(1,2,'**')
  File "C:/Users/KITCOOP/Desktop/asdfdg.py", line 13, in f_calc
    return result
UnboundLocalError: local variable 'result' referenced before assignment



def f_calc(v1,v2,op='+') :
    result = 0
    if op == '+' :
        result = v1+v2
    elif op == '-' :
        result = v1-v2
    elif op == '*' :
        result = v1*v2
    elif op == '/' :
        result = v1/v2
    else :
        print('type error : 연산불가')

    return result

>>> f_calc(1,2,'**')
type error : 연산불가
0


def f_calc(v1,v2,op='+') :
    result = 'type error : 연산불가'   # 리턴값이 존재하지 않는 경우 에러 방지용 선언
    if op == '+' :
        result = v1+v2
    elif op == '-' :
        result = v1-v2
    elif op == '*' :
        result = v1*v2
    elif op == '/' :
        result = v1/v2

    return result

>>> f_calc(1,2,'**')
'type error : 연산불가'


# 연습문제 : 두 리스트를 전달받아 집합연산 수행
# f_set(l1, l2, '+')
# +는 합집합, -는 차집합, &는 교집합
def f_set(l1, l2, op='+') :
    result = 'type error : 연산불가'
    if op == '+' :
        result = list(set(l1) | set(l2))
    elif op == '-' :
        result = list(set(l1) - set(l2))
    elif op == '&' :
        result = list(set(l1) & set(l2))

    return result
