
import numpy as np
import pandas as pd
# 13. multi - index
# 3) multi-index 연산(산술매서드)
df5 = pd.DataFrame(np.arange(1,17).reshape(4,4),
                   index=[['AA','AA','BB','BB'],['A','B','A','B']],
                   columns=[['COLA','COLA','COLB','COLB'],['a','b','a','b']])

# 산술연산 매서드의 일반적 방향 : 각 행별, 각 열별(multi-index도 그대로 적용)
df5.sum(0)   # 세로방향이므로 각 컬럼별 합이 상, 하위 레벨별 모두 출력
df5.sum(1)   # 가로방향이므로 각 행별 합이 상, 하위 레벨별 모두 출력

# 산술연산 매서드의 level지정 : 각 레벨이 같은 값 끼리 그룹연산 가능
df5.sum(axis = 0, level = 0)   # 인덱스의 상위레벨이 같은 값 끼리 연산
df5.sum(axis = 0, level = 1)   # 인덱스의 하위레벨이 같은 값 끼리 연산

df5.sum(axis = 1, level = 0)   # 컬럼의 상위레벨이 같은 값 끼리 연산
df5.sum(axis = 1, level = 1)   # 컬럼의 하위레벨이 같은 값 끼리 연산


# 4) multi-index level swap
df5.index.names = ['상위인덱스','하위인덱스']
df5.columns.names = ['상위컬럼','하위컬럼']

df5.swaplevel('상위인덱스','하위인덱스', axis = 0)
df5.swaplevel(0,1, axis = 1)   # 이름값, 위치값 모두 다 전달 가능. axis = 0 : 인덱스 방향, axis = 1 : 컬럼방향.

# 색인 객체에 대한 집합 연산자
s1 = pd.Series([1,2,3,4], index = ['a','b','c','d'])
s2 = pd.Series([3,4,5,6], index = ['c','d','e','f'])

s1.index.diff(s2.index)    # index object의 차집합 불가
s1.index.union(s2.index)   # index object의 합집합
s1.index.intersection(s2.index)   # index object의 교집합

# isin 연산자
emp = pd.read_csv('emp.csv', engine = 'python')
emp
# 예제) emp에서 이름이 SMITH와 ALLEN 선택
emp.loc[(emp['ENAME'] == 'SMITH')|(emp['ENAME'] == 'ALLEN'),:]
emp.loc[emp['ENAME'].isin(['SMITH','ALLEN']), :]


#[ 연습 문제 ]
# 병원현황.csv 파일을 읽고 
df6 = pd.read_csv('병원현황.csv', engine = 'python', skiprows=1)

# 1. 다음과 같은 데이터프레임으로 만들어라
#                  2013               
#                1 2 3 4
# 신경과 강남구
#       강동구
#       ....


df6 = df6.drop(['항목','단위'], axis = 1)

# '계' 행 제거
df6.loc[df6['표시과목'] != '계',:]

# multi-index 설정
df6 = df6.set_index(['시군구명칭','표시과목'])

idx1 = df6.columns.map(lambda x : x[:4])
idx2 = df6.columns.map(lambda x : x[6])
df6.columns = [idx1, idx2]

# multi-index 상황에서 '계' 행 삭제
df6 = df6.drop('계', axis = 0, level = 1)

df6 = df6.sort_index(axis=1, level=0)   # 2009 1.2.3.4, 2010 1.2.3.4 ... 이런식
df6.sort_index(axis = 1, level = [0,1], ascending = [True, True])
# df6.sort_index(axis=1, level=1)   # 2009 1, 2010 1, ... 이런식

# [ 참고 : multi-index일 경우 인덱스 정렬 ]
df6.sort_index(axis = 1, level = [0,1], ascending = [True, True])
df6.sort_index(axis = 1, level = [0,1], ascending = [True, False])
df6.sort_index(axis = 1, level = [0,1], ascending = [False, True])
df6.sort_index(axis = 1, level = [0,1], ascending = [False, False])

df6 = df6.sort_index(axis=0, level=1).swaplevel(0,1, axis=0)
df6

# 2. 성형외과의 각 구별 총 합을 출력
df6.loc['성형외과',:].sum(1)

# 3. 강남구의 각 표시과목별 총 합 출력
df6.xs('강남구', axis = 0, level = 1).sum(1)

# 4. 년도별 총 병원수의 합 출력
df6.sum(axis = 1, level = 0).sum()


# stack, unstack : 데이터의 구조 변경
# - unstack : multi-index를 wide하게 column화 하는 과정
# - stack : column을 multi-index화 하는 과정

s1 = pd.Series([1,2,3,4], index = [['A','A','B','B'],['a','b','a','b']])
s1.unstack()   # index의 가장 하위 레벨이 컬럼화
type(s1.unstack())
s1.swaplevel(0,1).unstack()   # index의 가장 상위 레벨이 컬럼화
s1.unstack(level=0)           # level옵션. index의 가장 상위 레벨이 컬럼화

df_stack = s1.unstack(level=0)
df_stack.stack()   # column이 index의 가장 하위 레벨로 stack처리됨.
df_stack.stack(level = 0)
df_stack.iloc[1,1] = np.nan
df_stack.stack()               # dropna = True
df_stack.stack(dropna=False)   # dropna = False 옵션으로 NA 행 표현
