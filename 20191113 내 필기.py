# sampling - radiant
#run pro
import numpy as np
import pandas as pd
cancer = pd.read_csv('cancer.csv', engine = 'python')

# sample number 추출
rn = np.random.randint(0,                                     # 시작값
                       cancer.shape[0],                       # 끝값
                       size = round(cancer.shape[0] * 0.7))   # 추출 개수

# sampling
cancer_train = cancer.iloc[rn]
cancer_test = cancer.drop(rn)

# get_dummies : dummy variable 생성
# - dummy variable : 문자형 변수를 이진 데이터(0과 1)로만 표현하는 방식
# 1) 변수가 갖는 문자의 개수만큼 분할
# Y  Y_A  Y_B  Y_C
# A   1    0    0
# B   0    1    0
# C   0    0    1
# A   1    0    0

# 2) 변수가 갖는 문자의 개수-1 만큼 분할
# Y  Y_A  Y_B
# A   1    0
# B   0    1
# C   0    0
# A   1    0

pd.get_dummies(cancer['diagnosis'])
pd.get_dummies(cancer['diagnosis'], prefix='Y')

# 예제) 다음의 Y데이터를 더미변수로 만든 후 기존 데이터와 결합
df1 = pd.DataFrame({'Y' : ['A','A','B','C','B'],
                    'SAL' : [900,1200,2000,2200,3000]})

df1_dum = pd.get_dummies(df1['Y'], prefix = 'Y')

df1.join(df1_dum)   # index 이름이 같은 행 끼리 조인
df1['SAL'].join(df1_dum)     # 'Series' object has no attribute 'join'. DataFrame으로 만들어줘야 함.
                             # 에러 발생, Series에 join 매서드 호출 불가
df1[['SAL']].join(df1_dum)   # 이런식으로 []를 한번 더 사용함으로 DataFrame으로 변환된다.
                             # DataFrame 변경 후 join 매서드 호출 가능

# 참고 : 특정 컬럼 선택 시 차원 축소
df1['SAL']     # Series 출력, 차원 축소 발생.
df1[['SAL']]   # DataFrame 출력, 차원 축소 발생 X.

# join 매서드
pd.Series(['ab','bc','cd']).str.join(';')   # 벡터화 join 매서드
';'.join(['a','b','c'])                     # 문자열 join 매서드

pd.Series(['a;b;c', 'A;B;C']).str.split(';').str.join('')

# Series에 정규식 표현식 전달
s1 = pd.Series(['av1 ac1@naver.com 1 1', 'a . bc@daum.net a f'])
import re
pattern1 = re.compile('([a-z0-9]+)@([a-z]+)\.([a-z]{3,3})', flags=re.IGNORECASE)
pattern1.findall(s1)       # Series 전달 불가
s1.str.findall(pattern1)   # str.findall을 통해 Series 적용 가능
s1.str.findall(pattern1).str[0].str[0]

# [ 연습 문제 ]
# ncs학원검색.txt 파일을 읽고 다음과 같은 데이터 프레임 형식으로 출력
# name         addr         tel           start        end
# 아이티윌  서울 강남구  02-6255-8001  2018-10-12  2019-03-27

# 파일 불러오기
c1 = open('ncs학원검색.txt')
txt1 = c1.readlines()
c1.close()

pd.Series(txt1).replace('\n', np.nan)   # 공백을 포함한 \n 문자열 치환 X
s_ncs = pd.Series(txt1).str.strip().replace('',np.nan).dropna()

pat1 = re.compile('(.+) \( (.+) ☎ ([0-9-]+) \) .+ : ([0-9-]+) ~ ([0-9-]+)')
v_name = s_ncs.str.findall(pat1).str[0].dropna().str[0].str.strip()
v_addr = s_ncs.str.findall(pat1).str[0].dropna().str[1].str.strip()
v_tel = s_ncs.str.findall(pat1).str[0].dropna().str[2].str.strip()
v_start = s_ncs.str.findall(pat1).str[0].dropna().str[3].str.strip()
v_end = s_ncs.str.findall(pat1).str[0].dropna().str[4].str.strip()

