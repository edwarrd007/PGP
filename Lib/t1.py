import subprocess as sub

def generate_halat(halat,tas):
	w = open('Lib/t2.py','w')
	mimi = 'i'
	tab = ''
	w.write('l=[]')
	for x,i in enumerate(range(tas)):
		w.write(f'\n{tab}for {mimi} in range({halat}):')
		mimi+='i'
		tab+='    '
	mimi = 'i'
	for i in range(tas):
		w.write(f'\n{tab}l.append({mimi})')
		mimi+='i'
	w.write('\nprint(l)')
	w.flush()
	w.close()





array = ''
lolo=[]
def generate(halat,cont):
	#halat is halat haye yek shaye ya yek coin ke 2 halat dare : ro & posht
	#cont is tedad yek shaye ya yek coin 
	global array,lolo
	array = ''
	lolo=[]
	xx=0
	generate_halat(halat,cont)
	x = sub.check_output('python Lib/t2.py',shell=True)

	tar = x.decode().strip().replace('[','').replace(']','').replace(',','').replace(' ','')
	#for i in range(len(x)):
	for i in tar:
		array+=i
		xx+=1
		if xx==cont:
			lolo.append(array)
			array=''
			xx=0
	
	return lolo