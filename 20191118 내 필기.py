import pandas as pd

df1 = pd.read_csv('부동산_매매지수.csv', engine = 'python', skiprows = [0,2])
df1.dtypes
df1 = df1.dropna(how='all')
df1.shape[0]
df1.index = pd.date_range('2008/04/07', periods = df1.shape[0], freq='7D')
df1

# resample : 시계열 인덱스의 빈도 변경
df1.resample('M', how='sum')
df1.resample('M').mean()
df1.resample('Y').mean()['2018']

# truncate : 날짜 시계열에 대한 선택
df1.truncate(after='2018-01-01')   # 2018-01-01 이후 날짜 삭제
df1.loc[:'2018-01-01']             # 시계열 인덱스 색인으로도 가능

