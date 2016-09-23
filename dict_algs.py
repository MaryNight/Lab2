#4
def child(masd):
	mas=[]
	for d in masd:
		for ch in d['children']:
			if ch['age']>18:
				mas.append(d['name'])
				break
	return mas
	
mary={
	"name":"mary",
	"age": 39,
	"children":[{
		"name": "mark",
		"age": 19,
		},{
			"name":"masha",
			"age":10,
			}],
	}

ilusha={
	"name":"ilusha",
	"age":37,
	"children":[{
		"name":"mark",
		"age": 19,
	},{
		"name": "masha",
		"age": 10,
		}],
	}
	
mat={
	"name":"mat",
	"age": 54,
	"children":[{
		"name": "den",
		"age": 16,
		},{
			"name":"ed",
			"age":10,
			}],
	}
emps = [mary, ilusha, mat]
print (child(emps))