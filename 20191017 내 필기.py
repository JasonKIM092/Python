# print 함수의 서식
# print(format % value)
print(1)
print('%d' % 100)
print('%.2f' % 100)
print('%05d' % 100)
print('%s' % 100)

v1 = 100
v2 = 150

print('%d' % (v1 + v2))

# 100 + 150 = 250 형식으로 출력
print('%d + %d = %d' % (v1, v2, v1 + v2))   # 100 + 150 = 250
print('%.2f + %.2f = %.2f' % (v1, v2, v1 + v2))   # 100.00 + 150.00 = 250.00

# 연산결과 250만 출력
print('%d' % (v1 + v2))

print('%d / %d = %d' % (5, 2, 5/2))   # 5 / 2 = 2
print('%d / %d = %f' % (5, 2, 5/2))   # 5 / 2 = 2.500000
print('%d / %d = %.2f' % (5, 2, 5/2))   # 5 / 2 = 2.50
print('%d / %d = %7.2f' % (5, 2, 5/2))   # 5 / 2 =    2.50 : 2.50랑 공백까지 합쳐서 7자리 출력

print(5 + 2)
print('5 + 2 = 5 + 2')
print('%d + %d = %d' % (5, 2, 5 + 2))
print('%.2f' % (5 + 2))
# print('%d' % (5,2))   # error : value의 갯수와 format의 갯수가 일치해야 한다.
print('%d %d' % (5,2))
print('%d       %d' % (5,2))   # 공백도 칸수대로 표현
print('%d--------%d' % (5,2))   # ---기호 표현
print(900)

# print를 사용한 자리수 지정
print('%5d' % 900)   # 5자리 정수로 표현, 부족한 자리수 공백
                     # Oracle : to_char(900, '99999')
print('%05d' % 900)   # 5자리 정수로 표현, 부족한 자리수 0으로 표현
                      # Oracle : to_char(900, '09999')
print('%f' % 900)
print('%.1f' % 900)
print('%7.1f' % 900)   # 7 : 정수자리수 아님. 전체자리수!!!.
                       # '.'도 하나의 자리수로 카운트함.
print('%7.2f' % 900)
# print('%d' % 'a')   # error : 문자를 숫자로 표현불가
print('%s' % 'a')
print('%5s' % 'a')
print('%5s' % 3)   # 숫자를 문자로 출력 가능.
print('%d + %d = %d' % (3,2,3+2))
print('{0:d} + {1:d} = {2:d}' .format(3,2,3+2))   # {위치값:format값}
print('{1:d} + {2:d} = {0:d}' .format(3+2,2,3))   # {위치값:format값}. 위치값 : 3+2가 0위치, 2가 1위치, 3이 2위치. R은 시작이 1인데, 파이썬은 0이다!!!
print('aaaaa \n bbbbbb')
print('aaaaa \nbbbbbb')
print('aaaaa \t bbbbbb')
print('aaaaa\tbbbbbb')

v1 = 3
type(v1)   # 저장된 데이터의 타입확인. R : class(v1)

# 변수의 타입 확인
v1 = 3
type(v1)   # class(v1) in R

# 모듈 : R에서의 패키지처럼 여러 함수의 묶음
# import module   # 모듈의 호출, R에서의 library(package명)

# 메서드 : 함수의 첫번째 인자를 호출형식으로 전달하는 형태의 객체
a1 = '12345'
a1.count('1')   # a1에서 1의 횟수 출력.
                # 함수형태였다면 count(a1,'1')
                # 함수 : func(data, value)
                # 매서드 : data.func(value)
# . : 호출이라는 의미가 있는 특수문자. 그래서 .을 변수명이나 함수에 쓰면 안됨.
# R : read.csv -> Python : read_csv
# R : read.table -> Python : read_table

abs(-7)
round(10.26)
# trunc(10.26)   # math 모듈

import math
math.trunc(10.26)   # module.func(value)
                    # 함수명만 쓸 경우 에러.
                    # 모듈 Alias 사용 가능. as로 사용함. ex) import math as m

import math as m   # 모듈의 Alias 사용
m.trunc(10.26)

from math import trunc   # 함수 앞에 모듈이름을 안쓰고 trunc 함수를 불러올 수 있음.
trunc(10.26)

dir(math)   # dir : 모듈이 갖고 있는 모든 함수명을 출력해주는 명령어.

# Python에서 list : 1차원이면서 가장 작은 데이터의 묶음. R에서 벡터와 동일한 개념. []로 묶어주면 됨.

from math import *   # math 모듈에 있는 모든 함수를 모듈이름을 생략하고 불러올때.
log(10)
cos(1)

