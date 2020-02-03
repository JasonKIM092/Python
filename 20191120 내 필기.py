# [ 시각화 연습문제 ]
import pandas as pd
# movie_ex1.csv 파일을 읽고
movie = pd.read_csv('movie_ex1.csv', engine = 'python')

# 날짜 파싱
from datetime import datetime
datetime(2019,1,1)

datetime(movie['년'],movie['월'],movie['일'])   # 벡터연산 불가

# 1) map
f1 = lambda x,y,z : datetime(x,y,z)

movie['년'].map(f1, movie['월'],movie['일'])         # map 매서드 : 함수에 여러 인자 전달 제한. 불가.
list(map(f1, movie['년'],movie['월'],movie['일']))   # map 함수 : 함수에 여러 인자 전달 가능. 가능.

movie['date'] = list(map(f1, movie['년'],movie['월'],movie['일']))

# 2) apply : Series 전달 후 필요 데이터 색인 통해 분리
f2 = lambda x : datetime(x[0],x[1],x[2])
movie.apply(f2, axis = 1)


# 1) 일자별 총 이용비율 평균을 구하고 plot 도표로 출력
movie.pivot_table(index = '일', values = '이용_비율(%)', aggfunc = 'mean').plot()
import matplotlib.pyplot as plt
fig1, ax1 = plt.subplots(1,1)
plt.rc('font',family='Malgun Gothic')

# 필기 #
# 1) groupby
movie.groupby('일')['이용_비율(%)'].mean().plot()

# 2) resample
movie = movie.set_index('date')
movie['이용_비율(%)'].resample('D').mean().plot()

# 그래프 옵션 설정
plt.rc('font',family='Malgun Gothic')
plt.rc('figure',figsize=[10,10])
plt.rc('font',size=10)

plt.title('일자별 이용비율 현황(2018년 2월)', fontsize=7)

# [ 참고 : plt.rc로 전달할 수 있는 옵션 ]
plt.rcParams.keys()

# 2) 전일대비 증감률을 구하여라
movie2 = movie.pivot_table(index = '일', values = '이용_비율(%)', aggfunc = 'mean')
movie2.shift(1)
((movie2 - movie2.shift(1))/movie2.shift(1) * 100).fillna(0)

# 3) 평일과 주말(금,토,일)로 그룹을 나누어서 연령대별 이용비율의 평균을 막대그래프로 출력
from datetime import datetime
movie['요일'] = movie.apply(lambda x : str(x[0]) + '/' + str(x[1]) + '/' + str(x[2]), axis = 1).map(lambda x : datetime.strptime(x,'%Y/%m/%d').strftime('%A'))
import numpy as np
movie['구분'] = pd.Series(np.where(movie.loc[:,'요일'].isin(['Friday' or 'Saturday' or 'Sunday']),'주말','평일'))

movie.pivot_table(index='연령대', columns='구분', values='이용_비율(%)').plot(kind='bar')

# 필기 #
s3 = movie['date'].map(lambda x : x.strftime('%w')).replace(['1','2','3','4'],'평일').replace(['0','5','6'],'주말')
s3.drop_duplicates()

movie.pivot_table(index = s3, columns = '연령대', values='이용_비율(%)').plot(kind='bar')
plt.xticks(rotation=0)

# [ 참고 : 시각화 옵션 적용 범위 ]
# - plt : 현재 활성화 되어있는 figure 혹은 여러개인 경우는 마지막 subplot
# - plt.rc : 현 시점 이후 활성화되는 모든 figure에 적용
# - ax.set_ : 특정 subplot(이름을 갖고 있는 경우에 한해) 적용

# 4) 하나의 figure에 두개의 subplot을 생성한 후 남,여의 일별 이용비율 평균을 plot 도표로 출력
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,2,1)
ax2 = fig1.add_subplot(1,2,2)

total = movie.pivot_table(index = '일', columns = '성별', values = '이용_비율(%)')
ax1.plot(total['남'])
total['남'].plot(ax=ax1)

ax2.plot(total['여'])
total['여'].plot(ax=ax2)

plt.title('여')
ax1.set_title('남', fontsize = 8)
ax2.set_title('여', fontsize = 8)

ax1.set_ylabel('이용비율')

ax1.set_xticks(total.index)
ax2.set_xticks(total.index)

plt.xticks(color='red')       # 마지막 subplot(ax2)에만 반영
ax1.set_xticks(color='red')   # 전달 불가

ax1.tick_params?

ax1.tick_params(axis='x', labelcolor='red', rotation=30)   

# 기타 numpy 함수
# 1. C순서 F순서
# - 배열 생성, 평탄화 시 행 우선순위(C), 컬럼우선순위(F) 선택 가능
import numpy as np
a1 = np.arange(1,17).reshape(4,4)
a2 = np.arange(1,17).reshape(4,4,order='F')

# 2. 평탄화
# - 1차원 배열로 재배치
# - C,F 순서 전달 가능
a1.flatten()      # a1의 행부터 평탄화
a1.flatten('F')   # a1의 컬럼부터 평탄화

# 3. 결합
np.concatenate((a1,a2), axis=0)
np.concatenate((a1,a2), axis=1)
np.vstack((a1,a2))   # 세로로 결합(행 추가)
np.hstack((a1,a2))   # 가로로 결합(컬럼 추가)

# 4. 분리
a3 = np.vstack((a1,a2))
a3_1, a3_2, a3_3 = np.split(a3, [2,5])   # [2,5] : 위치값(행번호)

# 5. 반복
a1.repeat(3)   # 각 원소들을 횟수만큼 반복, 차원 축소 리턴
np.array([1,2,3]).repeat(3)
np.array([1,2,3]).repeat([2,3,4])

np.array([[1,2],[3,4]]).repeat(2, axis=0)
np.array([[1,2],[3,4]]).repeat(2, axis=1)

np.tile(np.array([[1,2],[3,4]]),   # 반복할 배열
        (2,3))                     # 반복해서 리턴할 shape. (행, 열)

# 6. 색인과 치환
a5 = np.array([1,2,3,4])
idx = [0,3]
a5.take(idx)     # a5에서 idx에 해당되는 범위 추출
a5.put(idx,10)   # a5에서 idx에 해당되는 원소를 10으로 변경, 원본 직접 수정
a5               # a5[0], a5[10] 수정된 것 확인

# 7. 브로드캐스팅(배열 연산)
a1 + a1[0]       # 4x4 + 1x4 배열 연산 가능
a1 + a1[:,0]     # 4x4 + 1x4로 연산 (행 반복)
a1 + a1[:,0:1]   # 4x4 + 4x1로 연산 (컬럼 반복)