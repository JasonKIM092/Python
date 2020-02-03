# 함수의 인자 전달 방식
# 1. *vname : 다수의 인자를 전달
# 예제) 사용자가 입력하는 숫자를 모두 더하는 함수 생성
def f_sum(*vname) :
    hap =0
    for num in vname :
        hap = hap + num
    return hap

f_sum(1,2,3,4,5)

# 2. **vname : 다수의 인자를 딕셔너리 형태로 전달(키워드 인자)
def f_sum(v1, v2, **keywords) :
    hap =0
    for num in vname :
        hap = hap + num
    return hap

f_sum(1,2, reverse = True) :
    v1 + v2

#
import module_name.
module_name.module()

#
from module_name import *
module()

>>> import my_module
>>> my_module.f_sum(1,2,3,4,5)
15
>>> from my_module import *
>>> import math
>>> find_func(math, 'log')
['log', 'log10', 'log1p', 'log2']


# 연습문제) oracle instr과 같은 함수 생성
def instr(data, pattern, x, y) :
    z = data[x:]
    y = z.find(pattern, y)
    return print(x+y)

def instr(data, pattern, start = 0, n = 1) :
    if data.count(pattern) < n :
        position = -1
    else :
        for i in range(0,n) :
            position = data.find(pattern, start)
            start = position + 1
    return position

    



>>> c1 = open('test1.txt','r')
>>> r1 = c1.readline()
>>> print(r1)
1 2 3 4

>>> r2 = c1.readline()
>>> print(r2)
5 6 7 8

>>> c1.close()


# wd확인하는 법
import os
os.getcwd()

# wd변경법
import os
os.chdir('~~~')   # 해당 창을 닫고 새로열면 기존의 wd로 다시 리셋된다.


>>> c1 = open('test1.txt')
>>> s1 = c1.readline()
>>> s1
'1 2 3 4\n'   # print()와 만나면 실제 엔터로 파싱됨.
>>> print(s1)
1 2 3 4

>>>

>>> s1 = c1.readlines()
>>> s1
['5 6 7 8']
>>> c1.close()
>>> c1 = open('test1.txt')
>>> s1 = c1.readlines()
>>> s1
['1 2 3 4\n', '5 6 7 8']
>>> c1.close()
>>> c1 = open('test1.txt')
>>> s1 = c1.readlines()
>>> s1
['1 2 3 4\n', '5 6 7 8\n']


# 파일 입출력
1. open : cursor 선언 단계, 메모리에 외부 파일 데이터 임시 저장
2. fetch : cursor에 데이터를 하나씩 인출하는 작업
 - readline() : 한 줄씩 인출, 문자열로 저장
 - readlines() : 동시에 모든 라인 인출, 각 라인은 문자열로 리스트의 원소로 저장
3. close : cursor를 닫는 과정, 닫지 않으면 메모리 누수 현상 발생 주의

# 연습문제 : read_txt(file, sep = ' ') 함수를 생성,
# 사용자가 입력한 텍스트 파일을 분리구분 기호로 분리하여 리스트 형식으로 저장
# '\n' 처리는 strip이나 replace로 처리 가능하다.

def read_txt(fname, sep=' ') :
    outlist = []
    c1 = open(fname, 'r')
    s1 = c1.readlines()
    for inlist in s1 :
        l1 = inlist.strip().split(sep)
        outlist.append(l1)
    c1.close()
    return outlist

# 문자열 리스트 합치는 방법
>>> vstr = ''
	     
>>> for i in l1[0] :
	vstr = vstr + str(i)

# 만약 ';'으로 분리가 되어 있다면
# read_txt('test1.txt', sep = ';')로 불러온다.
