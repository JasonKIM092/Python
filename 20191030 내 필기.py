# Series 생성
import pandas as pd
s1 = pd.Series([1,2,3,4])
s2 = pd.Series([1,2,3,4], index = ['a','b','c','d'])   #인덱스 부여
s3 = pd.Series(s2, index = ['A','B','C','D'])   # 인덱스 재배치
s3
pd.Series(s2, index = ['b','d','a','c'])   # 인덱스 재배치
# 1. index 생성 : 앞에 있는 객체가 인덱스를 갖고 있지 않을 때
# 2. index 재배치(reindex) : 시리즈 안에 있는 객체가 이미 인덱스를 갖고 있을 때

# Series 연산
s1 + 1
s1 + s2   # 키값이 같은 애들끼리 연산이 된다. 해당 연산은 같은 키를 갖는 원소가 없어서 모두 출력하고 NA가 출력이 된다.

# Series 매서드
s1.index
s2.values
s1.dtype   # = s1.dtypes
s1.dtypes
s1.name = 'series1'
s2.index.name = 'ename'
s2.index

# Series 수정
s1[0] = 10
s1.index[1] = 'a'   # index object는 수정 불가.

# 예제) s1의 두번째 인덱스만 'a'로 수정.
s1.index.values[1] = 10   # 수정이 되기는 하나 s1 인덱스에는 반영 x.
s1 = pd.Series([1,2,3,4])
s1.index.values[1] = 10
s1

a11 = s1.index.values
a11[1] = 10
s1.index = a11   # index를 수정할 때는 이렇게 덮어쓰는 형태로 해야함.
                 # index를 직접 설정하지 않은 Range Index의 경우는 수정을 직접적으로 못하고,
                 # 덮어쓰는 형태로 해야한다.

s2.index
s2.index[1] = 'B'          # 불가, error 발생.
s2.index.values[1] = 'B'   # 수정됨
s2.index.values            # 수정된 것 확인
s2                         # s2 객체 index 수정된 것 확인
                           # index를 직접 설정한 경우는 바로 수정이 가능하다.

s3 = pd.Series([1,2,3,4], index=[1,2,3,4])
s3.index.values[1] = 10
s3


# NA 확인 함수
import numpy as np
a1 = np.array([1,2,np.nan,3])
np.isnan(a1)   # numpy NA 확인 함수

s1 = pd.Series(a1)
s1.isnull()      # pandas NA 확인 매서드
s1.isnotnull()   # notnull 매서드
pd.isnull(s1)    # pandas NA 확인 함수
pd.notnull(s1)   # pandas not null 확인 함수

l1 = pd.Series([4,7,-5,3])
l1.index = ['Bob','Steve','Jeff','Ryan']   # 일부구간이 아니라 전체는 덮어쓰는거라서 
                                           # Range Index라도 이런방식으로는 수정이 가능함.(전체수정)


# DataFrame
# - 2차원 구조
# - 엑셀 데이터 시트, 오라클 테이블 구조
# - Key를 갖는 구조(column이 주 키, index는 서브 키 개념)

# 1. DataFrame 생성
d1 = {'col':[1,2,3,4], 'col2':['a','b','c','d']}   # 딕셔너리 생성 :  Python에서는 모든 원소를 묶을 때 리스트를 사용. R에서는 벡터 사용!!
df1 = pd.DataFrame(d1)

# 2. DataFrame 매서드
df1.index     # index 확인
df1.columns   # column 확인
df1.values    # value값 array로 출력
df1.dtypes    # 각 컬럼의 데이터 타입 확인(desc in Oracle, str in R)
type(df1.columns)

# 3. DataFrame 수정
df1.index = ['a','b','c','d']
df1.index.name = 'index_name'
df1.columns = ['COL1','COL2']
df1.columns.name = 'column_name'
df1.name = 'data frame'
df1

# 4. DataFrame 색인
df1['COL1']   # 주 key가 column이므로 컬럼 우선순위
df1.COL1      # key 호출 형식으로 컬럼 선택 가능(df1$COL1 in R)
df1[1:3]      # slice 색인의 경우 row 우선순위를 가짐

df1['a','COL1']   # 불가
df1[0,0]          # 불가

df1.ix['a','COL1']   # Python DataFrame 행, 컬럼 색인은 ix 매서드를 통해 가능
df1.ix[0,0]
df1.ix[0,'COL1'] 
df1.ix[:,'COL1']
df1.ix['a',:]
df1.ix[['a','d'],'COL1']            # 리스트 색인 가능.
df1.ix[['a','d'],['COL1','COL2']]   # 리스트, 리스트 색인 가능
df1.ix[0:2, 0]                      # 슬라이스 색인 가능, Series 출력(1차원). 차원축소(2차원 -> 1차원) 출력.
d1 = df1.ix[0:2, 0]
type(d1)   # Series
df1.ix[0:2, 0:1]   # 슬라이스 색인 가능, 차원축소 방지(0:1)
df1.ix['a':'c', :]   # 문자열 연속적 시퀀스 전달 가능.
                     # cf)R에서는 불가했다. R에서는 dplyr패키지에서 select로 가능했다.
                     # 주의. 문자열의 연속적 색인에서 end범위를 포함한다.
                     # ex) 'a':'c'까지로 범위를 주면, 'c'를 포함해서 출력.
                     # 숫자에서는 0:3까지하면 0,1,2까지만 출력했다.

