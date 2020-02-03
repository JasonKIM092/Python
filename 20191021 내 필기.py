# eval
v1 = 'print(6)'
eval(v1)

v2 = input('수식을 입력하세요 : ')
eval(v2)


a1 = 11

if a1 > 10 :
    print('10보다 크다')  # 들여쓰기 맞춰주기!!!
    print('10보다 크다...')
# 다른 기호 없이 엔터 한칸을 뛰면 조건문 종료를 뜻한다.
print('프로그램 종료')


a1 = 11

if a1 > 10 :
    print('10보다 크다')  # 들여쓰기 맞춰주기!!!
print('10보다 크다...')   # 들여쓰기가 같지 않으면,
                          # if문 실행구문에 포함되지 않으므로 출력됨.
                          # 한칸의 엔터가 있다고 보지만,
                          # 현업에서는 쓰지 않는게 좋다.



#
v1 = int(input('점수를 입력하세요 : '))

if v1 >= 90 :
    print('A')
elif v1 >= 80 :
    print('B')
else :
    print('C')

print('프로그램 종료')




          

#
for i in 1:10 :   # 콜론이 두번이라 파싱 오류

for i in range(1,11) :
    print(i)

print('프로그램 종료')


#
for i in range(1,11,2) :   # by = 2씩 갭을 주는...
    print(i)

print('프로그램 종료')



# 범위를 직접 설정.
l1 = [1,2,5,10]

for i in l1 :
    print(i)

print('프로그램 종료')




# l1 + 1 출력(for문).
l1 = [1,2,5,10]

for i in l1 :
    print(i+1)   # 출력만 하고 객체에 담겨져 있지는 않다.

print('프로그램 종료')

# l1 + 1 출력(map).
l1 = [1,2,5,10]
list(ap(lambda x : x+1, l1))

# 리스트 형식으로 출력
l1 = [1,2,5,10]

l2 = []   # 빈 리스트 생성
for i in l1 :
    l2.append(i+1)

print(l2)
print('프로그램 종료')



# 연습문제
print('1. 입력한 수식 계산')
print('2. 두 수 사이의 합계')
ans = int(input('메뉴를 입력하세요 : '))

if ans == 1 :
    v1 = input('수식을 입력하세요 : ')
    print('%s 결과는 %.1f입니다.' % (v1, eval(v1)))
elif ans == 2 :
    no1 = int(input('첫 번째 수를 입력하세요 : '))
    no2 = int(input('두 번째 수를 입력하세요 : '))
    vsum = 0
    for i in range(no1, no2 + 1) :
        vsum = vsum + i
        
    print('%d+...+%d는 %d입니다.' % (no1, no2, vsum))
else :
    print('잘못된 입력입니다.')

print('프로그램 종료')

# 연습문제
no1 = int(input('첫 번째 숫자를 입력하세요 : '))
no2 = int(input('두 번째 숫자를 입력하세요 : '))
no3 = int(input('더할 숫자를 입력하세요 : '))

vsum = 0
for i in range(no1, no2 + 1, no3) :
    vsum = vsum + i
        
print('%d+%d+...+%d는 %d입니다.' % (no1, no1+no3, no2, vsum))





#
jumin = '9012311223344'
gender = '남자' if jumin[6] == '1' else '여자'

jumin = '9012313223344'
gender = '남자' if jumin[6] in ['1','3'] else '여자'
gender = '남자' if (jumin[6] == '1') or (jumin[6] == '3') else '여자'

jumin = ['9012311223344', '0012223456789']
f1 = lambda x : x[6] in ['1','3']
list(map(f1, jumin))

f1 = lambda x : (x[6] == '1') or (x[6] == '3')
list(map(f1, jumin))


#
jumin = ['8812111223928','8905042323343','90050612343432']
f1 = lambda x : '남자' if x[6] in ['1','3'] else '여자'
list(map(f1, jumin))


# 한 줄 출력
for i in l1 :
    print(i, end = ' ')

for i in l1 :
    print(i, end = ';')

#
for i in range(1,11) :
    print(i, end = ' ')
    if i == 5 :
	    print()   # 이렇게 쓰면 엔터가 자동으로 출력됨.

#
for i in range(1,11) :
    print('%2d' % i, end = ' ')
    if i == 5 :
	    print()

#
import random
random.randrange(0,10)     # R에서 sample과 동일
                           # == sample(0:9, size = 1)

#
for i in l1 :
    print(i)



#
>>> for j in range(0,2) :
	for i in range(0,5) :
		print(l1[j][i], end = ' ')

		
1 2 3 4 5 6 7 8 9 10

#
>>> for j in range(0,2) :
	for i in range(0,5) :
		print(l1[j][i], end = ' ')
		print()

		
1 
2 
3 
4 
5 
6 
7 
8 
9 
10

#
>>> for j in range(0,2) :
	for i in range(0,5) :
		print(l1[j][i], end = ' ')
	print()

	
1 2 3 4 5 
6 7 8 9 10 


# 이중(중첩) for문에서 내부 for문이 먼저 수행이 된다.
# 구구단
for j in range(1,10) :
    for i in range(2,10) :
        print('%dX %d= %2d' % (i,j,i*j), end = ' ')
    print()

#
l1 = [[1,2,3,4,5],[6,7,8,9,10]]

1 2 3 4  5
6 7 8 9 10


for j in range (0,2) : 
 for i in range(0,5) :
     print (l1[j][i], end = ' ')
