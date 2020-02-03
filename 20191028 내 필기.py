import numpy as np

# 리스트와 배열의 불리언색인

l0 = [1,2,3,4]
l1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

l0 > 3                            # 리스트에 조건 전달 불가.
l0[l0 > 3]                        # 조건 결과 색인값에 전달 불가.
l0[[False, False, False, True]]   # 불리은 리스트 색인값에 전달 불가.

arr1 = np.array(l1)       # 배열에 조건 전달 가능.
arr1[arr1[:,1] == 6, :]   # 조건 결과(불리언 리스트)를 색인 값에 전달 가능.

# asarray 함수로 배열 생성
l1 = [1,2,3,4]
a1 = np.array(l1)
a2 = np.asarray(a1)

# 같은 자료구조끼리 복사는 얕은 복사가 디폴트 옵션으로 수행이 됨.
# 다른 자료구조로 복사할 경우, deep copy가 수행됨.
# 기존 array구조에서 asarray를 통해 복사를 할 경우, 얕은 복사가 디폴트로 수행이 된다.

a1[0] = 10
a1   # 10으로 변경 됨.
l1   # 자료구조가 바뀌는 경우는 항상 deep copy가 수행. 10으로 변경 x.
a2   # asarray로 이미 생성된 배열을 또 다른 배열로 복사하는 경우 얕은복사 수행, 10으로 변경 됨.

# 배열의 데이터 타입 변경
a1 = np.array([1,2,3,4])
a1

# sol1) array함수에서 dtype옵션 사용
a2 = np.array(a1, dtype='float')
a2.dtype

# sol2) astype함수
a3 = a1. astype('float')
a3.dtype

# 배열 슬라이스 색인의 얕은 복사
arr1 = np.array(1,16).reshape(3,5)
arr2 = arr1[:,0:3]
arr3 = arr1[:,0:3].copy()

arr2[0,0] = 10
arr2   # 10으로 변경 됨.
arr1   # 얕은 복사가 수행되어, arr1도 10으로 변경 됨.
arr3

l1 = l0[:]   # 리스트에서 deep copy.
l1 = [1,2,3,4,5]
l2 = l1[:]
l3 = l1
l1[0] = 10
l2
l3

a1 = np.random.randn(7,4)
a2 = np.array(['a','b','c','d','e','f','g'])
a2 == 'b'
a1[a2 == 'b', : ]
a1[a2 == 'b']

# 2차원 : [행,열] [행, :] [행]. 행 우선순위.
# 3차원 : [층,행,열] [층,:,:] [층]. 층 우선순위.
a1[0]   # 2차원에서는 '행', 3차원에서는 '층'.

a2 != 'b'          # 같지 않다.
!(a2 == 'b')       # 에러.
~(a2 == 'b')       # 조건의 부정
a1[a2 != 'b']
a1[~(a2 == 'b')]   # 두번째 행을 제외한 나머지 행 모두 출력.

arr = np.random.randn(6,3)
np.dot(arr.T, arr)

# 축의 전치
# 1. T 매서드 : 행과 열 전치 리턴, 얕은 복사 수행
a1 = np.arange(1,10).reshape(3,3)
a2 = np.arange(1,19).reshape(2,3,3)
a1
a1.T
a2

# 2. swapaxes(축번호1, 축번호2) : 전달받은 두 축을 전치, 인자의 수는 항상 두 개, 인자 순서 의미 없음.
a1.swapaxes(0,1)   # 2차원
a1.swapaxes(1,0)   # 2차원
a2.swapaxes(1,2)   # 3차원
a2.swapaxes(2,1)   # 3차원
a2.swapaxes(0,1)   # 3차원
a2.swapaxes(1,0)   # 3차원

# 3. transpose(...) : 전달받은 축 번호 대로 전치 후 리턴, 인자의 개수는 차원에 맞게 전달, 인자 순서 중요(층, 행, 열).
# 2차원 : transpose(행,열)
# 3차원 : transpose(층,행,열)
a1.transpose(0,1)     # 2차원일때 원본출력
a1.transpose(1,0)     # 2차원일때 행,열 전치
a2.transpose(0,2,1)   # 3차원일때 행,열 전치

# Python에서의 축번호
# 2차원
행 0, 열 1 in Python
행 1, 열 2 in R

# 3차원
층 0, 행 1, 열 2 in Python
행 1, 열 2, 층 3 in R

## 참고 : 스파이더 주석 처리 : ctrl + 1

# 연습문제
# read_txt 함수를 사용하여 아래 파일을 불러온 후 다음 수행
# smith:10:1,500
# allen:20:2,800
# ford:30:1,900
# word:10:3,100
# scott:20:3,300

import my_module as mm
t1 = mm.read_txt('test1.txt', sep = ':', fmt = str)
t1