df1.iloc[0,0]         # positional indexing(위치값으로만 색인 시)
df1.iloc[0,'COL1']    # error. iloc에는 문자 전달 불가.

df1.loc['a','COL1']   # label based indexing(이름값만으로만 색인 시)
df1.loc[0,'COL1']     # error. loc에는 숫자 전달 불가.

df1.ix[-1,:]   # 제외 x. 맨 끝 행 출력.
df1.ix[1:,:]   # 첫번째 행 제외하고 출력.

df1.drop('c', axis = 0)         # 행 또는 컬럼 삭제 매서드, axis = 0이 default로 행 삭제, 1이면 컬럼 삭제.
df1.drop(['b','c'], axis = 0)   # 여러개 삭제 가능(리스트 전달)
df1.drop(0, axis = 0)           # 위치기반 삭제 불가, 라벨(이름)기반 삭제만 가능.


# [ 연습 문제 ]
# 1. 아래와 같은 데이터 프레임 생성 후(세 개의 컬럼을 갖는)
# name price qty
# apple 2000 5
# mango 1500 4
# banana 500 10
# cherry 400 NA
d1 = {'name':['apple','mango','banana','cherry'], 
      'price':[2000,1500,500,400], 
      'qty':[5,4,10,np.nan]}
df1.columns = ['name','price','qty']
df1 = pd.DataFrame(d1)
df1
df1.dtypes

a1 = np.array([['apple',2000,5],['mango',1500,4],['banana',500,10],['cherry',400,np.nan]])
df2 = pd.DataFrame(a1, index = [1,2,3,4], columns=['name','price','qty'])
df2.dtypes

# 1) mango의 price와  qty 선택
df1.ix[df1.name=='mango',['price','qty']]
df1.loc[df1.name=='mango',['price','qty']]
df1.loc[1,['price','qty']]   # 숫자 전달이 되는 이유 : rowname을 문자로 파싱함.
df1.iloc[1,[1,2]]
df1.iloc[1,1:3]
df1.iloc[1:2,1:3]   # 차원축소 방지

# 2) mango와 cherry 의 price 선택
df1.loc[[1,3],'price']
df1.iloc[[1,3], 1:2]

# 3) 전체 과일의 price만 선택
df1.loc[:,'price']
df1.price
df1['price']

# 4) qty의 평균
np.array([1,2,3,np.nan]).mean()   # numpy의 .mean()은 NA 무시 X.
df1.qty.mean()                    # pandas의 .mean()은 NA 무시. 3개의 평균이 계산.
                                  # skipna = True가 default.
df1.qty.mean(skipna = False)


df1.qty[df1.qty.isnull()] = 0   # NA 치환.
df1.qty.mean()

# [ 참고 ] - numpy와 pandas의 var 매서드 비교
a1 = [1,2,3,4]
s1 = pd.Series(a1)

a1.var()   # 1.25, ddof = 0, 편차제곱합 / 4.
s1.var()   # 1.67, ddof = 1, 편차제곱합 / 3.
s1.var(ddof = 0)   # 만약 s1.var()의 값을 a1.var()와 동일하게 맞추고 싶다면,
                   # a1.var()와 같은 결과

# 5) price가 1000 이상인 과일 이름 출력
df1.loc[df1.price >= 1000, 'name']
df1.ix[df1.price >= 1000, 'name']
df1.iloc[df1.price >= 1000, 'name']   # iloc는 boolean indexing 불가

# 6) cherry, banana, mango, apple 순 출력
df1.iloc[[3,2,1,0], :]
pd.DataFrame(df1, index = [3,2,1,0])

# 7) qty -> QTY 수정
# sol1)
df1.columns = ['name','price','QTY']

# sol2)
df1.columns.values[2] = 'QTY'

# 8) name에 'a'를 포함하는 행 출력
df1.name in 'a'   # 불가
'a' in 'apple'   # 스칼라에서만 수행 가능. 벡터 연산 불가. map처리로 풀기!!!
df1.ix[list(map(lambda x : 'a' in x, df1.name)), :]
df1.loc[list(map(lambda x : 'a' in x, df1.name)), :]

# 9) name값을 rowname으로 설정 후 name 컬럼 제외
df1.index = df1.name
df1.drop('name',axis=1)

# 10) apple과 cherry 행 삭제
df1.drop(['apple','cherry'], axis = 0)
