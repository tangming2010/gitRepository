Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	return x+y

>>> reduce(add,[1,2,3,4,5,6])
21
>>> def conn(x,y):
	x*10+y

	
>>> reduce(conn,[1,2,3,4,5,6,7,8])

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    reduce(conn,[1,2,3,4,5,6,7,8])
  File "<pyshell#6>", line 2, in conn
    x*10+y
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> def conn(x,y):
	return x*10+y

>>> reduce(conn,[1,2,3,4,5,6,7,8])
12345678
>>> def fn(x,y):
	return x*10+y

>>> reduce(fn,[1,3,5,7,9])
13579
>>> def str2int(s):
	
KeyboardInterrupt
>>> def fn(x,y):
	return x*10+y

>>> reduce(fn,map(int,'13579'))
13579
>>> def str2int(s):
	def fn(x,y):
		return x*10+y
	return reduce(fn,map(int,s))

>>> str2int('1242335')
1242335
>>> def str2int(s):
	return reduce(lambda x,y:x*10+y,map(int,s))

>>> str2int('34567890')
34567890
>>> sorted([23,3,12,124,432,3,44])
[3, 3, 12, 23, 44, 124, 432]
>>> def reversed_cmp(x,y):
	if x>y:
		return -1
	if x<y:
		return 1
	return 0

>>> sorted([23,34,434,14,345,3],reversed_cmp)
[434, 345, 34, 23, 14, 3]
>>> sorted(['about', 'bob', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
>>> def cmp_ignore_case(s1,s2):
	u1=s1.upper()
	u2=s2.upper()
	if u1<u2:
		return -1
	if u1>u2:
		return 1
	return 0

>>>  sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)
 
  File "<pyshell#50>", line 1
    sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)
    ^
IndentationError: unexpected indent
>>> sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)
['about', 'bob', 'Credit', 'Zoo']
>>> def calc_sum(*args):
	ax=0
	for n in args:
		ax=ax+n
	return ax

>>> def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum

>>> f=lazy_sum(1,2,3,4,5,6)
>>> f()
21
>>> f
<function sum at 0x7f625c0e0578>
>>> f1=lazy_sum
KeyboardInterrupt
>>> 
>>> map(lambda x:x*x,[1,2,3,4,5,6])
[1, 4, 9, 16, 25, 36]
>>> f=lambda x:x*x
>>> f
<function <lambda> at 0x7f625c0e05f0>
>>> f(0)
0
>>> f(23)
529
>>> ef build9x,y):
	
SyntaxError: invalid syntax
>>> def build(x,y):
	return lambda:x*x+y*y

>>> build(1,2)
<function <lambda> at 0x7f625c0e0668>
>>> f=build(1,3)
>>> f()
10
>>> def now():
	print '2013-13-25'

	
>>> f=now()
2013-13-25
>>> f
>>> f=now
>>> f()
2013-13-25
>>> f._name_

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    f._name_
AttributeError: 'function' object has no attribute '_name_'
>>> now._name_

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    now._name_
AttributeError: 'function' object has no attribute '_name_'
>>> def now():
	print '2013-12-2'

	
>>> f=now
>>> now.__name__
'now'
>>> f.__now__

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    f.__now__
AttributeError: 'function' object has no attribute '__now__'
>>> f.__name__
'now'
>>> def log(func):
	def wrapper(*args,**kw):
		print 'call %s():' %func.__name__

		
>>> def log(func):
	def wrapper(*args,**kw):
		print 'call %s():' %func.__name__
		return func(*args,**kw)
	return wrapper

>>> def now():
	print '2014-08-19'

	
>>> @log
def now():
	print '2014-08-19'

	
>>> now()
call now():
2014-08-19
>>> def log(func):
	def wrapper(*args,**kw):
		
KeyboardInterrupt
>>> cls

Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s():' %(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

>>> @log('2014-08-19')
def now():
	print 'hhhhh'

	
>>> now()
2014-08-19 now():
hhhhh
>>> int('12333')
12333
>>> int('12332',16)
74546
>>> import functools
>>> int2=functools.partial(int,base=1)
>>> int2('123')

Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    int2('123')
ValueError: int() base must be >= 2 and <= 36
>>> int2=functools.partial(int,base=16)
>>> int2('2133')
8499
>>> 
