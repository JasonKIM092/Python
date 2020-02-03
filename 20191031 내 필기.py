# 1. DataFrame 생성

# 2. DataFrame 매서드

# 3. DataFrame 수정

# 4. DataFrame 색인

# 5. DataFrame 구조 수정
import numpy as np
import pandas as pd
a1 = np.arange(1,13).reshape(4,3)
a2 = np.array([13,14,15]).reshape(1,3)

df1 = pd.DataFrame(a1, columns=['a','b','c'])
df2 = pd.DataFrame(a2, columns=['a','b','c'])

# 1) row 추가
df1.append(df2)                        # 새로 추가되는 df2의 index가 그대로 전달
df1.append(df2, ignore_index = True)   # df1 index에 이어서 전달
df1 = df1.append(df2, ignore_index = True)

# 2) column 추가
df1['d'] = [10,20,30,40,50]
df1

# 6. 산술연산
df3 = df1[['a','b']]
df4 = df1[['c','d']]
df4.columns = ['a','b']
df5 = df4.drop(4, axis=0)     # 이름기입. 위치값 X.
df6 = df4.drop('b', axis=1)   # 이름기입. 위치값 X.
df100 = df1[['c','d']]

df3 + df4     # 서로 같은 index, column끼리 연산
df3 + df5     # index가 일치하지 않는 값 NA 리턴
df3 + df6     # column이 일치하지 않는 값 NA 리턴
df3 + df100   # column key가 일치하지 않는 값 NA 리턴

# 산술연산 매서드(add(+), sub(-), div(/), mul(*))
df3 + df4
df3.add(df4)

df3 + df5
df3.add(df5, fill_value=0)   # NA + 3 => 0 + 3으로 연산시킴. 결과값이 NA가 아니라 3으로 리턴.
df3 +  df5.reindex(df3.index, axis = 0, fill_value = 0)

# 산술연산의 브로드캐스팅 기능(반복연산) : DataFrame + Series 연산 시
a11 = np.arange(1,9).reshape(4,2)
df11 = pd.DataFrame(a11, columns=['a','b'])

s1 = df11.iloc[0,:]   # 첫번째 행 선택(Series)
s2 = df11.iloc[:,0]   # 첫번째 컬럼 선택(Series)

df11 + s1                 # 반복연산 가능, (4 X 2) + (1 X 2). 행 반복일때는 굳이 산술연산 매서드 필요 없음.
                          # DataFrame + Series의 행 반복일 경우 반복연산 가능.
df11 + s2                 # 반복연산 불가, NA 리턴, 컬럼끼리 key값이 안맞아서 연산결과값 이상. key 확장.
df11 + df11.iloc[:,0:1]   # 반복연산 불가, NA 리턴.
df11.add(s2, axis = 0)    # 반복연산 가능. axis = 1로 쓰면 key가 안맞아서 NA가 출력. 컬럼을 반복연산할 때는 산술연산 매서드 필요.
                          # DataFrame + Series의 컬럼 반복일 경우 axis = 0 전달

# [ 참고 : array의 브로드캐스팅 기능 ]
a11[0,:]
a11 + a11[0,:]                # 연산 가능. (4 X 2) + (1 X 2)

a11[:,0]
a11 + a11[:,0]                # 연산 불가. (4 X 2) + (1 X 4)
a11 + a11[:,0].reshape(4,1)   # 연산 가능. (4 X 2) + (4 X 1)
a11 + a11[:,0:1]              # 연산 가능. (4 X 2) + (4 X 1)

a11[:,0:1]   # 차원축소 방지라서 (4 X 1) 형태.


# 7. reindex 기능
pd.DataFrame(df5, index = df3.index)

df5.reindex(df3.index,
            axis = 0,        # 재배치 방향 지정(0:행, 1:컬럼). default : axis = 0.
            fill_value = 0   # 재색인되는 과정에서 새로 추가된 NA를 치환하고자 할 때 사용.
            )

df5.reindex(df3.index,
            axis = 0,          # 재배치 방향 지정(0:행, 1:컬럼). default : axis = 0.
            method = 'ffill'   # NA부분을 이전값 혹은 다음값으로 치환하고자 할 때 사용.
                               # 'ffill' : NA를 이전 값으로 치환
                               # 'bfill' : NA를 이후 값으로 치환
            )

df5.reindex(df3.index, axis = 0, fill_value = 0)
df5.reindex(['a','b','c'], axis = 1)

# [ 연습 문제 ]
# 1. 3 X 4 배열 생성 후 a,b,c,d 컬럼을 갖는 df1 데이터프레임 생성
a1 = np.arange(1,13).reshape(3,4)
df1 = pd.DataFrame(a1, columns = ['a','b','c','d'])
df1

# 2. 2 X 4 배열 생성 후 a,b,c,d 컬럼을 갖는 df2 데이터프레임 생성
a2 = np.arange(1,9).reshape(2,4)
df2 = pd.DataFrame(a2, columns = ['a','b','c','d'])

# 3. 위 두 데이터프레임 union 후 df3 생성
df3 = df1.append(df2, ignore_index = True)

# 4. df3에서 0,2,4 행 선택해서 새로운 데이터 프레임 df4 생성
df4 = df3.iloc[[0,2,4],:]
df4

# 5. df3에서 'b','d' 컬럼 선택 후 새로운 데이터 프레임 df5 선택
df5 = df3.loc[:,['b','d']]
df5

