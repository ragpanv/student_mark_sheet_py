from tkinter import *
from math import ceil
r =Tk() 
r.title("STUDENT MARKSHEET") 
r.geometry("900x900") 

o1 = Entry(r) 
o2 = Entry(r) 
o3 = Entry(r) 
o4 = Entry(r) 
o5 = Entry(r) 
o6 = Entry(r) 
o7 = Entry(r) 
o8 = Entry(r)
o9 = Entry(r)

def display():
    Label(r,text=o1.get()).place(x=100,y=320)
    Label(r,text=o2.get()).place(x=100,y=340)
    Label(r,text=o3.get()).place(x=100,y=360)
    m1,m2,m3,m4,m5,m6=int(o4.get()),int(o5.get()),int(o6.get()),int(o7.get()),int(o8.get()),int(o9.get())
    total=0
    if m1>=90 and m1<=100:
        Label(r,text="S").place(x=400,y=120)
        total=total+40
    elif m1>=80 and m1<90:
        Label(r,text="A").place(x=400,y=120)
        total=total+36
    elif m1>=70 and m1<80:
        Label(r,text="B").place(x=400,y=120)
        total=total+32
    elif m1>=60 and m1<70:
        Label(r,text="C").place(x=400,y=120)
        total=total+28
    elif m1>=50 and m1<60:
        Label(r,text="D").place(x=400,y=120)
        total=total+24
    else:
        Label(r,text="F").place(x=400,y=120)
        total=total+0
        
    if m2>=90 and m2<=100:
        Label(r,text="S").place(x=400,y=140)
        total=total+40
    elif m2>=80 and m2<90:
        Label(r,text="A").place(x=400,y=140)
        total=total+36
    elif m2>=70 and m2<80:
        Label(r,text="B").place(x=400,y=140)
        total=total+32
    elif m2>=60 and m2<70:
        Label(r,text="C").place(x=400,y=140)
        total=total+28
    elif m2>=50 and m2<60:
        Label(r,text="D").place(x=400,y=140)
        total=total+24
    else :
        Label(r,text="F").place(x=400,y=140)
        total=total+0
        
    if m3>=90 and m3<=100:
        Label(r,text="S").place(x=400,y=160)
        total=total+40
    elif m3>=80 and m3<90:
        Label(r,text="A").place(x=400,y=160)
        total=total+36
    elif m3>=70 and m3<80:
        Label(r,text="B").place(x=400,y=160)
        total=total+32
    elif m3>=60 and m3<70:
        Label(r,text="C").place(x=400,y=160)
        total=total+28
    elif m3>=50 and m3<60:
        Label(r,text="D").place(x=400,y=160)
        total=total+24
    else :
        Label(r,text="F").place(x=400,y=160)
        total=total+0
        
    if m4>=90 and m4<=100:
        Label(r,text="S").place(x=400,y=180)
        total=total+40
    elif m4>=80 and m4<90:
        Label(r,text="A").place(x=400,y=180)
        total=total+36
    elif m4>=70 and m4<80:
        Label(r,text="B").place(x=400,y=180)
        total=total+32
    elif m4>=60 and m4<70:
        Label(r,text="C").place(x=400,y=180)
        total=total+28
    elif m4>=50 and m4<60:
        Label(r,text="D").place(x=400,y=180)
        total=total+24
    else :
        Label(r,text="F").place(x=400,y=180)
        total=total+0
    
    if m5>=90 and m5<=100:
        Label(r,text="S").place(x=400,y=200)
        total=total+30
    elif m5>=80 and m5<90:
        Label(r,text="A").place(x=400,y=200)
        total=total+27
    elif m5>=70 and m5<80:
        Label(r,text="B").place(x=400,y=200)
        total=total+24
    elif m5>=60 and m5<70:
        Label(r,text="C").place(x=400,y=200)
        total=total+21
    elif m5>=50 and m5<60:
        Label(r,text="D").place(x=400,y=200)
        total=total+18
    else :
        Label(r,text="F").place(x=400,y=200)
        total=total+0
    
    if m6>=90 and m6<=100:
        Label(r,text="S").place(x=400,y=220)
        total=total+30
    elif m6>=80 and m6<90:
        Label(r,text="A").place(x=400,y=220)
        total=total+27
    elif m6>=70 and m6<80:
        Label(r,text="B").place(x=400,y=220)
        total=total+24
    elif m6>=60 and m6<70:
        Label(r,text="C").place(x=400,y=220)
        total=total+21
    elif m6>=50 and m6<60:
        Label(r,text="D").place(x=400,y=220)
        total=total+18
    else :
        Label(r,text="F").place(x=400,y=220)
        total=total+0
        
    #Label(r,text=str(total)).place(x=180,y=240)    
    Label(r,text=str(ceil(total/10))).place(x=100,y=380)
    Label(r,text=str(total/22)).place(x=100,y=400)
Label(r, text="Name").place(x=20, y=20) 

Label(r, text="Reg.No").place(x=20, y=40) 

Label(r, text="Roll.No").place(x=20, y=60)

Label(r, text="Srl.No",font=('Arial',10),fg='Blue').place(x=20, y=100) 
Label(r, text="1").place(x=20, y=120) 
Label(r, text="2").place(x=20, y=140) 
Label(r, text="3").place(x=20, y=160) 
Label(r, text="4").place(x=20, y=180) 
Label(r, text="5").place(x=20, y=200) 
Label(r, text="6").place(x=20, y=220) 


Label(r, text="Subject Code",font=('Arial',10),fg='Blue').place(x=60, y=100) 
Label(r, text="UCS001").place(x=60, y=120) 
Label(r, text="UCS002").place(x=60, y=140) 
Label(r, text="UCS003").place(x=60, y=160) 
Label(r, text="UCS004").place(x=60, y=180) 
Label(r, text="UCS005").place(x=60, y=200) 
Label(r, text="UCS006").place(x=60, y=220) 

Label(r, text="Student Marks",font=('Arial',10),fg='Blue').place(x=180, y=100) 
o4.place(x=180, y=120) 
o5.place(x=180, y=140) 
o6.place(x=180, y=160) 
o7.place(x=180, y=180) 
o8.place(x=180, y=200) 
o9.place(x=180, y=220) 

Label(r, text="Sub Credit",font=('Arial',10),fg='Blue').place(x=320, y=100) 
Label(r, text="4").place(x=320, y=120) 
Label(r, text="4").place(x=320, y=140) 
Label(r, text="4").place(x=320, y=160) 
Label(r, text="4").place(x=320, y=180) 
Label(r, text="3").place(x=320, y=200) 
Label(r, text="3").place(x=320, y=220) 

Label(r, text="Total 22").place(x=320, y=240) 
Label(r, text="Grade obtained",font=('Arial',10),fg='Blue').place(x=400, y=100) 

Label(r,text="NAME : ",font=('Arial',10),fg='magenta2').place(x=20, y=320)
Label(r,text="Reg.No : ",font=('Arial',10),fg='magenta2').place(x=20, y=340)
Label(r,text="Roll.No : ",font=('Arial',10),fg='magenta2').place(x=20, y=360)
o1=Entry(r) 
o2=Entry(r) 
o3=Entry(r) 
o1.place(x=100, y=20) 
o2.place(x=100, y=40) 
o3.place(x=100, y=60) 

button1=Button(r, text="submit", bg="green", command=display) 
button1.place(x=20, y=280) 

Label(r, text="Total credit",font=('Arial',10),fg='magenta2').place(x=20, y=380) 
Label(r, text="SGPA",font=('Arial',10),fg='magenta2').place(x=20, y=400) 
r.mainloop() 

