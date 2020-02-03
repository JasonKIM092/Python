import numpy as np
import pandas as pd

# [ 연습 문제 ] - card_history.txt 파일을 읽고
a3 = np.loadtxt('card_history.txt', dtype = 'str', encoding = 'utf8')
df3 = pd.DataFrame(a3)
df3.columns = df3.iloc[0,:]
df3 = df3.drop(0, axis = 0)
df3.set_index('NUM')   # df3.index = df3.iloc[:,0]
                       # df3 = df3.drop('NUM',axis=1)
df3 = df3.applymap(lambda x : x.replace(',','')).astype('int')
df3

# 1) 각 일별 지출품목의 차지 비율 출력(식료품 : 20%, 의복 : 45%, ...)
f2 = lambda x : round(x/x.sum() * 100,2)
df3.apply(f2, axis = 1)

df3.apply(lambda x : round(x/x.sum() * 100,2), axis = 1)

df3.loc['1',:] / df3.loc['1',:].sum() * 100   # 1일의 각 품목별 지출비율
df3.loc['2',:] / df3.loc['2',:].sum() * 100   # 2일의 각 품목별 지출비율
df3.loc['3',:] / df3.loc['3',:].sum() * 100   # 3일의 각 품목별 지출비율
df3.loc['4',:] / df3.loc['4',:].sum() * 100   # 4일의 각 품목별 지출비율

# 2) 각 지출품목별 일의 차지 비율 출력(1일 : 0.7, 2일 : 1.1, ...)
f2 = lambda x : round(x/x.sum() * 100,2)
df3.apply(f2, axis = 0)

df3.apply(lambda x : round(x/x.sum() * 100,2), axis = 0)

df3['식료품'] / df3['식료품'].sum() * 100
df3['의복'] / df3['의복'].sum() * 100

# 3) 각 일별 지출비용이 가장 높은 품목 출력
df3.idxmax(1)

# 4) 각 일별 지출비용이 가장 높은 두 개 품목 출력
def top(data, n=5) : 
    return pd.Series(data.sort_values(ascending=False)[:n].index)

df3.apply(top, n=2, axis=1) 



df3.loc['1',:].sort_values(ascending=False)[:2].index
df3.loc['2',:].sort_values(ascending=False)[:2]
df3.loc['3',:].sort_values(ascending=False)[:2]

def f_top(data, n=5) : 
    return data.sort_values(ascending=False)[:n]

df3.apply(f_top, axis=1, n=3)


# 12. 기타
# - unique
df3.idxmax(1).unique()

# - count : NA가 아닌 데이터의 개수 세기
from numpy import nan as NA
df3.idxmax(1).count()
pd.Series[(1,2,NA,3)].count()   # NA 제외, NULL 제외

# - value_count
pd.Series(['a','a','b','c','c','c']).value_counts()
pd.Series(['a','a','b','c','c','c']).value_counts().sort_index()

# 13. multi - index
- index와 column이 여러 level(depth)로 구성되어 있는 경우(Python 가능, R 불가)

# 1) multi-index 생성
		col1	col2
A	a	   1	   2
	b	   3	   4
B	a	   5	   6
	b	   7	   8
    
df5 = pd.DataFrame(np.arange(1,9).reshape(4,2))
df5.columns = ['col1', 'col2']
df5.index = [['A','A','B','B'],['a','b','a','b']]
df5


		col_a		    col_b	
		col1	col2	col1	col2
A	a	   1	   2	   3	   4
	b	   5	   6	   7	   8
B	a	   9	  10	  11	  12
	b	  13	  14	  15	  16

df6 = pd.DataFrame(np.arange(1,17).reshape(4,4))
df6.index = [['A','A','B','B'],['a','b','a','b']]
df6.columns = [['col_a','col_a','col_b','col_b'],['col1','col2','col1','col2']]
df6

# 외부파일 불러오기 함수
- np.loadtxt : array로 저장
- pd.read_csv : DataFrame으로 저장

df7 = pd.read_csv('multi_index.csv', encoding = 'cp949')
df7.columns = [['a','a','냉장고','냉장고','TV','TV'],['a','a','price','qty','price','qty']]
df7 = df7.drop(0,axis=0)

df7.index = [['seoul','seoul','incheon','incheon'],['A','B','A','B']]
df7 = df7.drop([['a','a'],['a','a']],axis=1)

df7


# [ 연습 문제 : multi_index.csv 파일을 읽고 멀티 인덱스 설정 ]
df7 = pd.read_csv('multi_index.csv', encoding='cp949')
df7 = df7.fillna(method = 'ffill')
df7 = df7.set_index(['Unnamed: 0', 'Unnamed: 1'])
df7.columns = [['냉장고','냉장고','TV','TV'], df7.iloc[0,:]]

df7.iloc[1:,]   # 첫번째 행 제거
df7 = df7.drop(np.nan, axis = 0, level = 0)   # level : multi_index에서 삭제할 때 사용.
                                              # drop 매서드의 level 선택으로 첫번째 행(NA) 제거
df7
df7.index.names = ['지역','지점']
df7.columns.names = ['품명','구분']

# 2) multi-index 색인
# - 색인매서드 ix, loc, iloc : 기본은 상위 레벨의 값만 색인 가능
# - 색인매서드 ix, loc, iloc : 튜플 전달 시 하위 레벨의 값 색인 가능
# - xs : 하위 레벨 직접 색인 가능한 색인 매서드

df7.loc['seoul','냉장고']   # 색인가능. 상위레벨값.
df7.loc['seoul','price']   # error. 하위레벨만 전달 시 불가.
df7.loc['seoul',('냉장고','price')]   # 색인가능. 하위레벨 튜플전달.
df7.loc['seoul',[('냉장고','price'),('TV','price')]]   # 튜플도 리스트로 묶어서 전달 가능.
df7.loc[('seoul','B'),:]

df7.xs('price', axis = 1, level = 1)

df7.xs('A', axis = 0, level = 1)

# 3) multi-index 연산(산술매서드)

