
import re

def Find(pat, text):
	results = re.findall(pat, text)
	for result in results:
		print (result)
	#for i, val in enumerate(strlist):
	#    print i, val

def Split(pat, text):
	print(re.split(pat, text))

def Find(pat, text):
    match = re.search(pat, text)
    if match:        
        print (match.group())
    else:
        print ("Not found")

def run():
	#Find("data=.*", "name=\"jim lo\" data=cat")
	file = open("output.txt", "r")
	txt = file.readline()
	txt.decode('utf8')
	Find("(title=\")(.*)(\"|\s)", txt)

	#encoded = '\xe4\xbb\x8a\xe5\xa4\xa9\xe5\xa4\xa9\xe6\xb0\xa3\xe7\x9c\x9f\xe5\xa5\xbd'
	#msg = encoded.decode('utf8')
	#print msg

	f = open("output.txt", encoding = 'utf8')
	l = f.readline()
	print(l)
	#(title=\")(.*)(\">)'
	matchobj = re.match(r"(id=)", l)
	if matchobj:
		print(matchobj.group(0))
	else:
		print("not found")
	f.close()

if __name__ == '__main__':
	run()