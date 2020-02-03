#[ 파이썬 시각화 ]
# 파이썬 시각화를 위해서는 pylab 모드를 활성화 시켜야 함
1) ipython
- ipython 실행 시 : ipython --pylab
- ipython 실행 후 : %matplotlib qt
2) 기타 툴은 보통 pylab 모드 활성화 되어 있음

import matplotlib.pyplot as plt

# 1. figure 및 sublot 생성
# - figure : 그래프 그려질 창
# - subplot : figure 내에 실제 그래프가 그려질 도화지 같은 공간

# 1) figure 생성 후 subplot 생성 하는 방법
fig = plt.figure()   # figure 생성 후 figure의 옵션 설정을 위해서는 이름 부여 필요
ax1 = fig.add_subplot(1,   # subplot이 그려질 행의 수
                      2,   # subplot이 그려질 컬럼의 수
                      1)   # 각 subplot의 이름(위치)
ax2 = fig.add_subplot(1,2,2)   # subplot의 이름을 부여해야 그래프 그릴 때 subplot 지정 가능

import pandas as pd
s1 = pd.Series([1,2,3,4])
ax1.plot(s1)
ax2.plot(s1,'r--')

# 2) figure와 subplot 동시 생성 하는 방법
fig2, ax2 = plt.subplots(1,2)   # ax2[0], ax2[1] 통해 각 subplot 접근 가능
fig2, ax2 = plt.subplots(2,2)   # ax2[0,0], ax2[0,1], ... 통해 각 subplot 접근 가능

# 3) 자동 지정
# 3-1) Series의 호출
s1.plot()

# 3-2) DataFrame의 호출
# - 각 컬럼별 plot도표를 하나의 subplot에 표현
# - 각 컬럼 이름은 자동으로 범례로 전달
df1 = pd.DataFrame({'a':[1,2,3,4], 'b':[0,9,3,4], 'c':[3,5,10,11]})
df1.plot()

df2 = pd.DataFrame({'a':[1,2,3,4], 'b':[0,9,3,4], 'c':[3,5,10,11]})
df2.index.name = 'x-axis'
df2.columns.name = 'y-axis'

df2.plot()

# [ 참고 : spyder에서 figure를 윈도우 창에 띄우는 방법 ]
# Tools > Preference > IPython console > Graphics > Graphics backend에서
# Backend를 Automatic으로 변경 후 spyder restart(반드시 restart 필요)

# 2. plot 그리기
import numpy as np
fig1, ax1 = plt.subplots(2,2)
s1 = np.random.randn(30)
ax1[0,0].plot(s1)   # 축 지정 시 해당 subplot에 그래프 출력

pd.Series(s1).plot()   # 축 지정 안할 경우 마지막 생성된 subplot에 자동 출력
                       # 생성된 것이 없을 경우 figure와 subplot 자동 생성
                       
# [ 연습 문제 ]
# cctv.csv를 불러오고 각 년도별 검거율 증가추이를 각 구별로 비교할 수 있도록 plot 도표 그리기
cctv = pd.read_csv('cctv.csv', engine='python')
cctv1 = cctv.sort_values(by='구').set_index(['구','년도'])['검거'].unstack()
cctv1.apply(lambda x : round(x/x.sum() * 100,2), axis=1).plot()

cctv['rate'] = cctv['검거'] / cctv['발생'] * 100
cctv2 = cctv.pivot_table(index='년도', columns='구', values='rate')
cctv2.plot()
cctv2.plot(title = '구별 검거율 변화 추이2',
           xticks=cctv2.index,
           ylim=[0,130],
           rot=30,
           fontsize=8)
                       
# 3. plot 옵션 변경
plt.rc('font',family='Malgun Gothic')   # 한글깨짐 현상, 폰트 변경

# 1) x,y축 이름 변경
plt.xlabel('발생년도')
plt.ylabel('검거율')

# 2) 제목 변경
plt.title('구별 검거율 변화 추이')

# 3) x축, y축 범위 변경
plt.xlim
plt.ylim([0,120])

# 4) x축, y축 눈금 변경
# - x축 눈금은 index값이 자동으로 설정
x1 = cctv2.index
plt.xticks(x1)
plt.yticks

# 5) legend 설정
plt.legend(fontsize = 6, 
           loc='upper right', 
           title = '구이름'   # columns.name 설정 시 자동 반영
           )
plt.legend?

# 4. barplot 그리기
df1 = pd.DataFrame({'Apple' : [30,40,34], 'Banana' : [38,43,23], 'Mango' : [12,14,20]},
                    index = [2007,2008,2009])

df1.plot(kind='bar', stacked=True)
df1.plot(kind='bar')
plt.xticks(rotation=0)

# [ 연습 문제 ]
# kimchi_test.csv 파일을 읽고, 각 월별로 김치의 판매량을 비교할 수 있도록 막대그래프로 표현
kimchi = pd.read_csv('kimchi_test.csv', engine='python')
kimchi2 = kimchi.pivot_table(index = '판매월', columns = '제품', values = '수량', aggfunc = 'sum') 
kimchi2.plot(kind='bar')
plt.xticks(rotation=0)
plt.legend(fontsize = 7, loc='upper right', title = '제품명')

kimchi2 = kimchi.groupby(['판매월','제품'])['수량'].sum().unstack()
kimchi2.plot(kind='bar')
plt.ylim([0,250000])
plt.ylabel('판매량')
plt.xticks(rotation=0)
plt.title('월별 김치 판매량 비교')

# 5. hist 그리기
cctv['CCTV수'].hist(bins = 10)   # 정수 또는 리스트

cctv['CCTV수'].hist(bins = [0,100,200,500,2000])   # 정수 또는 리스트

cctv['CCTV수'].plot(kind='kde')
