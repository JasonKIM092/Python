>>> l1 = [1,2,3,4,5]
>>> l2 = [[1,2,3],[4,5,6]]
>>> l3 = ['smith','allen','word']
>>> l1
[1, 2, 3, 4, 5]
>>> l2[0][0]
1
>>> for i in l1 :
	print(i)

	
1
2
3
4
5
>>> for i in l1 :
	print(i, end=' ')

	
1 2 3 4 5 
>>> for i in l1 :
	print(i, end='')

	
12345
>>> for i in l1 :
	print(i, end=',')

	
1,2,3,4,5,
>>> for i in range(0,5) :
	print(l1[i], end=',')

	
1,2,3,4,5,

# 이중(중첩) for문에서 내부 for문이 먼저 수행이 된다.
>>> for i in l2 :
	for j in i :
		print(j, end = ' ')

		
1 2 3 4 5 6 

>>> for i in l2 :
	for j in i :
		print(j, end = ' ')
	print()

	
1 2 3 
4 5 6
>>> for i in range(0,2) :
	for j in range(0,3) :
		print(l2[i][j], end = ' ')
	print()

	
1 2 3 
4 5 6

>>> list(map(lambda x : x.startswith('s'), l3))
[True, False, False]
>>> v1 = list(map(lambda x : x.startswith('s'), l3))
>>> l3[v1]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l3[v1]
TypeError: list indices must be integers or slices, not list
>>> 리스트 색인은 숫자(정수, l3[0]), 슬라이스(l3[0:2])만 가능하다.
    l3[[0,2]], l3[[True, True, False]]는 불가하다.

>>> for i in l3 :
	i.startswith('s')

	
True
False
False
>>> v2 = []
>>> for i in l3 :
	v2.append(i.startswith('s'))

	
>>> v2
[True, False, False]

>>> v3 = []
>>> for i in l3 :
	if i.startswith('s') :
		v3.append(i)

		
>>> v3
['smith']

# 구구단
for j in range(1,10) :
    for i in range(2,10) :
        print('%dX %d= %2d' % (i, j, i*j), end = ' ')
    print()




>>> print('\u2605')
★
>>> print('\u2602')
☂
>>> print('\u260E')
☎

>>> u1 = '\u2605'
>>> print(3*u1)
★★★
>>> s1 = ' '  # 공백 1칸
>>> print(s1*4+u1)
    ★
>>> print(s1*3+u1*3)
   ★★★
>>> print(s1*2+u1*5)
  ★★★★★
>>> s1 = '  '  # 공백 2칸
>>> print(s1*4+u1)
        ★
>>> print(s1*3+u1*3)
      ★★★
>>> print(s1*2+u1*5)
    ★★★★★

>>> i = 1
>>> while i < 11 :
	print(i)
	i = i + 1

	
1
2
3
4
5
6
7
8
9
10

>>> i = 1
>>> while i < 11 :
	i = i + 1
	print(i)

	
2
3
4
5
6
7
8
9
10
11

# 100까지 더한 값
>>> i = 1
>>> hap = 0
>>> while i < 101 :
	hap = hap + i
	i = i + 1

	
>>> hap
5050


# 100까지 짝수만 더한 값
>>> i = 1
>>> hap = 0
>>> while i < 101 :
	if i % 2 == 0 :
		hap = hap + i
	i = i + 1

	
>>> hap
2550


# 홀수연산에서 continue 구문 사용해서 짝수만 더한 값.
# (continue = R에서 next와 동일)
# continue를 사용하는 방법(초기값과 증가구문 위치 주의)
>>> i = 0
>>> hap = 0
>>> while i < 100 :
	i = i + 1
	if i % 2 == 1 :
		continue
	hap = hap + i

	
>>> hap
2550


# 홀수만 더한 값
>>> i = 1
>>> hap = 0
>>> while i < 101 :
	if i % 2 == 1 :
		hap = hap + i
	i = i + 1


>>> hap
2500

# 짝수연산에서 continue 구문 사용해서 홀수만 더한 값.
>>> i = 0
>>> hap = 0
>>> while i < 100 :
	i = i + 1
	if i % 2 == 0 :
		continue
	hap = hap + i

	
>>> hap
2500

# 연습문제) $를 입력하면 반복문 탈출


# 패스워드 실패 시 계속 묻는 문장
while True :
    ans = input('패스워드를 입력하세요 : ')
    if ans == '$' :
        break

print('패스워드 일치')

# 연습문제) 별 그리기
라인수  공백수  별수
1(i)     4       1
2        3       3
3        2       5
4        1       7
5        0(5-i)  9(2i-1)

6        1(i-5)  7(2(10-i)-1)
7        2       5
8        3       3
9        4       1


i = 1
s1 = '  '
s2 = '\u2605'

while i < 10 :
    if i < 6 :
        print((5-i)*s1 + (2*i - 1)*s2)
    else :
        print((i-5)*s1 + (2*(10-i)-1)*s2)
    i = i + 1
    i = i + 1



u1 = '\u2605'
s1 = '  '
i=0  # 반복횟수
j=0 
while i < 9 :   
    i=i+1   # 9 + 1 = 10 이 되므로 i < 9
    if i<6 :
        j=j+1
        print(s1*(5-j)+u1*(j*2-1))
    else :
        j=j-1
        print(s1*(5-j)+u1*(j*2-1))



