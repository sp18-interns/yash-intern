import one

one.func()

print('Top Level two.py')

if __name__=='__main__':
	print('Two.py is being run directly')
else:
	print('Two.py has been imported')	