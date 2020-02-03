import pandas as pd
import numpy as np
# 사용자 정의 그룹핑
# 1) 딕셔너리 전달 : 각 인덱스 이름, 컬럼이름에 매칭되는 그룹이름을 딕셔너리로 전달
df4 = pd.DataFrame(np.arange(0,20).reshape(4,5), columns = ['a','b','c','d','e'])
df4
dic1 = {'a':'g1','b':'g1','c':'g2','d':'g2','e':'g2'}   # 컬럼을 그룹화하여 연산을 하려면 dictionary를 사용하여 그룹핑한다.
df4.groupby(dic1, axis = 1).sum()

# 2) 리스트 전달 : 각 행, 컬럼마다 그룹이름을 리스트로 전달
df4
df4.groupby(['g1','g1','g2','g2','g2'], axis=1).sum()
df4.groupby(['g1','g1','g2','g2']).sum()   # axis = 0 이 default

# 3) Series 전달
s_group = pd.Series(['g1','g1','g2','g2','g2'], index=['a','b','c','d','e'])
df4.groupby(s_group, axis = 1).sum()

# 4) cut object 전달
c1 = pd.cut(df5['시간대'], [0,12,24], include_lowest = True, labels=['오전','오후'])
df5.groupby(c1)['통화건수'].sum()

df4.groupby(['g1','g1','g2','g2']).sum()
c2 = pd.cut(df4.index.values, [-1,1,4], labels=['g1','g2'])
df4.groupby(c2).sum()

# [ 연습문제 ]
# 1. delivery.csv 파일을 읽고
deli = pd.read_csv('delivery.csv', engine = 'python')
df5 = pd.read_csv('delivery.csv', engine = 'python', parse_dates=['일자'])   # parse_dates : 날짜 파싱 옵션. 반드시 리스트로 전달할 것!!!

# 1) 요일별로 각 업종별 통화건수 총 합 확인
from datetime import datetime
deli['요일'] = deli.loc[:,'일자'].map(lambda x : datetime.strptime(str(x),'%Y%m%d').strftime('%A'))
deli.groupby(['요일','업종'])['통화건수'].sum().unstack()
deli

### 선생님 ###
# 요일 출력
df5['요일'] = df5['일자'].map(lambda x : x.strftime('%A')).str.upper()

df5.groupby(['요일','업종'])['통화건수'].sum()

# 2) 평일과 주말(금,토,일)로 그룹을 나누어서 각 그룹별 시군구별 통화건수 총 합 출력
deli['그룹'] = pd.Series(np.where(deli.loc[:,'요일'].isin(['Friday' or 'Saturday' or 'Sunday']),'주말','평일'))

deli2 = deli.groupby(['시군구','요일'])['통화건수'].sum().unstack()
dic2 = {'Friday' : '주말', 'Monday' : '평일', 'Saturday' : '주말', 'Sunday' : '주말', 'Thursday' : '평일', 'Tuesday' : '평일', 'Wednesday' : '평일'}
deli2.groupby(dic2, axis=1).sum()

deli.groupby(['시군구','그룹'])['통화건수'].sum().unstack()


### 선생님 ###
df6 = df5.groupby(['요일','시군구'])['통화건수'].sum().unstack()
df6.groupby({'FRIDAY':'주말', 'MONDAY':'평일','SATURDAY':'주말','SUNDAY':'주말','THURSDAY':'평일','TUESDAY':'평일','WEDNESDAY':'평일'}).sum()
df6.groupby(['주말','평일','주말','주말','평일','평일','평일'], axis=0).sum()   # 인덱스 순서대로 전달.

# 사용자 정의 함수 그룹핑
f2 = lambda x : x.max() - x.min()
df4.apply(f2, axis = 1)

df4.stack().groupby(level=0).apply(f2)   # groupby에서 이미 방향과 레벨을 설정해 주어서, apply에 따로 각각 전달할 필요 없다.
                                         # groupby에 사용자 정의 함수를 전달할 때 apply적용.
                                         
# [ 연습 문제 ]
# 1. fruits.csv 파일을 읽고
fruits = pd.read_csv('fruits.csv', engine='python')                                         
# 1) 년도별 이름별 qty의 총합, price의 평균 출력
fruits.groupby(['year','name']).agg({'qty':'sum','price':'mean'})

