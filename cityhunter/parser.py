
import re

def run():
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