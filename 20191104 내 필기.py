# pandas 적용함수(매서드)
import pandas as pd
# 1. map 매서드
# - 1차원 구조(Series) 적용가능.
# - list, DataFrame에 적용불가.
# - cf) list에는 map 함수 적용!!!
# - 원소의 반복 적용
# 예제) 다음의 데이터 프레임에서 col1 컬럼 천단위 구분기호 제거
df1 = pd.DataFrame({'col1':['1,100','1,200','1,300'],
                    'col2':['2,200','3,300','4,400']})

f1 = lambda x : x.replace(',','')
df1['col1'].map?
df1['col1'].map(f1)

# int 변경
# sol1)
df1['col1'].map(f1).astype('int')
df1['col1'].map(f1)   # 'str' object has no attribute 'astype', 출력결과 : Series라서 astype 매서드 전달 가능.

# sol2)
f2 = lambda x : x.replace(',','').astype('int')   
f2 = lambda x : x.replace(',','')   # 출력결과 : 문자열이므로 astype 전달 불가. 문자열을 숫자로 형변환 할때는 함수를 사용해야 한다.
f2 = lambda x : int(x.replace(',',''))
df1['col1'].map(f2)

df1.map(f1)   # 적용불가 : 'DataFrame' object has no attribute 'map'
df1['col1'].map(f2)


# 2. apply 매서드
# - 2차원 구조(DataFrame) 적용가능
# - 행별 열별 그룹 연산 적용
import numpy as np
df11 = pd.DataFrame(np.loadtxt('test3.txt'))
df11.dtypes
df11.apply?

df11.apply(sum, axis = 0)   # 컬럼별 합. = apply(df11, margin=2, sum) : 컬럼별 합 in R.
df11.apply(sum, axis = 1)   # 행별 합. = apply(df11, margin=1, sum) : 행별 합 in R.

# apply(df11, margin=1, sum) : 행별 합 in R.

df1.apply(f1, axis = 1)   # 실행안됨. applymap을 통해 전달가능.


# 3. applymap 매서드
# - 2차원 구조(DataFrame) 적용가능
# - 2차원 구조 내 원소별 반복 적용(DataFrame 유지)
df1.applymap(f1)
df1.applymap(f1).dtypes
df1.applymap(f1).astype('int')

df1['col1'].applymap(f1)   # 적용불가 : 'Series' object has no attribute 'applymap'

# 연습문제) 
# 1. disease.txt 파일을 불러들여 다음을 수행
a11 = np.loadtxt('disease.txt', dtype = 'str')
df11 = pd.DataFrame(a11)

# index, column 설정
df11.index = df11.iloc[:,0]
df11 = df11.drop(0, axis = 1)

df11.columns = df11.iloc[0,:]
df11 = df11.drop('월별', axis = 0)

df11.index.name = '월'
df11.columns.name = '질병'
df11.dtypes

# NA 치환
'NA'.replace('NA',np.nan)   # replace() argument 2 must be str, not float. 문자열 치환함수임!!!
                            # replace 매서드로는 NA치환도, NA로 치환도 불가!!!
'NA'.replace('NA',0)   # replace() argument 2 must be str, not int.
'NA'.replace('NA','0')   # 0으로는 치환 불가, 문자타입인 '0'으로는 가능.

df11.replace('NA','0')   # 문자열 replace는 패턴치환 가능하나, 데이터프레임 replace에서는 불가하다. 예를들어 문자열에서 'NA'에서 N을 n으로 치환이 가능하나, 데이터프레임에선 불가.

f1 = lambda x : x.replace('NA','0')
df11 = df11.applymap(f1)

# 천단위 구분기호 제거
# 1) 천단위 구분기호가 있는 대상만 적용(하나씩)
df11.loc['3월','A형간염'] = df11.loc['3월','A형간염'].replace(',','')
df11.loc['12월','이질'] = df11.loc['12월','이질'].replace(',','')

# 2) 데이터프레임 전체 적용
f2 = lambda x : x.replace(',','')
df11 = df11.applymap(f2)

# 전체 컬럼 정수타입으로 변경
df11 = df11.astype('int')


# 1) 대장균이 가장 많이 발병한 달을 출력
df11['대장균'].sort_values(ascending=False)[0:1].index
df11['대장균'].argmax()
df11['대장균'].idxmax()
df3.idxmax?

# 2) 각 질병 별 발병횟수의 총 합을 출력
df11.apply(sum, axis=0)
df11.sum(axis = 0)

# 2. student 데이터를 불러들여
a2 = np.loadtxt('student.csv', dtype = 'str', delimiter = ',')
df22 = pd.DataFrame(a2)
df22

df22.columns = df22.iloc[0,:]
df22 = df22.drop(0, axis = 0)
df22

# 1) 지역번호 컬럼 생성
'055)381-2158'.split(')')[0]
df22['TEL'].map(lambda x : x.split(')')[0])

# 2) id에 'a'가 포함된 학생의 정보 출력
'a' in df22['ID']   # 벡터연산 불가. 단순 포함여부 확인. 패턴여부 확인 불가.
'a' in 'star123'    # 문자열끼리의 in 연산자가 패턴 포함 여부 확인 가능.

df22.loc[df22['ID'].map(lambda x :'a' in x), :]

# 9. 순위
# - Series, DataFrame 적용가능
df22.rank(method = 'average',     # 순위 결정방식(min, max, first, average)
          na_option = 'bottom',   # NA 위치 지정(keep, top, bottom)
          ascending = True,
          axis = 0)

