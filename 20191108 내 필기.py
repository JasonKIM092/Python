import pandas as pd
import numpy as np
# pd.concat 함수
- oracle의 union 연산자 처럼 서로 분리되어진 데이터를 하나로 병합
- axis=0가 디폴트 이므로 행이 병합(세로방향)
- 결합시 서로 같은 key끼리 결합이 되며 서로 다른 key가 있는 경우 NA 리턴
- ignore_index=True를 통해 결합된 index를 새로 부여할 수 있음

# Series 병합
s1 = pd.Series([1,2,3,4])
s2 = pd.Series([5,6,7,8])
s3 = pd.Series([5,6,7,8,9])

pd.concat([s1,s2])                      # 세로방향 결합, 기존의 index가 그대로 유지
pd.concat([s1,s2], ignore_index=True)   # index가 새로 부여
pd.concat([s1,s2], axis=1)              # 가로방향 결합(컬럼확장)
pd.concat([s1,s3], axis=1)              # NA발생

# DataFrame 병합
df1 = pd.DataFrame(np.arange(1,5).reshape(2,2), columns=['a','b'])
df2 = pd.DataFrame(np.arange(5,9).reshape(2,2), columns=['a','b'])
df3 = pd.DataFrame(np.arange(9,13).reshape(2,2), columns=['a','c'])

pd.concat([df1,df2])
pd.concat([df1,df3])                 # 서로 key가 다르므로 NA 발생(outer join). join='outer'가 디폴트.
pd.concat([df1,df3], join='inner')   # key가 같은 경우만 출력(inner join)
pd.concat([df1,df2], axis=1)

# np.where로 null 치환
# 1. null이 아닌 경우 원래 데이터로부터 값 치환
s1= pd.Series([1,np.nan,3,np.nan,5], index=['a','b','c','d','e'])
np.where(s1.isnull(),0,s1)

# 2. null이 아닌 경우 다른 데이터로부터 값 치환
s2 = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
np.where(s1.isnull(),0,s2)
np.where(s1.isnull(), s2, s1)
        
# combine_first
- oracle의 merge와 비슷(수정과 삽입 동시 처리)
- NA는 치환, 없는 값은 삽입처리

df1 = pd.DataFrame([[1,2],[np.nan,4]], columns=['a','b'])
df2 = pd.DataFrame([[10,20],[30,40],[50,60]], columns = ['a','b'])

df1.combine_first(df2)
df2.combine_first(df1)

# NA치환 기능
s1 = pd.Series([1, np.nan, 3])
s2 = pd.Series([10,20,30])

np.where(s1.isnull(), s2, s1)   # array의 출력
s1.combine_first(s2)            # Series or DataFrame으로 출력

# subway2.csv 데이터를 사용해서
# tidy data 생성
sub_tidy = sub.set_index(['전체','구분']).stack().reset_index()
sub_tidy.columns = ['역','구분','시간','수']

# 1. 각 시간대별 승차의 최대와 최소를 동시 출력
sub_in_max = sub.pivot_table(index='전체', columns = '구분', values=sub.columns[2:], aggfunc = 'sum').xs('승차',axis=1,level=1).idxmax(0)
sub_in_min = sub.pivot_table(index='전체', columns = '구분', values=sub.columns[2:], aggfunc = 'sum').xs('승차',axis=1,level=1).idxmin(0)
pd.concat([sub_in_max, sub_in_min], axis=1, keys=['in_max','in_min'])

sub_tidy2 = sub_tidy.pivot_table(index = ['역','구분'], columns = '시간', values = '수', aggfunc = 'sum')
sub_tidy2_1 = sub_tidy2.xs('승차', axis=0, level=1)
f1 = lambda x : pd.Series([x.max(), x.min()], index=['max','min'])
sub_tidy2_1.apply(f1,0).T

# 2. 각 시간대별 하차가 가장 많은 역과 가장 적은 역이름을 동시 출력
sub_out_max = sub.pivot_table(index='전체', columns = '구분', values=sub.columns[2:], aggfunc = 'sum').xs('하차',axis=1,level=1).idxmax(0)
sub_out_min = sub.pivot_table(index='전체', columns = '구분', values=sub.columns[2:], aggfunc = 'sum').xs('하차',axis=1,level=1).idxmin(0)
pd.concat([sub_out_max, sub_out_min], axis=1, keys=['out_max','out_min'])

sub_tidy2_2 = sub_tidy2.xs('하차', axis=0, level=1)
f2 = lambda x : pd.Series([x.idxmax(), x.idxmin()], index=['max','min'])
sub_tidy2_2.apply(f2,0).T

### 위에까지가 시험범위 ###

# cut
# - 연속형 변수를 범주형 변수로 바꿀수 있는 함수     cf) 연속형 변수를 범주형으로 바꿀경우 예측력이 높아지는 케이스가 있다.
# - cut을 사용하여 사용자가 지정한 범위대로 그룹핑할 수 있음
pd.cut(x = ,                     # 연속형 변수
       bins = ,                  # 나눌 구간값을 갖는 리스트
       right = True,             # 오른쪽 닫힘 여부 (,] : 오른쪽 포함(~초과 ~이하)
                                 # right = False [,) : ~ 이상 ~ 미만
       labels = ,                # 각 구간이 갖는 이름
       include_lowest = False)   # 가장 작은 값 포함 여부

# 예) 시험성적이 0 ~ 100점일때 50점 이하, 50점 초과 80점 이하, 80점 초과 100점 이하 별 학생 수 출력
s1 = pd.Series([14,51,60,89,99,100])
pd.cut(s1, bins = [50,80,100])     # 첫번째 데이터(14)를 포함시킬 그룹이 없어 NA리턴
pd.cut(s1, bins = [0,50,80,100])   # 모든 데이터가 각 그룹에 포함
pd.cut(s1, bins = [0,50,80,100], labels = ['C','B','A'])   # 모든 데이터가 각 그룹에 포함
# ( : 초과
# ] : 이하

s2 = pd.Series([0,14,51,60,89,99,100])
pd.cut(s2, bins = [0,50,80,100])   # 0은 그룹에 포함 안됨
pd.cut(s2, bins = [0,50,80,100], include_lowest = True)   # 0도 그룹에 포함됨
