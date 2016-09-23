#2
def cats(a):
	s = 0
	for x in a:
		s += x
	return s
def average(a):
	return cats(a)/len(a)
import stat
a = [1, 4, 6, 3, 8, 5]

print (a)
print (cats(a))
print (average(a))