# 예제) 다음의 시리즈에서 순위 확인
s1 = pd.Series([9,4,4,1,2,3])
s1.rank(method='first')     # 동순위를 갖는 경우 먼저 오는 데이터에 높은 순위 부여
s1.rank(method='min')       # 동순위를 갖는(4,5) 순위 중 낮은 순위(4)로 통일
s1.rank(method='max')       # 동순위를 갖는(4,5) 순위 중 높은 순위(5)로 통일
s1.rank(method='average')   # method = 'average' default. 동순위를 갖는 경우, 순위의 평균을 부여


# 10. 수학통계 메서드
df1.sum(axis = 0)
df1.idxmax(axis = 0)

df11.idxmax()
df11.idxmax(axis = 0)   # default. 질병별(세로방향) 발병횟수 최대 월(index) 출력
df11.idxmax(axis = 1)   # 월별(가로방향) 발병횟수 최대 질병이름(column) 출력

df11.rank(method = 'min', axis = 0)   # axis = 0 default. 질병별(세로방향).
df11.rank(method = 'min', axis = 1)   # 월별(가로방향).

# 11. NA관련 메서드
df3 = pd.DataFrame(np.arange(1,21).reshape(4,5))
df3.columns = ['a','b','c','d','e']
df3.iloc[1,0] = np.nan
df3.iloc[2,[1,2]] = np.nan
df3

# 1) NA 치환 - fillna
# - 동일값 치환
df3.fillna(0)

# - 서로 다른 값 동시 치환
df3['a'].fillna(0)
df3['b'].fillna(10)
df3['c'].fillna(100)

df3.fillna({'a':0, 'b':10, 'c':100})   # fillna에 딕셔너리(컬럼이름 키) 전달 시 컬럼별 치환 가능.

# - 이전,이후 값 치환
df3.fillna(method='ffill')   # 이전값으로 치환
df3.fillna(method='bfill')   # 이후값으로 치환

df3.iloc[:,0].fillna(method='ffill')

# 2) NA 삭제 - dropna
df3.loc[df3['a'].notnull(), :]

df3.dropna(axis = 0,      # 행삭제(axis = 0), 컬럼삭제(axis = 1) 여부
           thresh = n,    # NA가 아닌 데이터의 개수 지정 가능
           how = 'all')   # 모든값이 NA인 경우만 삭제

df3.dropna()           # NA가 하나라도 포함된 행 삭제
df3.dropna(axis = 1)   # NA가 하나라도 포함된 컬럼 삭제

df3.dropna(thresh=4)   # NA가 아닌 값의 갯수가 4 이상인 행만 출력하고, 4 이하인 행은 삭제 하겠다.
                       # NA가 아닌 데이터를 4회 이상 포함하는 행(axis = 0) 선택
                       # NA가 아닌 데이터가 3회 이하일 경우 제거

df3.iloc[3,:] = np.nan
df3.dropna(how='all')   # 행의 모든 값이 NA인 경우만 삭제

import os
os.getcwd()
# 연습문제) test4.csv 파일을 읽고, 
a1 = np.loadtxt('test4.csv', dtype='str', delimiter=',')
df1 = pd.DataFrame(a1)
df1.columns = df1.iloc[0,:]
df1 = df1.drop(0, axis = 0)
df1

# .을 NA로 치환
# sol1) np.where를 사용한 df의 value 수정
np.where(df1=='.', np.nan, df1)   # array로 출력되는 이유는 numpy라서...
df1[ , ] = np.where(df1=='.', np.nan, df1)   # 불가능. 색인매서드 사용해야 함...
df1.iloc[:,:] = np.where(df1=='.', np.nan, df1)   # 이렇게 해야 df1이라는 데이터프레임의 값 수정.
df1

# cf)
df1 = np.where(df1=='.', np.nan, df1)   # 이건 데이터프레임을 지우고 array를 df1이라는 객체에 덮어쓰는 것. 즉, 결과값은 array.

# sol2) 조건 색인을 활용한 치환(조건에 맞는 데이터만 선택 후 수정)
df1[df1 == '.'] = np.nan   # 이 방식도 가능함.
df1

df1.astype('float')   # NA가 포함된 상황에서는 float타입.

# 1) 1980년부터의 행 이름을 갖도록 설정
df1.shape[0]   # 행의 수
df1.shape[1]   # 컬럼 수

idx1 = np.arange(1980, 1980+34)   # np.arange(1980,1980+len(df1),1)
f1 = lambda x : str(x) + '년'

idx1.map(f1)   # array구조에서는 'map매서드 적용불가'. 그래서 Series로 바꾸거나, 'map함수를 사용'할 것!!!
# sol1) Series로 변경
Series(idx1).map(f1)   # map 매서드는 Series만 전달 가능(리스트, 배열 불가)
# sol2) map함수 적용
df1.index = list(map(f1,idx1))   # map 함수는 1차원이면 전달 가능(list, array, Series)
df1


# 2) 모든 행이 NA인 경우는 삭제하여 test3_1 생성
test3_1 = df1.dropna(how='all', axis = 0)
    
# 3) NA가 각 행마다 2개 이상인 경우 삭제하여 test3_2 생성
test3_2 = df1.dropna(thresh = 3)

# 4) NA값을 이전값으로 치환하여 test3_3 생성
test3_3 = df1.fillna(method='ffill')

# 5) test3_3데이터를 사용하여 각 년도별 판매량이 가장 높은 지점 이름 출력
test3_3 = test3_3.astype('int')
test3_3.idxmax(1)

# 6) test3_3데이터를 사용하여 각 지점별 판매량이 높은순서대로 순위 부여
test3_3.rank(method='min', ascending = False)


# 12. 기타
# - unique
# - count
# - value_counts

# 13. 멀티 인덱스