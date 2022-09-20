import tkinter as tk
from tkinter.messagebox import showinfo,askokcancel,showerror
from tkinter.filedialog import askopenfilename
from Lib import config
import sys

#Add config Root App


class add_cf(object):
	def __init__(self,*x):

		if x and config.check_true():
			#other functions
			self.pathfile = (lambda:self.txt_e.get('1.0','end-1c').strip().split('\n'))
			self.exit=(lambda x:x.destroy())

			#other args
			self.err1=0
			self.gd1=0
			self.cwm_res = {}

			#create tk onject for add configuration	
			self.target = tk.Tk()
			self.target.configure(bg='#2E2E2E')
			
			#master target_root
			self.lable = tk.Label(text='-Password Generator Pro-\nv1.2\n$ By Edward $',bg='#404040',fg='white')
			self.target.title('PGP')
			self.target.geometry('400x355')
			self.target.resizable(False,False)

			#create frames
			self.frame1 = tk.Frame(master=self.target,bg='#2C2C2C',height=175)
			self.frame2 = tk.Frame(master=self.target,bg='#2C2C2C',height=175)
			self.frame3= tk.Frame(master=self.target,bg='#000000',height=2)

			#place and pack widgets
			self.frame1.pack(fill=tk.BOTH)
			self.frame3.pack(fill=tk.BOTH)
			self.frame2.pack(fill=tk.BOTH)
			self.button1 = tk.Button(master=self.target,text='Exit',width=12,height=1,command=(lambda:self.exit(self.target)),bg='#454545',fg='white')
			self.adm()
			self.button1.place(x=300,y=30)
			self.target.mainloop()
		
		else:
			showerror('Error','You Have Bad config.txt File Please Change config.txt File')

	
	def adm(self):
		#frame1
		self.lable_error = tk.Label(master = self.frame1,text='Click Add to Add new method !!',bg='#454545',fg='white',width=50,height=2)
		self.lable_error.place(x=25,y=135)
		self.lable_min = tk.Label(master = self.frame1,text='=',bg='#2C2C2C',fg='white',width=2,height=2)
		self.lable_min.place(x=90,y=30)
		self.txt_m1 = tk.Text(self.frame1,width=10,height=3)
		self.txt_m2 = tk.Text(self.frame1,width=10,height=3)
		self.txt_m1.place(x=5,y=20)
		self.txt_m2.place(x=110,y=20)
		self.button_addcwm = tk.Button(master=self.frame1,text='Add Change Word Method',width=30,height=2,command=(lambda:self.getresult(1)),bg='#454545',fg='white')
		self.button_addcwm.place(x=78,y=90)
		#frame2
		self.lable_error1 = tk.Label(master = self.frame2,text='Click Add to Add new method !!',bg='#454545',fg='white',width=50,height=2)
		self.lable_error1.place(x=25,y=135)
		self.txt_e = tk.Text(self.frame2,width=20,height=3)
		self.txt_e.place(x=5,y=20)
		self.button_addewm = tk.Button(master=self.frame2,text='Add End Word Method',width=30,height=2,command=(lambda:self.getresult(2)),bg='#454545',fg='white')
		self.button_addewm.place(x=78,y=90)

	def getresult(self,*x):
		#add new methods to config.txt file
		self.cwm = {}
		if x:
			if x[0]==1:
				self.err1=0
				self.gd1=0
				self.getres12()
				if self.restxt1[0]!='' and self.restxt2[0]!='' and len(self.restxt1)==len(self.restxt2):

					for i in range(len(self.restxt2)):
						
						if len(self.restxt2[i])==1 and len(self.restxt1[i])==1:
							self.cwm[self.restxt1[i]]=self.restxt2[i]
							self.gd1+=1
						
						else:
							self.handle_error(1,'Invalid Values')
							self.err1+=1
						
					kys = list(config.config(1).keys())

					for i in list(self.cwm.keys()):
						if i in kys:
							self.err1+=1
							self.gd1-=1
							continue
						self.cwm_res[i]=self.cwm.get(i)

					self.handle_access(1,f'You Have {self.err1} Bad Values And {self.gd1} Good Values')
					
					if self.gd1>0:
						print('yes')
						config.add_config(1,self.cwm_res)
					else:
						return None
				

				else:
					self.handle_error(1,'Error Occurred')

			else:
				res=self.pathfile()
				if res[0]!='':
					config.add_config(2,res)
					self.handle_access(2,f'You Have {len(res)} Good Values')
				else:
					self.handle_error(2,'Error Empty Box')
		else :
			showerror('Error','Error occurred')
	def getres12(self):
		#get all text in txtbox cwm(Change Word Method)
		self.restxt1 = self.txt_m1.get('1.0','end-1c').strip().split('\n')
		self.restxt2 = self.txt_m2.get('1.0','end-1c').strip().split('\n')

	def handle_error(self,x,text):
		#this func for handle errors 1 = cwm(Change Word Method) and 2 = ewm(End Word Method)
		if x==1:
			self.lable_error.configure(bg='darkred',text=text)
		elif x==2:
			self.lable_error1.configure(bg='darkred',text=text)
	def handle_access(self,x,text):
		#this func for handle good messages 1 = cwm(Change Word Method) and 2 = ewm(End Word Method)
		if x==1:
			self.lable_error.configure(bg='darkcyan',text=text)
		elif x==2:
			self.lable_error1.configure(bg='darkcyan',text=text)
