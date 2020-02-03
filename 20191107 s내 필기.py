# cross-table 특징
# - 행, 열별 데이터 정리 가능
# - 행별 열별 그룹연산이 쉬움
# - 조인 불가
# - multi-index 생성 후 unstack 처리 혹은 pivot으로 표현 가능

# unstack 시 주의점
# - 다음과 같이 중복값이 있는 경우 unstack을 통한 cross table 생성 불가
# A a
#   b
# B a
#   b
#   b
  
# 예제) unstack_test.csv 파일을 읽고 년도별 성별 정리된 교차 테이블 생성
import numpy as np
import pandas as pd
df1 = pd.read_csv('unstack_test.csv', engine = 'python')
df1.set_index(['년도','성별'])['구매량'].sum(level=[0,1]).unstack()

# [ 연습 문제 ]
# 1. delivery.csv 파일을 읽고
df4 = pd.read_csv('delivery.csv', engine = 'python')
df4
# 1) 각 업종별 통화건수가 많은 순서대로 시군구의 순위를 출력
df4.set_index(['업종','시군구'])['통화건수'].sum(level=[0,1]).unstack(level=0).rank(ascending = False, axis = 0, method = 'min').astype('int')

df4_1 = df4.set_index(['업종','시군구'])['통화건수'].sum(level=[0,1]).unstack(level=0)
df4_1.rank(ascending = False, axis = 0, method = 'min').astype('int')

# 2) 각 시군구별 업종 비율 출력
#        족발/보쌈  중국음식  치킨
# 강남구    31        45     21.5 ...
round(df4.set_index(['시군구','업종'])['통화건수'].sum(level=[0,1]).unstack().apply(lambda x : x/x.sum() * 100, axis=1), 2)

df4_1.apply(lambda x : round(x/x.sum()*100,2), axis=1)

df4_1.apply(lambda x : round(x/x.sum()*100,2), axis=1).sum(1)   # 전체 더해서 100이 나오는지 확인.

# 3) 시간대별 배달콜수가 가장 많은 업종 1개 출력
df4.set_index(['시간대','업종'])['통화건수'].sum(level=[0,1]).unstack().idxmax(1)

df4_2 = df4.set_index(['시간대','업종'])['통화건수'].sum(level=[0,1]).unstack()
df4_2.idxmax(1)


# 외부 파일 불러오기
# 1. read_csv : ','로 구분된 데이터를 주로 불러올때 사용(sep 옵션으로 분리구분기호 전달 가능)
# pd.read_csv(
#     filename = ,
#     sep=',',             # 파일의 분리 구분 기호
#     header='infer',      # 첫 번째 행을 컬럼화 시킬지 여부, None설정 시 컬럼이 아닌 value로 전달
#     names=None,          # 컬럼 이름 변경 및 지정
#     index_col=None,      # index로 설정할 컬럼 이름
#     usecols=None,        # 불러올 컬럼 이름 지정
#     dtype=None,          # 데이터 타입 지정, 딕셔너리 전달을 통해 컬럼별 지정 가능
#     engine=None,          
#     skiprows=None,       # 정수 전달 시 정수 행만큼 제외, 리스트 전달시 해당 위치 행 제외
#     nrows=None,          # 미리 불러오기 기능, 설정된 행만큼만 불러오기
#     na_values=None,      # NA로 인식시킬 문자열 지정, 딕셔너리 전달을 통해 컬럼별 지정 가능
#     parse_dates=False,   # 날짜 컬럼으로 인식시킬 컬럼명을 리스트로 전달
#     chunksize=None,      # 대용량 데이터를 나눠서 불러올 경우 행 수 지정
#     encoding=None        
# )

pd.read_csv('read_test.csv', engine = 'python', header=None, names=['A','B','C','D','E'])
pd.read_csv('read_test.csv', engine = 'python', index_col='date')
pd.read_csv('read_test.csv', engine = 'python', usecols = ['a','b'])
pd.read_csv('read_test.csv', engine = 'python', dtype='str').dtypes
pd.read_csv('read_test.csv', engine = 'python', dtype={'date' : 'str', 'c' : 'float', 'd' : 'float'})
pd.read_csv('read_test.csv', engine = 'python', na_values=['.','-','?','!'])
pd.read_csv('read_test.csv', engine = 'python', na_values={'a' : ['.','-'], 'b' : ['?','!']})
pd.read_csv('read_test.csv', engine = 'python', nrows = 5)
pd.read_csv('read_test.csv', engine = 'python', skiprows = 5)   # 갯수전달
pd.read_csv('read_test.csv', engine = 'python', skiprows = [5])   # row번호 전달
pd.read_csv('read_test.csv', engine = 'python', skiprows = [5,8,9])   # row번호 전달
pd.read_csv('read_test.csv', engine = 'python').dtypes
pd.read_csv('read_test.csv', engine = 'python', parse_dates=['date']).dtypes
pd.read_csv('read_test.csv', engine = 'python', parse_dates=['date']).shape

# chunksize
df_test = pd.read_csv('read_test.csv', engine = 'python', chunksize=30)
# 1) 단순 출력
for i in df_test :
    print(i)

# 2) 하나의 DataFrame으로 결합
df_test2 = pd.DataFrame()
for i in df_test :
    df_test2 = pd.concat([i, df_test2], ignore_index=True)