df_ncs = pd.DataFrame({'name' : v_name, 'addr' : v_addr, 'tel' : v_tel, 'start' : v_start, 'end' : v_end})
df_ncs.loc[df_ncs['addr'].str.contains('강남'),:]
df_ncs['name'].str.strip() == '아이티윌'   # 전처리 작업에서 str.strip()을 안한경우에 사용.
                                          # name 컬름의 값이 공백을 포함하는 경우 해당 조건으로 검색되지 않음. 
df_ncs['name'] == '아이티윌'

# Groupby 매서드 : 그룹핑 기능(분리-적용-결합)
# - 분리-적용-결합
# - groupby 매서드만 적용시 데이터 분리만 수행

emp = pd.read_csv('emp.csv', engine = 'python')

emp.groupby('DEPTNO').mean()   # 숫자 컬럼만 연산
emp.groupby('DEPTNO').mean()['SAL']   # 전체 컬럼 연산 후 컬럼 선택.
                                      # 전체 컬럼의 평균을 구한 후 SAL 컬럼 선택
emp.groupby('DEPTNO')['SAL'].mean()   # 선택적으로 연산하므로 성능상 유리.
                                      # SAL 컬럼만 선택한 후 평균 계산
emp['SAL'].groupby('DEPTNO').mean()        # 에러. deptno가 어디에 있는건지 출처가 불분명.
emp['SAL'].groupby(emp['DEPTNO']).mean()   # 이렇게 deptno의 출처를 밝혀줘야 함. 속도상 가장 유리.


# [ 참고 : Oracle에서의 그룹 연산 시 데이터의 선택 ]
# select mean(sal)
#   from ...
#  where deptno != 10  (o)
#  group by deptno
# having deptno != 10  (x)

# 다수 groupby 컬럼 전달
emp2 = emp.groupby(['DEPTNO', 'JOB'])['SAL'].mean()   # groupby 컬럼이 multi-index로 출력

# groupby 컬럼을 일반 컬럼으로 변경
# 1) groupby 수행 후 reset_index 처리
emp.groupby(['DEPTNO', 'JOB'])['SAL'].mean().reset_index()
# 2) groupby 수행 시 as_index = False 처리
emp.groupby(['DEPTNO', 'JOB'], as_index = False)['SAL'].mean()

# multi-index를 갖는 데이터의 groupby 적용(level인자 사용)
emp2.groupby(level=0).sum()

# groupby 객체에 여러 함수 적용 : agg
emp.groupby('DEPTNO')['SAL','COMM'].[sum(),mean()]   # 에러
emp.groupby('DEPTNO')['SAL','COMM'].agg(['sum','mean'])

# groupby 객체의 각 컬럼별 서로 다른 함수 적용 : agg에 딕셔너리 전달
emp.groupby('DEPTNO')['SAL','COMM'].agg({'SAL':'sum', 'COMM':'mean'})

# [ 참고 : Oracle과 R에서 컬럼마다 서로 다른 그룹연산 수행 ]
# 1) Oracle
# select sum(sal), avg(comm)
#   from emp
#  group by deptno
 
# 2) R
# ddply(emp, .(deptno), summarise, v1=sum(sal), v2=mean(comm))

# [ 연습 문제 ]
# 1. sales 데이터를 불러와서
sales = pd.read_csv('sales.csv', engine = 'python')

# 1) 각 날짜별 판매량의 합계를 구하여라.
sales.groupby('date')['qty'].sum()
sales.pivot_table(index = 'date', values = 'qty', aggfunc = 'sum')
sales.set_index(['date','code']).sum(level=0)

# 2) 각 code별 판매량의 합계를 구하여라.
sales.groupby('code')['qty'].sum()

# 3) product 데이터를 이용하여 각 날짜별, 상품별 매출의 합계를 구하여라.
product = pd.read_csv('product.csv', engine = 'python')
sales2 = pd.merge(sales, product, on = 'code')

sales2.groupby(['date','product']).apply(lambda x : x['qty'].mul(x['price']))

sales2['total'] = sales2['qty'] * sales2['price']

sales2.groupby(['date','code'])['total'].sum()