a1 = 'aaaaaaaaa'
a1 = '''aaaaaaa
bbbbbbbbb
ccccccccc'''      # 문자열 값을 입력할때 엔터를 입력하고 싶다면 '이나 "를 세번 반복 해서 입력한다.('''/""")

# 문자열 결합
'a' + 'b' + 'c'   # abc, 'a'||'b'||'c' in Oracle. paste('a','b','c', sep='') in R.
ename = 'smith'
dname = 'sales'
ename + dname
ename + '의 부서는 ' + dname   # 문자열을 결합할 때 + 쓰면 됨.

ename + ' ' + dname
ename + ' - ' + dname

# 문자열에다 색인기호를 써서 문자열 일부를 추출 가능하다.
# R에서는 색인이 아니라 substr으로 써야했다.
s1 = 'abcdef'
s1[2]   # c
s1[1]   # b
s1[0]   # a
s1[1:2]   # b. 1:2를 쓰면 파이썬에서는 2이전의 숫자까지를 뜻한다. 결국 1:1로 해석이 된다.
s1[1:3]   # bc

# 파이썬에서는 문자열 슬라이싱 가능(R에서 불가. substr사용)
v1 = 'abcdef'
v1[1]   # 두번째 원소 출력(b). substr(v1,2,2) in R.
v1[1:3]   # 두, 세번째 원소 출력(bc). substr(v1,2,3) in R.

# 파이썬에서의 위치 및 슬라이스 색인
# 012345   # 위치
# abcdef   # 문자열

# 0:3   # 0~2까지 출력. 첫번째부터 세번째까지
# 1:4   # 1~3까지 출력, 두번째, 세번째, 네번째 출력.


# 문자열 포함
'a' in 'abc'   # True

# 문자열 매서드
s1 = 'abcade'
s2 = ' abc '
s3 = 'a;b;c'

s1.startswith('a')     # s1이 a로 시작하는지 여부
s1.startswith('a',4)   # 해당위치(4)가 a로 시작하는지 여부. False
s1.startswith('a',1)   # False
s1.startswith('a',3)   # True
s1.endswith('a')       # s1이 a로 끝나는지 여부
s1.find('b')           # s1에서의 b의 위치 리턴
s1.find('a')           # 두번째 a의 위치값을 찾는것은 불가능. 오라클에서는 instr함수로 두번째 a의 위치값 추출이 가능했음.
s1.find('a',2)         # 두번째 a의 위치값 출력. 위치값은 항상 처음(0)기준.
s1.find('a',4)         # -1리턴. -1은 없다는 뜻이다. 즉, 4번째 위치인 d 이후로는 a가 없단 뜻.
'f' in s1              # 특정 문자열이 s1에 있는지 여부.
s1.find('f')  == -1    # 특정 패턴이 포함이 되었는지 여부 확인 가능 명령어. s1에 f가 포함이 되어있지 않는 것(-1)이 맞느냐?란 뜻. 결과값 True
s1.find('f')  != -1    # s1에 f가 있느냐?
s2.strip()             # s2에서 양쪽 공백 삭제
s2.lstrip()            # s2에서 왼쪽 공백 삭제
s1.lstrip('a')         # s1에서 a를 왼쪽에서 지워라. 'bcade'. 오라클에서도 파이썬에서도 중간에 포함된 a는 제거 못한다.
s1.replace('a','')     # 'bcde' 중간에 있는 a, 처음있는 a도 다 제거.
s2.rstrip()            # s2에서 오른쪽 공백 삭제
s1.replace('a','A')    # s1에서 a를 A로 치환
s3.split(';')          # s3을 ;로 분리
s3.split(';')[1]       # b. 위치색인으로 원소값 추
s1.count('a')          # s1에 a가 포함된 횟수
s1.upper()             # 대문자 치환
s1.lower()             # 소문자 치환
s1.title()             # 맨 앞 글자 대문자로 치환. Oracle에서 initcap.
'abc cba'.title()      # 'Abc Cba'

