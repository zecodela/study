
import re

def Find(pat, text):
    match = re.search(pat, text)
    if match:        
        print (match.group())
    else:
        print ("Not found")

def run():
    Find("tel=.*\b$", "tel=60716030 name=jimlo")
        
if __name__ == '__main__':
	run()