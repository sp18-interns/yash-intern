from MyMainPackage import *

from MyMainPackage.Subpackage import *


some_main_script.report_main()
mysubscript.sub_report()


print('Top Level One.py')

def func():
	print('One.py is here')


if __name__=='__main__':
	print('One.py is being run directly')
else:
	print('One.py has been imported')	