# 1) 이름이 s로 시작하는 직원의 이름과 연봉 출력
t1 = np.array(t1)
t1[list(map(lambda x : x.startswith('s'), t1[:,0])), :][:, [0,2]]

b1 = list(map(lambda x : x.startswith('s'), t1[:,0]))
t1[b1,:][:,[0,2]]

t1[np.ix_(b1,[0,2])]

# 2) 10번 부서 직원들의 이름 출력
t1[t1[:,1] == '10',0]

# 3) 각 직원의 10% 인상된 급여를 이름과 함께 출력
t1[:,2]
t1[:,2] = list(map(lambda x : round(int(x.replace(',',''))*1.1), t1[:,2]))
t1[:,[0,2]]
t1[np.ix_(:,[0,2])]   # np.ix_에서는 콜론(:) 못씀
t1[np.ix_([0,1,2,3,4],[0,2])]

# 배열 함수
from numpy import nan
a1 = np.array([1,2,3,nan])

from numpy import nan as NA
a1 = np.array([1,2,3,NA])

import numpy as np
a1 = np.array([1,2,3,np.nan])
np.isnan(a1)

a1 + a2   # NA 포함 산술 연산 결과는 NA
np.add(a1,a2)
np.maximum(a1, a2)

# np.where 함수
# - Oracle의 decode, R의 ifelse 구문과 비슷
# - np.where(조건, 참 리턴, 거짓 리턴)
# - 벡터 연산 가능

# 예제) 위의 a1에서 NA는 0으로 치환
np.where(np.isnan(a1),0,a1)

# 연습문제) 다음의 배열에서 1000이하는 'C', 1000초과 2000이하는 'B',
# 2000초과는 'A'리턴
a1 = np.array([1100,900,1400,550,3000])
a2 = [1100,900,1400,550,3000]
np.where(a1 <= 1000, 'C', np.where(a1 <= 2000, 'B', 'A'))

['C' if i <= 1000 else 'B' if i <= 2000 else 'A' for i in a1]

result = []
for i in a1:
    if 1000 >= i:
        result.append('C')
    elif 2000 >= i:
        result.append('B')
    else:
        result.append('A')
        
result
# 실행할 때 드래그 해서 할것!!!
        
        
result      
len(a1)

# 산술연산 매서드
a1 = np.arange(5)
a1.sum()
a1.mean()
a1.max()
a1.min()
a1.var()

a2 = np.arange(1,10).reshape(3,3)
a2.sum(axis=0)   # = apply(a2, 2, sum) in R. 파이썬에서 행별 계산은 서로 다른 행끼리의 연산이다. 
                 # cf) R에서는 서로 같은 행끼리의 연산. apply(a2, 1, sum) in R.
                 # 행별(서로 다른 행끼리) in Python. => apply(a2, 2, sum) in R.
a2.sum(axis=1)   # = apply(a2, 1, sum) in R
                 # 컬럼별(서로 다른 컬럼끼리) in Python. => apply(a2, 1, sum) in R.

# 분산 = 편차 제곱의 합 / n       # numpy에서의 var 계산식
# 분산 = 편차 제곱의 합 / (n-1)   # pandas에서의 var 계산식

# [연습문제] 다음의 배열에서 행별, 열별 분산을 구하여라 in Python
# 단, 분산을 구할 때 var 매서드 사용 대신 분산을 구하는 수식으로 계산
                 
a2 = np.arange(1,10).reshape(3,3)
a2

# 1) 행별 분산
a2.mean(axis=0)   # 행별. [4,5,6]
a2 - a2.mean(0)   # 편차
(a2 - a2.mean(0))**2   # 편차 제곱 합
((a2 - a2.mean(0))**2).sum(0)   
((a2 - a2.mean(0))**2).sum(0) / 3   # 분산 연산

((1-4)**2 + (4-4)**2 + (7-4)**2) / 3
((2-5)**2 + (5-5)**2 + (8-5)**2) / 3
((3-6)**2 + (6-6)**2 + (9-6)**2) / 3
a2.var(axis = 0)

# 2) 열별 분산
a2.mean(axis=1)   # 열별. [2,5,8]
a2 - a2.mean(1).reshape(3,1)   # reshape : 컬럼별 반복을 수행하려면 데이터구조를 맞춰줘야 한다.
(a2 - a2.mean(1).reshape(3,1))**2
((a2 - a2.mean(1).reshape(3,1))**2).sum(1)
((a2 - a2.mean(1).reshape(3,1))**2).sum(1) / 3

((2-1)**2 + (2-2)**2 + (3-2)**2) / 3
((4-5)**2 + (5-5)**2 + (6-5)**2) / 3
((7-8)**2 + (8-8)**2 + (9-8)**2) / 3
a2.var(axis = 1)
