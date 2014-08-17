Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> n=1
>>> while n<=99
SyntaxError: invalid syntax
>>> L=[]
>>> n=1
>>> while n<=99:
	L.append(n)
	n=n+2

	
>>> L
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
>>> [L[0],L[1],L[2]]
['Michael', 'Sarah', 'Tracy']
>>> L[0],L[1],L[2]
('Michael', 'Sarah', 'Tracy')
>>> r=[]
>>> n=3
>>> for i in range(n):
	r.append(L[i])

	
>>> r
['Michael', 'Sarah', 'Tracy']
>>> time()

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    time()
NameError: name 'time' is not defined
>>> date()

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    date()
NameError: name 'date' is not defined
>>> import time
>>> t

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> time
<module 'time' (built-in)>
>>> time.localtime
<built-in function localtime>
>>> print time.t

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print time.t
AttributeError: 'module' object has no attribute 't'
>>> print time.time()
1408284707.68
>>> time.clock()
18.0296
>>> import datetime
>>> datetime.date()

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    datetime.date()
TypeError: Required argument 'year' (pos 1) not found
>>> datetime.date.day()

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    datetime.date.day()
TypeError: 'getset_descriptor' object is not callable
>>> datetime.date.day
<attribute 'day' of 'datetime.date' objects>
>>> import time
>>> print time.strftime("%H:%M:%S))
		    
SyntaxError: EOL while scanning string literal
>>> print time.strftime("%H:%M:%S)
		    
SyntaxError: EOL while scanning string literal
>>> print (time.strftime("%H:%M:%S"))
22:17:13
>>> import time
>>> print (time.strftime("%Y-%m-%d %H:%M:%S"))
2014-08-17 22:18:59
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

>>> L
['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
>>> L[:3]
['Michael', 'Sarah', 'Tracy']
>>> L=range(100)
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> L[0:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L[4-89]
15
>>> L[5:20]
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> L[-10]
90
>>> L[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> (1,23,34,45,56,3)[:4]
(1, 23, 34, 45)
>>> "dfghjkldsafgsfujksnmdgfjgws,m"[1:2]
'f'
>>> d={'a':1,'b':2,'c':3}
>>> for key in d:
	print key

	
a
c
b
>>> for value in d:
	print value

	
a
c
b
>>> for key in d:
	print d[key]

	
1
3
2
>>> for value d.itervalues:
	
SyntaxError: invalid syntax
>>> for value in d.itervalues:
	print value

	

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    for value in d.itervalues:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for value in d.values():
	print value

	
1
3
2
>>> for value in d.itervalues():
	print value

	
1
3
2
>>> for ch in 'ABCSDSA'
SyntaxError: invalid syntax
>>> for ch in 'ABCSDSA':
	print ch

	
A
B
C
S
D
S
A
>>> for ch in 'ABCSDSA'[0:5]:
	print ch

	
A
B
C
S
D
>>> for k, v in d.iteritems():
	print k,v

	
a 1
c 3
b 2
>>> for k, v in d.iteritems():
	print k---v

	

Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    print k---v
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> for k, v in d.iteritems():
	print(k+"----"+v)

	

Traceback (most recent call last):
  File "<pyshell#86>", line 2, in <module>
    print(k+"----"+v)
TypeError: cannot concatenate 'str' and 'int' objects
>>> print "a'+"b"
SyntaxError: EOL while scanning string literal
>>> print("a"+"b"
      )
ab
>>> for k, v in d.iteritems():
	print(str(k)+","+str(v))

	
a,1
c,3
b,2
>>> from collections import Iterable
>>> isinstance('abc',Iterable)
True
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> for(i=0;i<len(L),i++):
	
SyntaxError: invalid syntax
>>> isinstance(L,Iterable)
True
>>> for i in range(len(L)):
	printL[i]

	

Traceback (most recent call last):
  File "<pyshell#100>", line 2, in <module>
    printL[i]
NameError: name 'printL' is not defined
>>> for i in range(len(L)):
	print(L[i])

	
0
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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> range(1:3)
SyntaxError: invalid syntax
>>> range(5,99,3)
[5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
>>> L=range(5,99,4)
>>> for i in range(len(L)):
	print L[i]

	
5
9
13
17
21
25
29
33
37
41
45
49
53
57
61
65
69
73
77
81
85
89
93
97
>>> for i,value in enumerate(['A','B','V']):
	print i,value

	
0 A
1 B
2 V
>>> for x,y in[(1,1),(2,2),(3,3)]:
	print x,y

	
1 1
2 2
3 3
>>> for x,y in[(1,1),(2,2),(3,3)]:
	print(str(x)+"------->"+str(y))

	
1------->1
2------->2
3------->3
>>> L={}
>>> l=[]
>>> for i in range(1,10):
	L.append(i*i)

	

Traceback (most recent call last):
  File "<pyshell#123>", line 2, in <module>
    L.append(i*i)
AttributeError: 'dict' object has no attribute 'append'
>>> L=[]
>>> for in range(1,10):
	
SyntaxError: invalid syntax
>>> for i in range(1,10):
	L.append(i*i)

	
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x*x for x in range(1,10)]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> L=[x*x for x in range(1,10)]
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x*x for x in range(1,10) if x%2==0]
[4, 16, 36, 64]
>>> [m+n for m in "ABC" n in "abc"]
SyntaxError: invalid syntax
>>> [ m+n for m in "ABC" for n in "abc"]
['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']
>>> 'A'-'a'

Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    'A'-'a'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> int('A')

Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    int('A')
ValueError: invalid literal for int() with base 10: 'A'
>>> ch(97)

Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    ch(97)
TypeError: 'str' object is not callable
>>> [m+n for m in "ABC" for n in "abc" if ord(n)-ord(m)==ord('a')-ord('A')]
['Aa', 'Bb', 'Cc']
>>> import os
>>> [d for d in os.listdir(.)]
SyntaxError: invalid syntax
>>> [d for d in os.listdir('.')]
['workspace', '.bash_history', '.cache', '.Xauthority', '\xe8\xa7\x86\xe9\xa2\x91', 'hello.exe', '.goutputstream-7G30GX', '.goutputstream-LM2GHX', '.config', '\xe6\x96\x87\xe6\xa1\xa3', 'test', 'new_feature.cpp', '.macromedia', '.goutputstream-LA8VGX', '\xe4\xb8\x8b\xe8\xbd\xbd', '\xe5\x85\xac\xe5\x85\xb1\xe7\x9a\x84', 'gitRepository', '.dbus', '.dmrc', '.gksu.lock', 'hello.cpp', '.bashrc', '\xe9\x9f\xb3\xe4\xb9\x90', '.gnome2', 'clang_complete', 'ebook', 'examples.desktop', 'Android', '\xe6\xa1\x8c\xe9\x9d\xa2', '.xsession-errors.old', '.eclipse', 'test.cpp', 'Hello.cpp', '.pki', '.goutputstream-G8N3GX', '.gitconfig', '.swp', '.compiz', '.pulse-cookie', '.bash_logout', '.goutputstream-QPD3GX', '.gnome2_private', '.vim', '.goutputstream-TBYLGX', '.goutputstream-NULAHX', '\xe6\xa8\xa1\xe6\x9d\xbf', 'temp', '.profile', '.gstreamer-0.10', '.swt', '.gtk-bookmarks', '.kde', '.ssh', '.apport-ignore.xml', '.xinputrc', '.ICEauthority', '.wicd', '.mozilla', '.idlerc', 'clang_complete.vmb', '\xe5\x9b\xbe\xe7\x89\x87', '.gconf', '.goutputstream-2VVEGX', '.local', '.pulse', '.subversion', '.pam_environment', '.xsession-errors', '.adobe', '.repopickle_.gitconfig', 'libcxx', '.goutputstream-MYBEHX', '.goutputstream-ZRTUHX', '.codeblocks', 'hello', '.sunpinyin', '.repoconfig', 'myfirst.exe', '.viminfo', '.thumbnails', '.gvfs', '.mission-control', '.compiz-1', 'test.exe', '.hedgewars', '.fontconfig', 'Hello.h', '.face']
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k ,v in d.itervalues():
	print k "=" v
	
SyntaxError: invalid syntax
>>> for k ,v in d.itervalues():
	print k,"=",v

	

Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    for k ,v in d.itervalues():
ValueError: need more than 1 value to unpack
>>> for k ,v in d.itervalues():
	print k ,"=", v

	

Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    for k ,v in d.itervalues():
ValueError: need more than 1 value to unpack
>>> for k ,v in d.itervalues():
	print k, "=" ,v

	

Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    for k ,v in d.itervalues():
ValueError: need more than 1 value to unpack
>>> for k ,v in d.itervalues():
	print k, "=", v

	

Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    for k ,v in d.itervalues():
ValueError: need more than 1 value to unpack
>>> for k, v in d.iteritems():
	print k,'=',v

	
y = B
x = A
z = C
>>> [k+'='+v for k,v in d]

Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    [k+'='+v for k,v in d]
ValueError: need more than 1 value to unpack
>>> [k+'='+v for k,v in d.values()]

Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    [k+'='+v for k,v in d.values()]
ValueError: need more than 1 value to unpack
>>> [k+ '=' +v for k,v in d.values()]

Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    [k+ '=' +v for k,v in d.values()]
ValueError: need more than 1 value to unpack
>>> [k+'='+v for k, v in d.values()]

Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    [k+'='+v for k, v in d.values()]
ValueError: need more than 1 value to unpack
>>> [k + '=' + v for k, v in d.values()]

Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    [k + '=' + v for k, v in d.values()]
ValueError: need more than 1 value to unpack
>>>  [k + '=' + v for k, v in d.iteritems()]
 
  File "<pyshell#164>", line 1
    [k + '=' + v for k, v in d.iteritems()]
    ^
IndentationError: unexpected indent
>>> [k + '=' + v for k, v in d.iteritems()]
['y=B', 'x=A', 'z=C']
>>> [k + '=' + v for k, v in d.value()]

Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    [k + '=' + v for k, v in d.value()]
AttributeError: 'dict' object has no attribute 'value'
>>>  [k + '=' + v for k, v in d.values()]
 
  File "<pyshell#167>", line 1
    [k + '=' + v for k, v in d.values()]
    ^
IndentationError: unexpected indent
>>> [k + '=' + v for k, v in d.values()]

Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    [k + '=' + v for k, v in d.values()]
ValueError: need more than 1 value to unpack
>>> [k + '=' + v for k, v in d.iteritems()]
['y=B', 'x=A', 'z=C']
>>> [k + '=' + v for k, v in d.values()]

Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    [k + '=' + v for k, v in d.values()]
ValueError: need more than 1 value to unpack
>>> [k+'='+v for k,v in d.itervalues()]

Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    [k+'='+v for k,v in d.itervalues()]
ValueError: need more than 1 value to unpack
>>> [k + '=' + v for k, v in d.iteritems()]
['y=B', 'x=A', 'z=C']
>>> [k + '=' + v for k, v in d.values()]

Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    [k + '=' + v for k, v in d.values()]
ValueError: need more than 1 value to unpack
>>> [k + '=' + v for k,v in d.iteritems()]
['y=B', 'x=A', 'z=C']
>>> [k + '=' + v for k, v in d.iteritems()]
['y=B', 'x=A', 'z=C']
>>> [k + '=' +v for k,v in d.iteritems()]
['y=B', 'x=A', 'z=C']
>>> [k+'='+v for k,v in d.iteritems()]
['y=B', 'x=A', 'z=C']
>>> [k+'='+v for k,v in d.itervalues()]

Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    [k+'='+v for k,v in d.itervalues()]
ValueError: need more than 1 value to unpack
>>> [k+'='+v for k,v in d.iteritems()]
['y=B', 'x=A', 'z=C']
>>>  L = ['Hello', 'World', 'IBM', 'Apple']
 
  File "<pyshell#180>", line 1
    L = ['Hello', 'World', 'IBM', 'Apple']
    ^
IndentationError: unexpected indent
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [ s.lower for s in L if isinstance(s,str)]
[<built-in method lower of str object at 0x7f1b8aa92a50>, <built-in method lower of str object at 0x7f1b8aa923c0>, <built-in method lower of str object at 0x7f1b8aa92090>]
>>> L
['Hello', 'World', 18, 'Apple', None]
>>> [ s.lower() for s in L if isinstance(s,str)]
['hello', 'world', 'apple']
>>> g=(x*x for x in range(10)]
SyntaxError: invalid syntax
>>> g=(x*x for x in range(10))
>>> g
<generator object <genexpr> at 0x7f1b8aa8bc30>
>>> g.next()
0
>>> g.next()
1
>>> g.next()
4
>>> g.next()
9
>>> g.next()
16
>>> g.next()
25
>>> g.next()
36
>>> g.next()
49
>>> g.next()
64
>>> g.next()
81
>>> g.next()

Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    g.next()
StopIteration
>>> g.next()

Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    g.next()
StopIteration
>>> g.next()

Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    g.next()
StopIteration
>>> f=(x*x for x in range(10))
>>> for n in f:
	print n

	
0
1
4
9
16
25
36
49
64
81
>>> for n in f:
	print n

	
>>> 
>>> f=(x*x for x in range(10))
>>> for n in f:
	print ("2%",%n)
	
SyntaxError: invalid syntax
>>> 
>>> for n in f:
	print ("2d%",n)

	
('2d%', 0)
('2d%', 1)
('2d%', 4)
('2d%', 9)
('2d%', 16)
('2d%', 25)
('2d%', 36)
('2d%', 49)
('2d%', 64)
('2d%', 81)
>>> for n in f:
	print "2d%" ,%n
	
SyntaxError: invalid syntax
>>> 
>>> def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

        
>>> fab(5)
1
1
2
3
5
>>> def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

        
>>> fab(10)
<generator object fab at 0x7f1b8a8ed280>
>>> n=fab(10)
>>> n.next()
1
>>> n.next()
1
>>> n.next()
2
>>> n.next()
3
>>> n.next()
5
>>> n.next()
8
>>> n.next()
13
>>> 
>>> n.next()
21
>>> n.next()
34
>>> n.next()
55
>>> n.next()
KeyboardInterrupt
>>> 
>>> n.next()

Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    n.next()
StopIteration
>>> n.next()

Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    n.next()
StopIteration
>>> n.next()

Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    n.next()
StopIteration
>>> def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 2
	print 'step 3'
	yield 3

	
>>> o=odd()
>>> for n in o:
	n.next()

	
step 1

Traceback (most recent call last):
  File "<pyshell#251>", line 2, in <module>
    n.next()
AttributeError: 'int' object has no attribute 'next'
>>> o.next()
step 2
2
>>> o.next()
step 3
3
>>> y=odd()
>>> for n in y:
	n.next()

	
step 1

Traceback (most recent call last):
  File "<pyshell#257>", line 2, in <module>
    n.next()
AttributeError: 'int' object has no attribute 'next'
>>> y.next()
step 2
2
>>> for o in odd():
	o.next()

	
step 1

Traceback (most recent call last):
  File "<pyshell#261>", line 2, in <module>
    o.next()
AttributeError: 'int' object has no attribute 'next'
>>> for i in o:
	print i

	

Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    for i in o:
TypeError: 'int' object is not iterable
>>> o=odd()
>>> for i in o:
	print i

	
step 1
1
step 2
2
step 3
3
>>> 
