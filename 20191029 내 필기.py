# 수학 통계 매서드
import numpy as np
arr1 = np.arange(1,13).reshape(4,3)
arr2 = np.random.randn(2,4,3)
arr1
arr2
arr2.min(0)   # 층별 비교 : 행과 열은 고정, 서로 다른 층끼리 비교.
arr2.min(1)   # 행별 비교 : 층과 열은 고정, 서로 다른 행끼리 비교.

arr1.sum()
arr1.mean()
arr1.var()

np.array([2,4,6]).var()           # var = 편차 제곱 합 / n in numpy. default ddof = 0 in numpy.
np.array([2,4,6]).var(ddof=1)     # var = 편차 제곱 합 / (n - 1) in pandas. default ddof = 1 in pandas.
np.array([2,4,6]).var(ddof=k)     # var = 편차 제곱 합 / (n - k)

arr1.std()
arr1.min()
arr1.max()

arr0 = np.arange(1,11)
arr0[arr0.argmin()]   # 1차원에는 색인이 의미가 있다.

arr1.argmin(0)   # 최소값을 갖는 대상의 위치값 출력 매서드 in Python numpy. which.min in R. idxmin in Python pandas.
                 # arr1은 2차원이라 해당 매서드를 통한 색인의 의미가 없다.
arr1.argmax(0)   # 최대값을 갖는 대상의 위치값 출력 매서드 in Python numpy. which.max in R. idxmax in Python pandas.

arr1.cumsum()    # 누적합. 0 : [1,4,7,10], [2,5,8,11], [3,6,9,12]의 누적합. 서로 다른 행끼리의 누적합.
arr1.cumprod()   # 누적곱. 0 : [1,4,7,10], [2,5,8,11], [3,6,9,12]의 누적곱. 서로 다른 행끼리의 누적곱.

# 논리 연산 함수
arr0 = np.arange(1,11)
arr0 > 5
(arr0 > 5).sum()     # True의 개수 출력.
(arr0 > 5).count()   # numpy에는 count 함수가 없다.
(arr0 > 5).any()     # 하나만 True여도 True 리턴, 조건 충족 요소 존재 확인.
(arr0 > 5).all()     # 전체가 True여야 True 리턴, 모둔 요소 조건 충족 여부 확인.
np.bincount([True, True, True, False])   # 항목별 카운트(count), table in R.

# 정렬
a1 = np.array([5,2,6,3,9])
a2 = np.array([[3,1,5],[2,4,1],[4,0,8]])
a1.sort()    # 원본 객체 즉시 정렬 수정
a1
a2.sort(0)   # 서로 다른 행 내에서 정렬 수행
a2.sort(1)   # 서로 다른 열 내에서 정렬 수행
a2

# [ 참고 : 매뉴얼 확인 방법 ]
a2.sort?    # help(sort) in R. help 출력.
a2.sort??   # 함수 코드 출력

import my_module as mu
mu.read_txt?
mu.read_txt??

# numpy 집합 연산자
a1 = np.array([1,2,3,4,5])
a2 = np.array([3,4,5,6,7])

np.union1d(a1,a2)       # 합집합
np.intersect1d(a1,a2)   # 교집합
np.setdiff1d(a1,a2)     # 차집합

# [ 참고 : 리스트(세트)의 집합 연산자(union, intersection, difference) ]
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

set(l1).union(set(l2))
set(l1).intersection(set(l2))
set(l1).difference(set(l2))

# unique 연산자
np.unique([1,2,2,2,3,3])
set([1,2,2,2,3,3])

# numpy(array)의 in 연산자
l1 = [1,2,3,4]

l1 in [1,2]                # 리스트끼리 in 연산자는 포함 연산자, or 연산자 축약 전달 불가.
[i in [1,2] for i in l1]   # 스칼라 in 연산자는 or 연산자 축약형.

np.in1d(np.array(l1),[1,2])                 # numpy의 in1d 연산자는 or 연산자 축약형.
np.array(l1)[np.in1d(np.array(l1),[1,2])]   # 색인을 이용하여 값 출력.
np.in1d(l1,[1,2])                           # in1d 연산자에 리스트 전달 가능.
l1[np.in1d(l1,[1,2])]                       # 리스트에 직접 색인 전달 불가.
np.array(l1)[np.in1d(l1,[1,2])]             # array로 변경해주고 색인 가능.

