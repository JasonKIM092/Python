>>> c1 = open('test1.txt','r')
>>> s1 = c1.readline()
>>> 
>>> s1
'1 2 3 4\n'
>>> s1 = c1.readline()
>>> s1
'5 6 7 8\n'
>>> s1 = c1.readline()
>>> s1
''
>>> c1 = open('test1.txt','r')
>>> s1 = c1.readlines()
>>> s1
['1 2 3 4\n', '5 6 7 8\n']
>>> v1='1\t2'
>>> v1
'1\t2'
>>> print(v1)
1	2
>>> l1=[]

>>> c1 = open('test1.txt','r')
>>> s1 = c1.readlines()
>>> s1
['1;2;3;4\n', '5;6;7']
>>> l1=[]

>>> for i in s1 :
	l1.append(i.strip().split(';'))

	
>>> l1
[['1', '2', '3', '4'], ['5', '6', '7']]



>>> l1 = [1,2,3,4]
>>> c1 = open('test5.txt','w')
>>> c1.writelines()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c1.writelines()
TypeError: writelines() takes exactly one argument (0 given)
>>> c1.writelines(l1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c1.writelines(l1)
TypeError: write() argument must be str, not int
>>> 
>>> vstr=''
>>> sep=' '
>>> for i in l1 :
	vstr = vstr + str(i) + sep

	
>>> vstr
'1 2 3 4 '
>>> c1.writelines(vstr)
>>> c1.close()