df5 = df3[['b','d']]   # 컬럼 우선순위.

# 6. df3 - df4 수행(NA 리턴 없이)
# 1) 산술연산 매서드
df3.sub(df4, fill_value = 0)

# 2) reindex
df3 - df4.reindex(df3.index, axis = 0, fill_value = 0)

# 7. df3 * df5 수행(NA 리턴 없이)
# '*' 라서 fill_value = 1
# 1) 산술연산 매서드
df3.mul(df5, fill_value = 1)

# 2) reindex
df3 * df5.reindex(df3.columns, axis = 1, fill_value = 1)

# 8. 정렬
# index(column) 순 사용자 지정 정렬
pd.DataFrame(df3, index = [1,2,3,4,0])   # index 정렬
df3.reindex([1,2,3,4,0], axis = 0)       # index 정렬

pd.DataFrame(df3, columns = ['b','c','d','a'])   # column 정렬
df3.reindex(['b','c','d','a'], axis = 1)         # column 정렬

# index(column) 순서대로 정렬
df3.sort_index(axis = 0,               # 정렬방향(0:index, 1:column)
               ascending = True,       # 정렬순서(내림차순, 오름차순)
               na_position = 'last')   # NA 정렬 순서('last' : 맨 끝, 'first' : 맨 앞)

df3.sort_index(axis = 0, ascending = False, na_position = 'last')   # index 역순 정렬
df3.sort_index(axis = 1, ascending = False, na_position = 'last')   # column 역순 정렬

# 특정 컬럼 순서대로 정렬
df1 = pd.DataFrame({'a':[5,5,1,1,3,3], 'b':['a','b','d','c','e','a']})
df1.sort_values(by = 'a',              # 정렬 컬럼(리스트 가능)
                ascending = False,     # 정렬 순서(리스트 가능)
                na_position='first')   # 각 NA 위치

df1.sort_values(by = 'a', ascending = False, na_position='first')
df1.sort_values(by = 'a', ascending = True, na_position='first')

df1.sort_values(by=['a','b'], ascending = [True, False])
df1.sort_values(by=['a','b'], ascending = [True, True])

# [ 연습 문제 ]
#1. 다음의 데이터를 배열로 불러온 뒤 다음과 같은 데이터 프레임 형태로 변경
# 7.5	3.6	3.5	3.3	1.5
# 7.4	3.2	3	2.8	1.2
# 6.6	2.9	2	2	1.1
# 7.7	3	2.2	2.2	1
# 7.9	3.1	2.3	2.3	1.2
# 7.7	3.3	2.6	2.5	1.3
# 7.7	3	2.3	2.2	1.4
# 7.1	3.2	2	2.1	1.4
# 7	3.1	2.1	2	1.2
# 7.9	3.6	2.5	2.5	1.6
# 7.8	3.5	2.5	2.4	3
# 7.4	3.4	2.1	2.1	2.7
# 7.5	3	2.1	2.1	2.5
# 7.9	3	2	1.9	1.9

#	20대	30대	40대	50대	60세이상
#2000년	7.5	3.6	3.5	3.3	1.5
#2001년	7.4	3.2	3	2.8	1.2
#2002년	6.6	2.9	2	2	1.1
#..............................................
#2011년	7.4	3.4	2.1	2.1	2.7
#2012년	7.5	3	2.1	2.1	2.5
#2013년	7.9	3	2	1.9	1.9

import pandas as pd
import numpy as np
import my_module as mu
test3 = mu.read_txt('test3.txt', sep = '\t', fmt = str)
df1 = pd.DataFrame(test3)
df1.index = ['2000년','2001년','2002년','2003년','2004년',
             '2005년','2006년','2007년','2008년','2009년',
             '2010년','2011년','2012년','2013년']
df1.columns = ['20대','30대','40대','50대','60세 이상']
df1

# 선생님
a1 = np.loadtxt('test3.txt')
df1 = pd.DataFrame(a1)

idx1 = np.arange(2000,2014).astype('str')
idx1 + '년'   # 문자열 결합 처리 벡터연산 불가.(문자열 + 문자열 벡터연산 불가능.)
'2000' + '년'   # 가능.
df1.index = list(map(lambda x : x + '년', idx1))
df1

np.arange(20,51,10).astype('str')
cols = list(map(lambda x : x + '대', np.arange(20,51,10).astype('str')))
cols.append('60세 이상')
df1.columns = cols
df1

#2. 2010년부터의 20~40대 실업률만 추출하여 새로운 데이터프레임을 만들어라 
df2 = df1.loc[['2010년','2011년','2012년','2013년'],['20대','30대','40대']]
df2

# 선생님
df2 = df1.loc['2010년':,'20대':'40대']

#3. 30대 실업률을 추출하되, 소수점 둘째자리의 표현식으로 출력
df3 = df1.iloc[:,1:2]

# 선생님
df1['30대']

'%.2f' % 3.6
'%.2f' % df1['30대']   # 벡터연산 불가

['%.2f' % x for x in df1['30대']]

#4. 60세 이상 컬럼 제외
df4 = df1.drop('60세 이상', axis=1)
df4

# 선생님
df1.drop('60세 이상', axis = 1)

#5. 30대 컬럼의 값이 높은순 정렬
df1.sort_values(by = '30대', ascending = False)

# 선생님
df1.sort_values('30대', ascending = False)
