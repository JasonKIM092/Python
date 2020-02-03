import pandas as pd
import numpy as np

# 1. 중복 여부 확인
s1 = pd.Series([1,1,2,2,3,3])
s1.duplicated()

# 2. 중복 제거하기
s1[s1.duplicated()]
s1.drop_duplicates()

# 3. DataFrame일 경우 중복 제거(key선택 가능)
df1 = pd.DataFrame({'col1':[1,1,2,2,3,3], 'col2':['a','a','a','b','b','b']})
df1.drop_duplicates(['col1'])          # select distinct col1과 같은 기능
df1.drop_duplicates(['col1','col2'])   # select distinct col1, col2와 같은 기능

# [ 참고 : array의 중복 제거 ]
a1 = np.array([1,1,2,2,3,3])
np.unique(a1)


# 문자열의 대소 치환 매서드
'a'.upper()   # 가능
['a','b'].upper()   # 불가, list에는 upper 매서드 적용 불가
list(map(lambda x : x.upper(), ['a','b']))   # list 출력

pd.Series(['a','b']).upper()   # 불가, Series에는 upper 매서드 적용 불가
pd.Series(['a','b']).map(lambda x : x.upper())   # Series 출력
pd.Series(['a','b']).str.upper()   # str : pandas에서 제공하는 벡터화가 내장된 문자열 매서드의 묶음

# [ 참고 ]
# str(1) : 형변환함수
# int, float, str : 형변환함수
# .str : 문자열 매서드 묶음. 메서드형식

# 벡터화가 내장된 replace 매서드
s1 = pd.Series([1,2,3,4])

s1.replace(1,100)                   # 하나의 값 치환(1:1 치환)
s1.replace([1,2,3],100)             # 여러 값을 하나로 치환(n:1 치환)
s1.replace([1,2,3],[100,200,300])   # 여러 값을 각각 치환, 리스트로 전달(n:n 치환)
s1.replace({1:100, 2:200, 3:300})     # 여러 값을 각각 치환, 딕셔녀리로 전달(n:n 치환)

# cf) NA 치환 및 NA로의 치환 가능
s1.replace({1:100, 2:200, 3:np.nan})
s2 = pd.Series([1,2,np.nan,4])
s2.replace({1:100, 2:200, 3:300})

# 날짜 형 변환 함수
# 1. 문자 -> 날짜(문자열의 날짜로의 파싱)
strptime   # p : parsing(파싱)
from datetime import datetime
'2019-11-11'.strptime('%Y-%m-%d')   # 문자열 적용 불가(datetime 모듈 호출 필요)

d1 = datetime.strptime('2019-11-11','%Y-%m-%d')

# 2. 날짜 -> 문자(날짜의 형식 변경)
strftime   # f : format
d1.strftime('%A')

# [ 연습 문제 ]
# 1. movie_ex1.csv 파일을 읽고
df1 = pd.read_csv('movie_ex1.csv', engine = 'python')
'2018'+'2'+'1'
datetime.strptime('2018'+'/'+'2'+'/'+'1', '%Y/%m/%d')

'2018'+'%02d' % 2 + '%02d' % 1
datetime.strptime('2018'+'%02d' % 2 + '%02d' % 1, '%Y%m%d')

df1['날짜'] = df1.loc[:,'년'].map(str) + '-' + df1.loc[:,'월'].map(str) + '-' + df1.loc[:,'일'].map(str)

# 년월일 결합
# 1. map 함수 사용(사이즈가 같은 1차원 객체를 동시 전달 가능)
list(map(lambda x,y : x.split(y)[0], ['a;b;c','AA;BB;CC'], [';',';']))

f1 = lambda x,y,z : str(x) + '/' + str(y) + '/' + str(z)
list(map(f1, df1['년'],df1['월'],df1['일']))

# 2. apply 사용
f2 = lambda x : str(x[0]) + '/' + str(x[1]) + '/' + str(x[2])
df1['date'] = df1.apply(f2, axis = 1)

# 요일 구하기
datetime.strptime(df1['date'], '%Y/%m/%d')   # 벡터연산 불가

f3 =lambda x : datetime.strptime(x, '%Y/%m/%d').strftime('%A')
df1['day'] = df1['date'].map(f3).str.upper()

# 1) 요일별 연령대의 이용비율의 평균을 교차테이블 형식으로 출력
# (단, 요일과 연령대는 정렬된 상태)
df1['요일'] = df1.loc[:,'날짜'].map(lambda x : datetime.strptime(x,'%Y-%m-%d')).map(lambda x : x.strftime('%A'))

df100 = df1.pivot_table(index = '요일', columns = '연령대', values = '이용_비율(%)', aggfunc = 'mean')

df1.pivot_table(index = 'day', columns = '연령대', values = '이용_비율(%)').iloc[[1,5,6,4,0,2,3],:]   # 사용자 지정 정렬
# sort_index : 가나다, ABC 순으로 정렬됨.

# 2) 요일별 성별 이용비율의 비율 출력
df1.pivot_table(index = '요일', columns = '성별', values = '이용_비율(%)', aggfunc = 'mean')


f4 = lambda x : round(x/x.sum() * 100, 2)
df1.pivot_table(index = 'day', columns = '성별', values = '이용_비율(%)').apply(f4, 1).iloc[[1,5,6,4,0,2,3],:]   # 사용자 지정 정렬


# index. column 변경
df_1 = pd.DataFrame(np.arange(1,10).reshape(3,3),
                 index=['a','b','c'],
                 columns=['col1','col2','col3'])

# 예제) df_1의 인덱스와 컬럼을 대문자로 치환
df_1.index.str.upper()
df_1.columns.str.upper()