list1 = []
list2 = []
value = 0
for i in range(0,4) :
    for k in range(0,5) :
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []   # [list2 [list1]] 이런 구조의 2차원 리스트이다.
                 # list1을 초기화 시키지 않으면 계속 쌓이는 구조...

for i in range(0,4) :
    for k in range(0,5) :
        print('%3d' % list2[i][k], end = ' ')
    print('')


list1 = []
list2 = []
value = 0
for i in range(0,4) :
    for k in range(0,5) :
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []

for i in range(0,4) :
    for k in range(0,5) :
        print('%3d' % list2[i][k], end = ' ')
    print('')
# 2차원 리스트라서
# list2[[list1]] 이런식으로 구성된거임.`

>>> l1 = [1,2,3,4]
>>> t1 = (1,2,3,4)
>>> type(l1)
<class 'list'>
>>> type(t1)
<class 'tuple'>
>>> l1[0] = 10
>>> l1
[10, 2, 3, 4]
>>> t1[0] = 10
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    t1[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> # 튜플은 수정이 불가능하고, 오로지 읽기만 가능한 자료구조.
>>> list(l1)
[10, 2, 3, 4]
>>> tuple(l1)
(10, 2, 3, 4)
>>> # 튜플로 바꾸는 방법 : tuple() 함수 사용
>>> # 리스트로 바꾸는 방법 : list() 함수 사용
>>> t2 = (10)
>>> 
>>> # 하나 원소를 튜플로 만들면 스칼라값이됨.
>>> # 튜플로 꼭 생성하고 싶으면
>>> t3 = (10,)
>>> # 로 하믄 됨.

>>> del(t3[0])   # 튜플 원소 삭제 불가
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    del(t3[0])
TypeError: 'tuple' object doesn't support item deletion
>>> del(t3)   # 튜플 자체 삭제 가능
>>> t3
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    t3
NameError: name 't3' is not defined

>>> v1 = 1,2,3   # 패킹
>>> a1, a2, a3 = v1   # 언패
>>> v1
(1, 2, 3)
>>> a1
1
>>> a2
2
>>> a3
3

# 딕셔너리
>>> d1 = {'a':1, 'b':2, 'c':3}
>>> d1
{'a': 1, 'b': 2, 'c': 3}
>>> d1['a']
1
>>> d1.get('a')
1
>>> d1['d'] = 4   # 키 삽입
>>> d1
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> del(d1['d'])   # 키 삭제
>>> d1
{'a': 1, 'b': 2, 'c': 3}

# 튜플 : 리스트와 같은 1차원 구조, 수정 불가
# 1. 튜플의 생성
t1 = (1,2,3)
t2 = 1,2,3
t3 = (10, )
t4 = (10)   # tuple이 아닌 스칼라로 생성

# 2. 튜플의 수정 불가(삽입, 원소 삭제)
t1.append(4)   # 불가
del(t1[0])     # 불가
del(t1)        # 튜플 자체 삭제는 가능(not defined)

# 딕셔너리 : 키와 값 형태로 저장, 출력되는 자료 구조
# 1. 딕셔너리 생성
d1 = {'a':1, 'b':2, 'c':3}

# 2. 딕셔너리 키 출력
d1['a']   # key 색인 가능
d1.get('a')   # get 매서드 사용

# 3. 딕셔너리 수정
d1['d'] = 4    # key 추가
d1['d'] = 44   # value 변경
del(d1['d'])   # key 삭제

# 연습문제) 다음의 리스트와 딕셔너리를 참고하여 전화번호를 완성 : 02)345-4958
l1 = ['345-4958', '334-0948', '394-9050', '473-3853']
l2 = ['서울', '경기', '부산', '제주']
area_no = {'서울' : "02",'경기' : "031", '부산' : "051", '제주' : "064"}

>>> f1 = lambda x, y : area_no.get(y) + ')' + x
>>> list(map(f1, l1, l2))

for i,j in zip(l1, l2) :   # zip : 동시에 여러개의 인자를 반복 전달하고 싶을 때 사용하는 함수
    area_no.get(j) + ')' + i

# keys, values
>>> area_no.keys()
 
dict_keys(['서울', '경기', '부산', '제주'])
>>> area_no.keys()[0]
 
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    area_no.keys()[0]
TypeError: 'dict_keys' object does not support indexing
>>> # 딕셔너리 keys : 색인이 불가능
 
>>> list(area_no.keys())
 
['서울', '경기', '부산', '제주']
>>> list(area_no.keys())[0]
 
'서울'
>>> area_no.values()
 
dict_values(['02', '031', '051', '064'])
>>> list(area_no.values())
 
['02', '031', '051', '064']
>>> list(area_no.values())[0]
 
'02'

>>> area_no.items()
 
dict_items([('서울', '02'), ('경기', '031'), ('부산', '051'), ('제주', '064')])
>>> area_no.items()[0]
 
Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    area_no.items()[0]
TypeError: 'dict_items' object does not support indexing
>>> list(area_no.items())[0]
 
('서울', '02')

>>> '서울' in l2
 
True
>>> 'x' in 'abcx'
 
True
>>> 'x' in ['a','x']
 
True
>>> '서울' in area_no
 
True
>>> '서울2' in area_no
 
False

# 연습문제) 위의 l1에서 각 전화번호가 0을 포함하는지 여부 출력
f2 = lambda x : '0' in x
list(map(f2, l1))

list(map(lambda x : '0' in x, l1))

tel = []
for i in l1 :
    if '0' in i :
        tel.append(i)

tel
