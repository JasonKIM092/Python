

# 정규식 패턴
import re
txt1 = 'asd asd@naver.com  123x  d  !  ced@yahoo.co.kr'
pattern1 = re.compile('.+@.+\..+', flags = re.IGNORECASE)
pattern2 = re.compile('[a-z0-9]+@[a-z]+\.[a-z]{2,4}', flags = re.IGNORECASE)   # 띄어쓰기는 한개의 공백으로 파싱하므로 띄어쓰기는 신중히 할 것.
pattern3 = re.compile('[a-z0-9]+@[a-z]+\.[a-z.]{2,5}', flags = re.IGNORECASE)

# 패턴.findall(text)
pattern1.findall(txt1)
pattern2.findall(txt1)
pattern3.findall(txt1)

# 연습문제) 다음의 텍스트에서 '문자열+숫자' 패턴 추출
txt2 = '''a a1 . +12 
abc+123 ax1 df Ax+000'''

pattern4 = re.compile('[a-z]+\+[0-9]+', flags=re.IGNORECASE)
pattern4.findall(txt2)

# 정규식 표현식의 그룹핑 기능
# : 일단 정규식 패턴에 일치하는 문자열 추출 후 해당 문자열에서의 그룹을 생성하여
# 각 그룹을 분리하여 출력하고자 할 경우 사용 => ()

# 예제) 다음의 텍스트에서 이메일 아이디와 엔진주소를 각각 출력
txt3 = 'a ab@naver.com 1 3a kd3@daum.netad123'
pattern5 = re.compile('([a-z0-9]+)@([a-z]+\.[a-z]{3,3})', flags=re.IGNORECASE)   # 주의! ID 자리에 +까지 포함해서 ()그룹핑할 것!! @를 기준으로 앞뒤!
txt4 = pattern5.findall(txt3)

import pandas as pd
v_id = pd.Series(txt4).str[0]   # txt4 출력결과가 list이므로 Series로 만들어 준 후 .str 매서드 사용!
v_addr = pd.Series(txt4).str[1]

pd.DataFrame({'email_id':v_id, 'address':v_addr})


# [ 연습 문제 ]
# shoppingmall.txt 파일을 읽고 쇼핑몰 웹 주소만 출력(총 25개)
import numpy as np
txt5 = np.loadtxt('shoppingmall.txt', dtype='str', delimiter='\n')
txt5 = str(txt5)
import re
pattern6 = re.compile('[a-z://]+[a-z0-9.-]+\.[a-z0-9./]{2,15}', flags=re.IGNORECASE)
t1=pattern6.findall(txt5)
len(t1)
dir(np)
dir(pd)
np.loadtxt?

# 데이터 불러오기
c1 = open('shoppingmall.txt')
list1 = c1.readlines()
c1.close()
list1

text1 = pd.Series(list1).str.cat(sep='')
patt1 = re.compile('http://[a-z0-9./_-]+',flags=re.IGNORECASE)   # - 기호는 범위의 의미가 있어서 문자로 전달시 맨 앞이나, 맨 뒤에 보낸다.
patt1.findall(text1)
