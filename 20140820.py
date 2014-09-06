#!/usr/bin/env python
# _*_ CODING:UTF-8 _*_

' a test module '

__author__='tm'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print 'Hello,world!'
	elif len(args)==2:
		print 'Hello,%s!' %args[1]
	else:
		print 'Too many arguments!'

if __name__=='__main_':
	test()
