#1 Вариант 1.1
print ("----Вариант 1----")
a = [1, 2, 5, 7, 3, 0]
print (a)

i = 0
nmin = i
min = a[nmin]

while (i < len(a)):
	if (a[i] < min):
		nmin = i
		min = a[nmin]
	i = i + 1
print (min)
print ("----Вариант 2----")

#1 Вариант 1.2
a = [1, 2, 5, 7, 3, 0]
print (a)

i = 0
m = a[0]
for i in range(len(a)):
	if a[i] < m:
		m = a[i]
print (m)