# numpy 파일 입출력
np.loadtxt('test1.txt',         # 파일명
           delimiter = ':',     # 분리 구분 기호
           dtype = 'str',       # 데이터 타입(float이 디폴트)
           skiprows = 1,        # 데이터 로딩시 제외할 행 설정, 정수만 설정 가능
                                # skiprows가 정수인 경우는 위에서부터 제외
                                # 4라고 기록하면 위에서부터 4개가 생략된 채 출력됨.
                                # 리스트 형태로 전달 불가. ex) skiprows = [0,3]. 이렇게 전달 불가.
           encoding = 'cp949'   # 데이터 로딩 인코딩 옵션
           )

np.loadtxt   # 주석제외하고 파일 불러옴.
np.loadtxt('test1.txt', delimiter = ':', dtype = 'str', skiprows = 1, encoding = 'utf8')

arr1 = np.arange(1,10).reshape(3,3)
np.savetxt('arr1.txt', arr1, fmt = '%s', delimiter=',')

#예제) 파일이 다음과 같이 저장되어 있는 경우 data만 불러오기
#name:deptno:sal
#smith:10:1,500
#allen:20:2,800
#name1:deptno1:sal1
#ford:30:1,900
#word:10:3,100
#scott:20:3,300

np.loadtxt('test1.txt', delimiter=':', dtype='str', encoding = 'utf8',
           skiprows = [0,3])  # np.loadtxt의 skiprows는 리스트 전달 불가
np.loadtxt('test1.txt', delimiter = ':', dtype = 'str', skiprows = [0,3], encoding = 'utf8')    # skiprows = [0,3]. 이런식으로 리스트 전달 불가.

# pandas
import pandas as pd
pd.read_csv('test1.txt', sep=':', dtype='str', encoding = 'utf8', 
            skiprows = [0,3],   # pd.read_csv의 skiprows는 리스트 전달 가능
            header=None)        # 컬럼 지정 안 할 경우. header = None. header = False 아님.
pd.read_csv('test1.txt', sep = ':', dtype = 'str', skiprows = [0,3], encoding = 'utf8', header = 0)

# [연습문제]
# 1. 1부터 증가하는 3 X 4 X 5 배열 생성 후
arr1 = np.arange(1,61).reshape(3,4,5)
arr1.shape
arr1.ndim
arr1.dtype

# 1) 모든 값에 짝수는 *2를 홀수는 * 3을 연산하여 출력
arr2 = np.where(arr1%2==0, arr1*2, arr1*3)

# 2) 각 층의 첫번째 세번째 행의 두번째 네번째 컬럼 선택하여 NA로 치환
arr2[np.ix_([0,1,2],[0,2],[1,3])] = np.nan   # 수정불가. np.nan이 float으로 인지됨.

arr2 = arr2.astype('float')
arr2[np.ix_([0,1,2],[0,2],[1,3])] = np.nan   # 수정가능.
arr2

# [ 참고 ]
arr2[:,[0,2], :][:,:,[1,3]] = 0   # 연속적 색인의 경우 출력만 가능. 수정불가.
                                  # 수정안됨. 연속적 색인은 출력만 가능하고 수정은 불가.

# 3) 위의 수정된 배열에서 NA의 개수 확인
np.isnan(arr2).sum()

# [ 참고 : na 치환 ] nan을 0으로 수정하는 방식.
arr2[np.isnan(arr2)]   # 색인
arr2[np.isnan(arr2)] = 0

# 4) 층별 누적합 확인
arr2.cumsum(0)


# 2. emp.csv 파일을 array 형식으로 불러온 뒤 다음 수행(컬럼명은 제외)
import os
os.getcwd()             # 작업 디렉토리 확인.
os.chdir('C:\\Users')   # 작업 디렉토리 일시적 변경.

emp = np.loadtxt('emp.csv', delimiter = ',', dtype = 'str', skiprows = 1)
emp.shape[0]   # 행의 수 확인.
emp.shape[1]   # 컬럼 수 확인.