>>> input()
abc
'abc'
>>> v1 = input('삭제할까요? Y|N' : ')
	       
SyntaxError: invalid syntax
>>> v1 = input('삭제할까요? Y|N : ')
	       
삭제할까요? Y|N : y
>>> v1 = input('삭제할까요? Y|N : ')
	       
삭제할까요? Y|N : n
>>> 


jumin = '9112311234567'
jumin[6] == '1'   # 주민번호 성별값이 1이 맞는가?
jumin.startswith('1',6)  # 위와 같은 명령어.
jumin.startswith('1',6,10)   # 마지막 문자의 위치값은 해당 위치값이 끝이면 생략 가능.

# 데이터타입
jumin[6] == 1   # cf) 데이터 타입 꼭 지켜줄것. 해당 명령어는 False로 나옴.
                # 문자열이므로 문자로 입력해줄것.

jumin = 9112311234567
type(jumin)
jumin[6] == 1   # error.
jumin[6]   # error. 문자열 슬라이스 :  문자에만 사용 가능. 숫자에는 사용 불가.
jumin.startswith(1,6)  # error. 문자열 매서드 : 문자에만 사용 가능. 숫자에는 사용 불가.
                       # AttributeError: 'int' object has no attribute 'startswith'.(attribute : 매서드). 매서드 startswith에는 숫자 오브젝트사용이 불가하다.
jumin.startswith(1,6,10)   # error. 문자열 매서드 : 문자에만 사용 가능. 숫자에는 사용 불가.

# 연습문제
ename = 'smith'
tel = '02)345-7839'
jumin = '901223-2223928'
vid = 'abc1234!'

# 1) ename의 두번째 글자가 m으로 시작하는지 여부
>>> ename.startswith('m',1)
>>> ename[1] == 'm'
     
# 2) tel에서 국번(345) 출력
>>> tel[3:6]
     
>>> v1 = tel.find(')')
>>> v2 = tel.find('-')
>>> tel[(v1+1):v2]
     
# 3) jumin에서 여자인지 여부 출력
>>> jumin[7] == '2'
>>> jumin.startswith('2',7)
     
# 4) id에서 '!'가 포함되어 있는지 여부 출력
>>> vid.find('!') != -1
>>> '!' in vid
     
# 5) vid 왼쪽에서 'a' 삭제
>>> vid.lstrip('a')


v1 = 'a!b!cde!'
v1.find('!')     # 처음발견된 !의 위치를 알려줌.
v1.find('!',2)   # b이후 발견되는 !의 위치 알려줌. 위치값은 0부터 시작(a부터 시작해서 카운트)
               
# 계산기 프로그램
print('계산기 프로그램')

v1 = int(input('첫 번째 수를 입력하세요 : '))
v2 = int(input('두 번째 수를 입력하세요 : '))

print(v1 + v2)

# input으로 물어본 값은 문자로 불러오게 됨.
# int('10') + int('56') = 66

# 형 변환함수
# int : 정수 변환 함수
# float : 소수 변환 함수
# str : 문자열 변경 함수



# 연습문제
# 두 수를 입력받아 첫 번째 수를 두번째 수로 나눈 몫과 나머지를 아래처럼 출력
# 10 / 3의 몫 : 3, 나머지  : 1
print('계산기 프로그램')

v1 = int(input('첫 번째 수를 입력하세요 : '))
v2 = int(input('두 번째 수를 입력하세요 : '))

v3 = v1 // v2
v4 = v1 % v2

print('%d / %d 의 몫 : %d, 나머지 : %d' % (v1,v2,v3,v4))



# 실습문제
# 1. 문자열, 찾을 문자열, 바꿀 문자열을 입력 받아 변경한 결과를 아래와 같이 출력
# 변경전 :
# 변경후 :

v1 = input('문자열을 입력하시오. : ')
v2 = input('찾을 문자열을 입력하시오. : ')
v3 = input('바꿀 문자열을 입력하시오. : ')
v4 = v1.replace(v2,v3)

print('''변경전 : %s
변경후 : %s''' % (v1,v4))


# 2. 이메일 주소를 입력받고 다음과 같이 출력
# 아이디 : a1234
# 메일엔진 : naver

v1 = input('이메일 주소를 입력하세요 : ')

v2 = v1.find('@')
v3 = v1.find('.')

v4 = v1[0:v2]
v5 = v1[(v2+1):v3]

print('아이디 : %s, 메일엔진 : %s' % (v4,v5))
               

# 3. 2번을 활용하여 다음과 같은 홈페이지 주소 출력
# http://kic.com/a1234
               
v1 = input('이메일 주소를 입력하세요 : ')

v2 = v1.find('@')
v3 = v1.find('.')

v4 = v1[0:v2]
v5 = v1[(v2+1):v3]

print('http://kic.com/%s' % (v4))


# 4. num1='12,000' 의 값을 생성 후, 33으로 나눈 값을 소숫점 둘째짜리까지 표현

num1 = '12,000'
num1 = int(num1.replace(',',''))
v1 = 33
print('%d / %d = %.2f' % (num1,v1,num1/v1))