# 예제) df_1의 col2를 COLUMN2로 변경(일부 치환 형식)
a1 = df_1.columns.values
a1[1] = 'COLUMN2'
df_1.columns = a1

# 예제) df_1의 col3를 COLUMN3로 변경(rename 매서드)
df_1.rename(columns={'col3':'COLUMN3'})

# rename 매서드
# - index와 column의 일부 수정 가능
# - map(dictionary) 형식과 비슷
# - index와 column 인자에 치환 대상을 딕셔너리로 전달

# 벡터화 내장된 문자열 함수(str. 메서드명으로 호출, Series에만 전달 가능, DataFrame에는 전달 불가)
# 'str.'으로 호출해야 벡터화 기능 사용 가능
# 1. upper, lower, title : 대소 치환
s1 = pd.Series(['aA','bB','cC'])
df1 = pd.DataFrame(s1)
s1.upper()        # 불가, 문자열 매서드 호출
s1.str.upper()    # 가능, str 모듈 내 문자열 매서드 호출
s1.str.lower()
s1.str.title()    # 카멜표기법(첫 글자만 대문자)
df1.str.upper()   # 'DataFrame' object has no attribute 'str'

# 2. startwith, endswith, contains : 패턴 포함 여부 확인
s1.startswith('a')       # 불가
s1.str.startswith('a')   # 각 값이 'a'로 시작하는지 여부 확인
s1.str.endswith('a')     # 각 값이 'a'로 끝나는지 여부 확인
s1.str.contains('a')     # 각 값이 'a'를 포함하는지(위치에 상관 없이) 여부 확인

# 3. count, len : 개수 반환
s1.str.count('a')   # 각 원소에 'a'가 포함된 횟수 출력
s1.str.len()        # 각 원소의 전체 길이

# 4. cat, join : 문자열 결합
s1.str.cat(sep=';')   # 각 원소를 분리구분기호와 함께 하나의 문자열로 결합
s1.str.join(';')      # 각 원소의 문자열 끼리를 분리구분기호와 함께 각각 하나의 문자열로 결합

# 5. str, get, slice : 색인
s2 = pd.Series(['abcde','ABCDE'])
s2.str[0]                               # 각 원소의 문자열 색인
s2.str.get(0)                           # 각 원소의 positional 추출
s2.str.slice(start=0, stop=1, step=1)   # 각 원소별 문자열 추출(substr 기능)
s2.map(lambda x : x[0])

# 6. strip, lstrip, rstrip : 공백과 문자열 제거
s1.str.lstrip('a')
s1.str.rstrip('A')
s1.str.strip('c')

# 7. pad : 공백, 문자열 삽입
s1.str.pad(width = 5, side = 'left', fillchar='-')
s1.str.pad?

# 8. split : 문자열 분리
s3 = pd.Series(['a;b;c','A;B;C'])
s3.str.split(';')          # 각 원소를 분리구분 기호로 분리한 후 리스트로 출력
s3.str.split(';').str[0] 
s3.str.split(';').str.get(0)

# 9. find : 문자열 위치
s3.str.find(';')

# 10. replace, translate : 치환
# replace
s1 = pd.Series(['abcde','cdefg'])
s1.replace('c','C')       # Pandas replace는 값 치환만 가능, 패턴치환 불가.
s1.replace('abcde','?')   # Pandas replace는 값 치환만 가능, 패턴치환 불가. 값 치환.

s1.str.replace('c','C')   # 벡터화 내장된 문자열 replace 매서드
# 천단위 구분 기호를 치환할때, 해당 .str 매서드는 Series단위 즉, 컬럼단위로만 치환이 가능하므로
# DataFrame에서는 전체 치환을 원할 경우, applymap이 더 좋을때도 있다.

# translate
dir(str)
s1.str.translate(table)   # table은 변경할 문자열의 매칭 테이블을 의미
# 1) 딕셔너리로 전달
s1.str.translate({ord('c') : 'C', ord('d') : 'D'})   # translate는 각 문자열 유니코드를 전달해야 하는데, 이걸 대체해주는 함수가 ord()이다.

# 2) str.maketrans로 테이블 생성 후 전달
table1 = str.maketrans('cd','CD')
s1.str.translate(table1)

# 3) 삭제 처리 : 치환 값에 None
s1.str.translate({ord('c') : None, ord('d') : None})    # maketrans는 1:1매칭이라 무조건 글자수를 맞춰야한다. None전달 불가.
s1.str.translate({ord(i) : None for i in 'cdefggfh'})   # [None for i in [1,2,3]]

# [ 연습 문제 ]
# professor.csv 파일을 읽고
prof = pd.read_csv('professor.csv', engine='python')

# 1) ID의 두번째 값이 a인 직원 출력
prof.loc[prof.ID.str.find('a') == 1,:]

# 2) email-id 출력
prof.EMAIL.str.split('@').str[0]

# 3) 홈페이지 주소 출력, 홈페이지 주소가 있으면 그래도, 없으면 아래와 같이
# http://www.kic-campus.com/email-id
import numpy as np
np.where(prof.HPAGE.isnull(), 'http://www.kic-campus.com/'+ prof.EMAIL.str.split('@').str[0], prof.HPAGE)

prof.EMAIL.str.split('@').str[0].map(lambda x : 'http://www.kic-campus.com/'+ x)
np.where(prof.HPAGE.isnull(), prof.EMAIL.str.split('@').str[0].map(lambda x : 'http://www.kic-campus.com/'+ x), prof.HPAGE)
prof.HPAGE.combine_first(prof.EMAIL.str.split('@').str[0].map(lambda x : 'http://www.kic-campus.com/'+ x))

# 4) 입사년도 출력
prof.HIREDATE.str[:4]
prof.HIREDATE.str.split('/').str[0]
