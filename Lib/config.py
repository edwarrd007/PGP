
EWM=''
CWM=''
text = None
def config(*w):
	#return methods to root
	#change word method and end word method
	global CWM,EWM
	ewm=[]
	cwm={}
	if openf and check_true():
		openf()
		for i in EWM[1].split(','):
			ewm.append(i)
		for i in CWM[1].split(','):
			d = i.split('=')
			cwm[d[0]]=d[1]
		if w:
			return cwm
		else:
			return (cwm,ewm)
	else:
		return 0
def add_config(x,res):
	res1=''
	res2=''
	old_keys=None
	new_keys=None
	ccres=None
	ret = []
	ret1 = []
	with open('config.txt','r') as ww :
		ccres = ww.readlines(900000)

	if type(res)==dict:
		old_keys = list(config(1).keys())
		new_keys = list(res.keys())
		res1 = ccres[2].replace('\n','')
		for i in new_keys:
			if i not in old_keys:
				res1+=','+i+'='+res.get(i)
			else:
				continue
		ret1.append(ccres[0])
		ret1.append(ccres[1])
		ret1.append(res1)
		save(ret1)
	else:
		res2 = ccres[0].replace('\n','')
		for i in res:
			if i not in res2:
				res2+=','+i

		res2+='\n'
		ret.append(res2)
		ret.append(ccres[1])
		ret.append(ccres[2])
		save(ret)

def save(result):
	with open('config.txt','w') as w:
		for i in result:
			w.write(i)
def openf():
	global CWM,EWM,text
	if check_true():
		EWM=text.split(':')[0].split('<->')
		CWM=text.split(':')[1].split('<->')
		return 1
	else:
		return 0


def check_true():
	global text
	with open('config.txt','r') as w:
		text = w.read().replace('\n','')
		if ':' in text and 'EWM' in text and 'CWM' in text:
			return 1
		else:
			return 0