from tkinter import *
import tkinter.font as font
exp=''

def btn_click(x):
	global exp
	exp=exp+str(x)
	eqn.set(exp)

def clear_click():
	global exp
	exp=""
	eqn.set("")

def equal_click():
	try:
		global exp
		total=str(eval(exp))
		eqn.set(total)
		exp=total
	except:
		eqn.set(" error ")
		exp="" 
  
if __name__ == "__main__": 

	root=Tk()
	root.configure(background='black')
	root.title('calculator')
	#root.geometry('270x150')
	eqn=StringVar()
	large_font = ('Verdana',20)

	ip=Entry(root,width=20,textvariable=eqn,font=large_font)
	ip.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
	myFont = font.Font(family='Verdana' ,size=15)

	btn1=Button(root,text=1,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(1))
	btn2=Button(root,text=2,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(2))
	btn3=Button(root,text=3,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(3))
	btn4=Button(root,text=4,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(4))
	btn5=Button(root,text=5,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(5))
	btn6=Button(root,text=6,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(6))
	btn7=Button(root,text=7,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(7))
	btn8=Button(root,text=8,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(8))
	btn9=Button(root,text=9,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(9))
	btn0=Button(root,text=0,padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click(0))

	btn_add=Button(root,text='+',padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click('+'))
	btn_equal=Button(root,text='=',padx=40,pady=20,height=1, width=2,bg='#cc4e2b', fg='white',font=myFont,command=equal_click)
	btn_sub=Button(root,text='-',padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click('-'))
	btn_mul=Button(root,text='*',padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click('*'))
	btn_div=Button(root,text='/',padx=40,pady=20,height=1, width=2,bg='#767e8a', fg='white',font=myFont,command=lambda:btn_click('/'))
	btn_clear=Button(root,text='clear',padx=40,pady=20,height=1,bg='#3da656', fg='white',font=myFont, width=2,command=clear_click)
	
	btn1.grid(row=3,column=0)
	btn2.grid(row=3,column=1)
	btn3.grid(row=3,column=2)
	btn4.grid(row=2,column=0)
	btn5.grid(row=2,column=1)
	btn6.grid(row=2,column=2)
	btn7.grid(row=1,column=0)
	btn8.grid(row=1,column=1)
	btn9.grid(row=1,column=2)
	btn0.grid(row=4,column=0)

	btn_add.grid(row=4,column=3)
	btn_equal.grid(row=4,column=2)
	btn_sub.grid(row=3,column=3)
	btn_mul.grid(row=2,column=3)
	btn_div.grid(row=1,column=3)
	btn_clear.grid(row=4,column=1)

	root.mainloop()