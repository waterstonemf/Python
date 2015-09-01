import re

msg = "Line1: Hello Python, I am testing the regular expression. \r\nLine2: So \\r\\n really mean something?\r\nLine3: I don't know"
print msg

line = re.search(r"Line\d",msg)

print line.group(0)

print type(line.group)

line = re.match(r"Line3",msg)
if line:
	print line.group(0)
else:
	print 'No match'


lines = re.findall(r"Line\d",msg)
for l in lines:
	print l
	
	
pattern = 'abc123456efg'

num = re.search('\d+',pattern)
if num:
	print num.group(0)
	
num_pattern = re.search('(\d+)',pattern)
if num_pattern:
	print num_pattern.group(1)