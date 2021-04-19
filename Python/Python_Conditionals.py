#Booleans are True and False
if True:
	print('Conditional is True')

#Below print statement is not executed
if False:
	print('This is not printed, conditional is False')

language = 'Python'

if language == 'Python':
	print('Language is Python')
else:
	print('Language is not Python')


language = 'Java'

if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
else:
	print('Language is neither Python nor Java')


language = 'R'

if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
else:
	print('Language is neither Python nor Java')



#and
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin_Page')
else:
	print('Bad Creds')


logged_in = False

if user == 'Admin' and logged_in:
	print('Admin_Page')
else:
	print('Bad Creds')



#or
if user == 'Admin' or logged_in:
	print('Admin_Page')
else:
	print('Bad Creds')


#not
if not logged_in:
	print("Please log in!!")
else:
	print("Welcome!!")


logged_in = True
if not logged_in:
	print("Please log in!!")
else:
	print("Welcome!!")



#'is' tests if two objects are the same in memory, i.e., they have the same objectid
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)

#a and b have different object ids, so "a is b" returns False
print(id(a))
print(id(b))

#Now assign b to a, so "a is b" returns True
b = a
print(a is b)
print(id(a))
print(id(b))


#Below will always evaluate to False in Python
     #False
     #None
     #Zero of any numeric type
     #Empty String ''
     #Any empty sequence. Example: (), []
     #Any empty mapping/dictionary. Exampe: {}

condition = False

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')



condition = None

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')



condition = 0

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')



condition = 0.0

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')



condition = ''

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')



condition = ()

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')



condition = []

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')



condition = {}

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')