#usr/bin/python3

'''
athor : Edward
date :2022/02/21
version : 1.2v

'''


import tkinter as tk
import sys
import threading
from Lib import t1
from Lib import config
from Lib import add_method_app as ac
from tkinter.messagebox import showinfo,askokcancel
from tkinter.filedialog import askopenfilename


################################
def methods(func1,func2,x):
	#1 and 2 methods flags
	if x==3:
		shart = endwordcount
	elif x==2:
		shart = changewordcount
	elif x==4:
		shart = capitalwordcount
	else:
		shart = capitalseccendcount

	if shart%2==0:
		func2.configure(bg='green')
		func1.configure(text=f'{message[x]} Succes',bg='green')
		pelas(x,1)
	else:
		func2.configure(bg='darkred')
		func1.configure(text=f'{message[x]} Faild',bg='darkred')
		pelas(x,-1)

def pelas(x,i):
	#change methods value
	global endwordcount,changewordcount,capitalwordcount,capitalseccendcount
	if x == 3:
		endwordcount+=i
	elif x==2:
		changewordcount+=i
	#elif x==4:
	#	capitalwordcount+=i
	elif x==1:
		capitalseccendcount+=i
	else :
		pass




################################

#get all text in textbox as list
pathfile = (lambda:txt.get('1.0','end-1c').strip().split('\n'))

#func for getting methods
#get all methods for endword in Lib/config.py
lolaii = (lambda:config.config())

#endword method
def endword(passwords):
	#this method adding the shapes in end of words
	#Example : password = password@123
	if lolaii!=0:
		endwordshape = lolaii()[1]
	global result
	result=[]	
	for pwd in passwords:
		for shp in endwordshape:
			result.append(str(pwd+shp))
			#result.append(str(shp+pwd))




################################
changewordmethod = lolaii()[0]
def changeword(passwords):
	#this method Change the words with your methods
	#Example : password = p@ssword
	#Example : password = passw0rd
	global result
	if lolaii!=0:
		changewordmethod = lolaii()[0]
	result_chgw = None
	halat=2
	flg=0
	ya_ali=[]

	for i in passwords:
		for m in t1.generate(halat,foo(i)[1]):
				#print(t1.generate(halat,foo(i)[1]))
				ya_ali.append(bar(m,i))
	for i in ya_ali:
		result.append(i)

def dorost(m,w):
	kalame =''
	flg = 0
	for i in w:
		if i not in changewordmethod:
			kalame+=i

		else:
			if m[flg]=='1':
				kalame+='1'
				
			else:
				kalame+=i
			flg+=1
	#print(kalame)
	return kalame

def bar(method,word):
	gg = 0
	kalame = ''

	#for i in word:
	#	if i not in changewordmethod:
	#		kalame+=i
	#	else :
	for x,ii in enumerate(dorost(method,word)):
		if word[x]==ii:
			kalame+=ii
		elif ii=='1':
			kalame+=changewordmethod.get(word[x])
		else:
			continue

	return kalame



def foo(x):
	#this func for ehtemalat
	qwe=list(changewordmethod.keys())
	h=''
	flg = 1
	cont=0
	#cont is kol hallat
	for i in x:
		flg = 0
		for ii in qwe:
			if i == ii:
				h+='1'
				cont+=1
				flg = 1
				break
		if not flg:
			h+='x'
	return(h,cont)

################################################



def capitalword(passwords):
	#Soon !!
	pass



#################



def capitalseccend(passwords):
	global result
	for i in passwords:
		result.append(i)
		ii = i[0].capitalize()+i[1:]
		result.append(ii)

	#result=[]
	#for i in ok:
	#	result.append(i)


######################


def check_empty():
	global result
	if result:
		return [result]
	else:
		passwords = [pathfile()]
		return passwords
def main():
	#start the Process APP 
	
	global endwordcount,changewordcount,capitalwordcount,capitalseccendcount,result,txt,lable5,listmethods
	passwords = [pathfile()]
	if txt.get('1.0','end-1c').strip()=='':
		lable5.configure(text=f'{message[5]}',bg='darkred')
	else:


		l_m = [capitalseccendcount,changewordcount,endwordcount,capitalwordcount]
		for i in range(4):
			if l_m[i]:
				if i !=1:
					x1 = threading.Thread(target=listmethods[i],args=check_empty())
					x1.start()
					x1.join()
				else:
					xx = threading.Thread(target=changeword,args=check_empty())
					xx.start()
					xx.join()

		wx = threading.Thread(target=inseert,args=[result])
		wx.start()
	passwords=[]
	result=[]

##################

