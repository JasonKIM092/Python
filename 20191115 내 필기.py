# 시계열
from datetime import datetime

# 1. 현재 날짜 및 시간 출력
d1 = datetime.now()   # Sys.Date(), sysdate

d1.year    # 년(d1은 반드시 datetime 형식이어야 가능)
d1.month   # 월(d1은 반드시 datetime 형식이어야 가능)
d1.day     # 일(d1은 반드시 datetime 형식이어야 가능))

# 2. 날짜 파싱
v1 = '2019/11/11'
v2 = 20190112
l1 = ['2019/01/11','2019/01/12']
datetime.strptime(v1, '%Y/%m/%d')   # 문자 스칼라(문자열) 파싱 가능
datetime.strptime(v2, '%Y%m%d')     # strptime() argument 1 must be str, not int
                                    # 숫자 스칼라 파싱 불가
datetime.strptime(str(v2), '%Y%m%d')

datetime.strptime(l1, '%Y/%m/%d')   # strptime() argument 1 must be str, not list
                                    # 리스트 파싱 불가(벡터 연산 불가)
# 1) datetime.strptime의 반복 처리
list(map(lambda x : datetime.strptime(x, '%Y/%m/%d'), l1))   # map함수로 반복
[datetime.strptime(i, '%Y/%m/%d') for i in l1]               # 리스트 내포 표현식으로 반복

# 2) pd.to_datetime(벡터연산 가능)
import pandas as pd
pd.to_datetime(l1, format = '%Y/%m/%d')

# 3. 날짜 포멧 변경
d1.strftime('%Y')   # 년
d1.strftime('%m')   # 월
d1.strftime('%d')   # 일
d1.strftime('%A')   # 요일(문자)
d1.strftime('%w')   # 요일(숫자)

# 4. 날짜(스칼라) 연산
from datetime import timedelta
d2 = datetime(2019,10,11)

# 1) 날짜와 날짜의 연산 : timedelta로 리턴
d2 - d1              # 날짜 - 날짜 연산 가능(timedelta 형태로 리턴)
(d1 - d2).days       # 두 날짜의 시간차(일 기준)

# 2) 날짜와 숫자의 연산 : 기본적으로 불가, 숫자를 timedelta 형식으로 변경 처리 후 연산 가능
d1 + 10   # unsupported operand type(s) for +: 'datetime.datetime' and 'int'
          # 날짜 + 숫자 연산 불가
d1 + timedelta(10)     # timedelta의 기본 단위는 "일" 수
d1 + timedelta(1)      # timedelta의 기본 단위는 "일" 수, 하루 뒤
d1 + timedelta(1/24)   # timedelta의 기본 단위는 "일" 수, 한시간 뒤

# 3) 날짜와 숫자의 연산 :  기본적으로 불가, 숫자를 offset 형식으로 변경 처리 후 연산 가능
import pandas.tseries.offsets
from pandas.tseries.offsets import Day, Hour, Second

d1 + Day(10)      # 10일 뒤
d1 + Hour(10)     # 10시간 뒤
d1 + Second(10)   # 10초 뒤

# [ 연습 문제 ]
# emp.csv 파일을 읽고
emp = pd.read_csv('emp.csv', engine='python')
# 1) 급여 검토일의 요일 출력 (단, 급여 검토일은 입사날짜의 100일 후 날짜)
(emp['HIREDATE'].map(lambda x : datetime.strptime(x,'%Y-%m-%d %H:%M')) + timedelta(100)).map(lambda x : x.strftime('%A'))

(pd.to_datetime(emp['HIREDATE']) + Day(100)).map(lambda x : x.strftime('%A'))

# 2) 입사일로부터 근무일수 출력
datetime.now() - emp['HIREDATE'].map(lambda x : datetime.strptime(x,'%Y-%m-%d %H:%M'))

(datetime.now() - pd.to_datetime(emp['HIREDATE'])).map(lambda x : x.days)

# 5. 날짜 인덱싱 및 색인
# np.arange : 연속적 정수 출력
import numpy as np
pd.date_range(start = '2019/01/01', end = '2019/01/31', freq='D')        # 매일
pd.date_range(start = '2019/01/01', end = '2019/01/31', freq='7D')       # 7일 마다의 연속날짜
pd.date_range(start = '2019/01/01', end = '2019/01/31', freq='W')        # 매주 일요일. freq='W' : freq='W-SUN' default
pd.date_range(start = '2019/01/01', end = '2019/01/31', freq='W-MON')    # 매주 월요일
pd.date_range(start = '2019/01/01', freq='7D')                           # 마지막값 설정 오류
pd.date_range(start = '2019/01/01', periods = 30, freq='7D')             # periods 옵션으로 설정가능.

s1 = pd.date_range(start = '2019/01/01', end = '2019/01/31', freq='D')
s2 = np.arange(1,32)

s_time = pd.Series(s2, index=s1)

s_time[::2]
s_time + s_time[::2]
s_time.add(s_time[::2], fill_value = 0)

# datetime index의 색인
s3 = pd.date_range('2019/01/01', '2019/06/30', freq = 'W-MON')
s4 = np.arange(1,len(s3)+1)

s_time2 = pd.Series(s4, index=s3)
s_time2['2019-05']   # 일부 구간만 검색해도 파싱이 되어서 여러개의 원하는 결과값을 추출이 가능하다.

s3 = pd.date_range('2019/01/01', '2019/06/30', freq = 'W-MON')
s4 = np.arange(1,len(s3)+1)
s5 = np.arange(0,len(s3))

s_time3 = pd.Series(s, index=s3)

s_time2 = pd.Series(s4, index=s3)
s_time2['2019-05']   # 일부 구간만 검색해도 파싱이 되어서 여러개의 원하는 결과값을 추출이 가능하다.