df_test2

# 3) 원하는 행의 수 만큼 출력 후 결합
# df_test = pd.read_csv('read_test.csv', engine = 'python', chunksize=30)
# df_test.get_chunk(10)    단순 출력. 단, 한번 출력하면 없어짐

df_test = pd.read_csv('read_test.csv', engine = 'python', chunksize=30)
df_test1_1 = df_test.get_chunk(10)
df_test1_2 = df_test.get_chunk(10)

pd.concat([df_test1_1, df_test1_2])


# 2. pd.read_clipboard
pd.read_clipboard()

# 3. cx_Oracle 모듈을 사용한 oracle 데이터베이스에서 파일 불러오기
import cx_Oracle
con1 = cx_Oracle.connect("scott/oracle@192.168.0.84:1521/testdb")   # @ip주소/포트/db이름
pd.read_sql('select * from student', con = con1)
pd.read_sql('select * from student s, exam_01 e where s.studno = e.studno', con=con1)

# [ 참고 : 설치된 오라클 이름 및 서비스 포트 확인 방법 ]
#- cmd 창에서 아래 명령어 수행

#C:\Users\KITCOOP> lsnrctl status
#서비스 요약...
#"testdb" 인스턴스(READY 상태)는 이 서비스에 대해 1 처리기를 가집니다.         # db이름
#  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=DESKTOP-AL444TC)(PORT=1521)))   # 포트 : 1521
#192.168.0.84  : cmd창에서  ipconfig (ip주소)

# [ 참고 : 오라클 연동 시 한글 깨지는 현상 - encoding 처리 필요 ]
# 아래와 같이 언어를 한글지원이 가능한 'KO16MSWIN949'으로 변경 후  reconnection
import os
os.putenv('NLS_LANG', 'KOREAN_KOREA.KO16MSWIN949')

# merge
# - python에서의 RDBMS의 join 연산
# - equi-join만 가능(non-equi-join 불가)
# - outer-join 가능
# - 두개 DataFrame만 조인 가능

# pd.merge(left,                  # 조인할 첫 번째 대상
#          right,                 # 조인할 두 번째 대상
#          how = 'inner',         # inner join여부(inner, outer, left, right)
#          on = ,                 # 양측에 모두 존재하는 조인 컬럼명
#          left_on = ,            # 첫 번째 DataFrame에 있는 조인 컬럼명
#          right_on = ,           # 두 번째 DataFrame에 있는 조인 컬럼명
#          left_index = False,    # 첫 번째 index를 조인컬럼 설정 시
#          right_index = False)   # 두 번째 index를 조인컬럼 설정 시

# 예제) oracle에서 student테이블과 exam_01테이블을 각각 불러온 후 merge를 사용하여 조인
std = pd.read_sql('select * from student', con=con1)
std_1 = std.set_index('STUDNO')
std_1.index.names = [np.nan]
exam = pd.read_sql('select * from exam_01', con=con1)

pd.merge(std, exam, on = 'STUDNO')
pd.merge(std_1, exam, on = 'STUDNO')
pd.merge(std_1, exam, left_index=True, right_on = 'STUDNO')

# [ 참고 : index로 설정된 값을 다시 컬럼화 하는 경우]
std_1.reset_index()

# 예제) emp테이블을 불러온 후 각 직원의 상위관리자의 이름과 연봉 출력
# (단, 상위관리자가 없는 직원도 출력)
pd.read_sql('''select e1.*, e2.ename, e2.sal
                 from emp e1, emp e2 
                where e1.MGR = e2.EMPNO(+)''', con = con1)
emp = pd.read_sql('select * from emp', con = con1)

df10 = pd.merge(emp, emp, how = 'left', left_on = 'MGR' , right_on = 'EMPNO')[['ENAME_x','SAL_x','ENAME_y','SAL_y' ]]

# 상위관리자가 없는 인원을 본인의 이름으로 치환하라.
df10 = df10[['ENAME_x','ENAME_y','SAL_x','SAL_y']].fillna(method='ffill', axis=1)   # 컬럼순서를 바꾸고, fillna를 축방향으로 전달해준다.
df10[['ENAME_x','SAL_x','ENAME_y','SAL_y' ]]

# pivot, pivot_table : 테이블 재배치
# - tidy data로 부터 교차테이블 만들 경우 사용
# - pivot은 요약기능이 없으므로 데이터 요약이 필요할 경우 pivot_table 사용
pivot(index = ,
      columns = ,
      values = )
pivot_table(index = ,
            columns = ,
            values = ,
            aggfunc = 'mean')

# 예제) movie 데이터로부터 연령대별 성별 이용비율의 평균을 교차테이블 형식으로 출력
movie = pd.read_csv('movie_ex1.csv', engine='python')
movie.pivot_table(index='연령대', columns = '성별', values = '이용_비율(%)', aggfunc = 'count')   # 개수(aggfunc)
movie.pivot_table(index='연령대', columns = '성별', values = '이용_비율(%)', aggfunc = len)       # 개수(aggfunc)

# 예제) 성별 이용비율의 평균을 구하여라
movie.pivot_table(index = '성별', values = '이용_비율(%)', aggfunc = 'mean')
movie.pivot_table(columns = '성별', values = '이용_비율(%)', aggfunc = 'mean')