emp = pd.read_csv('emp.csv', dtype = 'str')
emp = np.array(emp)

# 1) 이름이 smith와 allen의 이름, 부서번호, 연봉 출력
emp[(emp[:,1] == 'SMITH')|(emp[:,1] == 'ALLEN'),:][:,[1,5,7]]

emp[np.ix_(np.in1d(emp[:,1], ['SMITH','ALLEN']), [1,-1,-3])]
emp[np.in1d(emp[:,1], ['SMITH','ALLEN']),:][:,[1,-1,-3]]

# 2) deptno가 30번 직원의 comm의 총 합 
emp[:,-2] = np.where(emp[:,-2]=='','0',emp[:,-1])

emp[(emp[:,7]=='30'),6].astype('int').sum()
emp[(emp[:,-1]=='30'),-2].astype('int').sum()

# 3) 각 직원의 출생년도 출력
[x[:4] for x in emp[:,4]]
list(map(lambda x : x[:4], emp[:,4]))
list(map(lambda x : x.split('-')[0], emp[:,4]))

l2 = []
for i in emp[:,4] :
    l2.append(i[:4])
    
l2




import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import nan as NA

# 프로파일 생성 및 실행
# 파이썬 실행 시 호출해야 할 모듈을 미리 한 파일에 만들어 놓는 경우
# 해당 파일을 'run 프로파일명'으로 실행시키면 작업공간에서 
# 미리 만들어 놓은 프로파일로 모듈 호출 가능

#run pro          # 작업공간(디폴트 디렉토리)에 있는 profile.py 파일 실행
np.array([1,2,NA])   
Series([1,2,3,4])

# Series
# - pandas에서 제공하는 1차원 자료 구조
# - 하나의 데이터 타입만 허용
# - index와 value로 구성
# - DataFrame 객체의 각 컬럼이 갖는 자료 구조

# 1. Series 생성
s1 = Series([1,2,3,4])
s2 = Series(['a','b','c','d'])
s3 = Series([1,2,3,4,'5'])   # 묵시적 형변환 x. 자료타입이 두가지라 숫자가 문자로 바뀐것이다.

s1.dtypes            # Series를 구성하는 데이터 타입 확인. object == str.
s1.index             # Series를 구성하는 index 출력
s1.values            # Series를 구성하는 값을 array 형태로 출력
s1.astype('float')   # Series 데이터 타입 변경

# index 부여
s4 = Series([1,2,3,4], index=[1,2,3,4])   # index가 없는 객체에 index 전달 시 새 index 부여
Series(s4, index=['a','b','c','d'])       # NaN리턴 이유 : 인덱스가 없는 자료구조(객체)에 인덱스를 만들어주면 인덱스 부여가 맞다.
                                          # 하지만 인덱스가 있는 자료 구조에 인덱스를 다시 설정하면 
                                          # 인덱스의 변경의 아니라 앞에 있는 인덱스를 뒤에 있는 인덱스에 순서대로 재배치 하라는 것이다.
                                          # index가 있는 객체 index 전달시 reindex(재배치)

# 예제) 금요일에 4, 화요일에 3, 수요일에 1, 월요일에 10, 목요일에 9, 일요일에 5,
# 토요일에 1의 값을 갖는 Series를 생성, 생성 후 월~일 순서대로 재배치 한 새로운 시리즈 생성
s1 = Series([4,3,1,10,9,5,1], index = ['금','화','수','월','목','일','토'])   # 인덱스 부여
s2 = Series(s1, index = ['월','화','수','목','금','토','일'])   # 인덱스 재배치

# 이미 index를 갖는 Series의 index 변경
s1.index = ['a','b','c','e','f','g','h']
s1

# 2. Series 연산
s_1 = Series([1,2,3,4], index = ['b','a','d','c'])
s_2 = Series([10,20,30,40,], index = ['a','b','c','d'])

s_1 + s_2   # key값이 같은 원소끼리 계산함. 위치값 아님.


# 3. Series 색인
s1['e']       # key indexing
s1[3]         # positional indexing
s1[0:3]       # slice indexing
s1[[0,2,3]]   # list indexing
s1[s1 > 5]    # boolean indexing