def inseert(x):
	#insert passwords to main TextBox
	global txt
	txt.delete('1.0',tk.END)
	for i in x:
		print(i)
		txt.insert(tk.END,i+'\n')

def save_to_file():
	#save the result in file
	pass


##################

# ac = add_config 
# adding methods(config)
def conf(*x):
	tar=ac.add_cf(1)


################################
def c_file():
	with open('result.txt','a') as w:
		w.flush()


pathfile_nosplit = (lambda:txt.get('1.0','end-1c'))
def select_file():
    filetypes = (
    	('result','result.txt'),
        ('all file','*.txt'),
        
    )
    c_file()
    filename = askopenfilename(
        title='Open a file',
        initialdir='.',
        filetypes=filetypes)
    if filename:
    	with open(filename,'a') as w:
    		w.write(pathfile_nosplit())
    	showinfo(
    	    title='Saved',
    	    message='Done !',
    	    )
#######################

def exit(x):
	if askokcancel("askquestion", "Are you sure?"):
		x.destroy()
	else:
		return




#create Tk object
root = tk.Tk()
root.configure(bg='#2E2E2E')


#create Frames
frame1 = tk.Frame(master=root,bg='#2C2C2C',height=250)
frame2 = tk.Frame(master=root,bg='#2C2C2C',height=250)
frame3 = tk.Frame(master=root,bg='#000000',height=5)

#masetr root
lable = tk.Label(text='-Password Generator Pro-\nv1.2\n$ By Edward $',bg='#404040',fg='white')
root.title('PGP')
root.geometry('700x500')
root.resizable(False,False)	


#master frame1
lable3 = tk.Label(master=frame1,text='',bg='green',fg='white',height=1,width=2)
lable2 = tk.Label(master=frame1,text='',bg='green',fg='white',height=1,width=2)
lable4 = tk.Label(master=frame1,text='',bg='darkred',fg='white',height=1,width=2)
lable1 = tk.Label(master=frame1,text='',bg='green',fg='white',height=1,width=2)
lable5 = tk.Label(master = frame1,text='Click Start to Generate Password !!',bg='#454545',fg='white',width=60,height=2)

button3 = tk.Button(master=frame1,text='Capital Seccend',width=12,height=1,command=(lambda:methods(lable5,lable1,1)),bg='#454545',fg='white')
button2 = tk.Button(master=frame1,text='Change Word',width=12,height=1,command=(lambda:methods(lable5,lable2,2)),bg='#454545',fg='white')
button4 = tk.Button(master=frame1,text='End Word',width=12,height=1,command=(lambda:methods(lable5,lable3,3)),bg='#454545',fg='white')
button = tk.Button(master=frame1,text='Capital Word',width=12,height=1,command=(lambda:methods(lable5,lable4,4)),bg='#454545',fg='white')

#add config button
button2_1 = tk.Button(master=frame1,text='Add method',width=12,height=1,command=(lambda:conf(1)),bg='#454545',fg='white')


button1 = tk.Button(master=frame1,text='START',width=16,height=8,command=main,bg='#454545',fg='white')



#master frame2
scrollbar = tk.Scrollbar(frame2)
scrollbar.pack( side = tk.LEFT, fill = tk.Y )
txt = tk.Text(frame2,width=50,height=10,yscrollcommand = scrollbar.set)
button_1 = tk.Button(master=frame2,text='Exit',width=12,height=1,command=(lambda:exit(root)),bg='#454545',fg='white')
button_2 = tk.Button(master=frame2,text='Save The Result To File',width=18,height=1,command=(lambda:select_file()),bg='#454545',fg='white')



#pack , place and grid
txt.pack(side=tk.LEFT)
scrollbar.config(command=txt.yview)
lable.pack(fill=tk.BOTH)
lable1.place(x=130,y=10)
lable2.place(x=130,y=50)
lable3.place(x=130,y=90)
lable4.place(x=130,y=130)
lable5.place(x=10,y=200)
frame1.pack(fill=tk.BOTH)
frame3.pack(fill=tk.BOTH)
frame2.pack(fill=tk.BOTH)
button3.place(x=20,y=10)
button2.place(x=20,y=50)
button2_1.place(x=200,y=50)
button4.place(x=20,y=90)
button.place(x=20,y=130)
button1.place(x=450,y=90)
button_1.place(x=600,y=140)
button_2.place(x=560,y=90)



message = ['','Capital Seccend','Change Word','EndWord Method','Soon !!','Error Empty Box']

endwordcount=1
changewordcount=1
capitalwordcount=1
capitalseccendcount=1
listmethods = [capitalseccend,changeword,endword,capitalword]
result = []
finalresult = None

if __name__=='__main__':
	#start the app
	root.mainloop()
