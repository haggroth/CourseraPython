name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mails = dict()
for line in handle:
	words = line.split()
	if len(words) == 0 : continue
	if words[0] != 'From': continue
	addr = words[1]
	if  mails.has_key(addr):
		mails[addr] += 1
	else:
		mails[addr] = 1
maxnum = 0
maxname = ''
for name in mails:
	if mails[name] > maxnum:
		maxnum = mails[name]
		maxname = name
print maxname, maxnum