# 2) apple과 banana는 group_a, 나머지는 group_b로 묶고 각 그룹별 qty 총합
dic2 ={'apple':'group_a','banana':'group_a','berry':'group_b','peach':'group_b'} 
fruits.name.map(dic2)
fruits.groupby(fruits.name.map(dic2))['qty'].sum()   # 본래 groupby에 전달되는 값은 인덱스 값인데, 현재 문제는 하나의 컬럼이다.
                                                     # 그럴 경우 다음과 같이 groupby에 위치값을 주면 된다.

# 2. student.csv와 exam_01.csv 파일을 읽고
std = pd.read_csv('student.csv', engine='python')
exam = pd.read_csv('exam_01.csv', engine='python')
std2 = pd.merge(std, exam, on = 'STUDNO')

# 1) 각 성별 A,B,C 그룹에 해당되는 학생 수 출력
# (단, A그룹은 시험성적이 90이상, B그룹은 70이상, C그룹은 나머지)
std2['성별'] = std['JUMIN'].astype('str').str[6].replace({'1':'남자','2':'여자'})
std['JUMIN'].astype('str').str[6].map({'1':'남자','2':'여자'})   # replace 혹은 map도 가능.
std2['등급'] = pd.cut(std2['TOTAL'], [0,70,90,101], right=False, labels = ['C','B','A'])   # 101 : 100점을 받은 학생은 어떤 그룹에 포함되지 못하므로, 101점이라는 존재하지 않는 점수를 범위에 부여.
std2.groupby(['성별','등급'])['STUDNO'].count().unstack().fillna(0).astype('int')

# groupby-transform
std = pd.read_csv('student.csv', engine='python')
std.groupby('GRADE')['WEIGHT'].max()            # ddply-summarise in R

std.groupby('GRADE')['WEIGHT'].transform(max)   # ddply-transform in R
std_tr = std.groupby('GRADE')[['WEIGHT']].transform(max)   # ['WEIGHT'] -> [['WEIGHT']]으로 변경함으로써 Series를 DataFrame으로 출력
std.join(std_tr, lsuffix='_x', rsuffix='_y')   # ddply-transform in R
                                               # 인덱스의 이름이 동일하여서 lsuffix와 rsuffix 옵션 사용.

df4 = pd.DataFrame(np.arange(0,20).reshape(4,5), columns = ['a','b','c','d','e'])
df4.groupby(['g1','g1','g2','g2']).sum()            # 0,1행 g1그룹, 2,3행 g2그룹
df4.groupby(['g1','g1','g2','g2']).transform(sum)   # 각 행마다 그룹 연산 결과 동일하게 출력

# group_keys : groupby 결과의 index(groupby column) 생략 시 필요
std.groupby(['GRADE','DEPTNO1'], group_keys=False)[['WEIGHT']].mean()   # 출력값을 구분할 타 인덱스가 없으므로 group_keys=False가 작동이 안돼는 것.

f_sort = lambda x,y : x.sort_values(by=y)[0:1]   # [0:1] : 차원축소방지 목적

df4.stack().reset_index().groupby('level_0').sum()
df4.stack().reset_index().groupby('level_0').apply(f_sort, y='level_1')
df4.stack().reset_index().groupby('level_0', group_keys=False).apply(f_sort, y='level_1')

# [ 연습 문제 ]
# 1. taxi_call.csv 데이터를 사용하여
taxi = pd.read_csv('taxi_call.csv', engine='python')
# 1) 구별 택시콜이 가장 많은 시간대를 출력
taxi.groupby(['발신지_시군구','시간대'])['통화건수'].count().groupby(level=0).idxmax().str[1]

# 2) 다음의 시간대별 통화건수의 총 합 출력
# 20 ~ 03시, 03 ~ 08시, 08 ~ 15시, 15 ~ 20시
pd.cut(taxi['시간대'], [20,3,8,15,20])
taxi.groupby(['발신지_시군구','시간대'])['통화건수'].sum().unstack().fillna(0)
taxi.groupby('시간대')['통화건수'].sum()
