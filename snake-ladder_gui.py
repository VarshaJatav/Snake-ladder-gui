

from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from random import *
root=Tk()
root.geometry("605x725")


i1=Image.open("one.png")
i1=i1.resize((80,80))
im1=ImageTk.PhotoImage(i1)

i2=Image.open("two.png")
i2=i2.resize((80,80))
im2=ImageTk.PhotoImage(i2)

i3=Image.open("three.png")
i3=i3.resize((80,80))
im3=ImageTk.PhotoImage(i3)

i4=Image.open("four.png")
i4=i4.resize((80,80))
im4=ImageTk.PhotoImage(i4)

i5=Image.open("five.png")
i5=i5.resize((80,80))
im5=ImageTk.PhotoImage(i5)

i6=Image.open("six.png")
i6=i6.resize((80,80))
im6=ImageTk.PhotoImage(i6)

d={1:38,4:14,9:31,17:7,21:42,28:84,51:67,54:34,62:19,64:60,71:91,80:100,87:24,93:73,95:75,98:79}

pos1=Button(root,text="Position: ",bg="lightblue")
pos1.grid(row=2,column=0)

pos2=Button(root,text="Position: ",bg="#FDBBBB")
pos2.grid(row=2,column=9)

b=[]
for i in range(9,-1,-1):
    if i%2!=0:
        for j in range(0,10):
            a=str(i)+str(j)
            b.append(a)
    elif i%2==0:
        for j in range(9,-1,-1):
            a=str(i)+str(j)
            b.append(a)        

i={1:im1,2:im2,3:im3,4:im4,5:im5,6:im6}
x1,x2=0,0
a1,a2=True,False
def fun1():
    global x1,i,g1,b1,d,but1,a1,a2,but2,imgg1,imgg2,x2,b2
    r=randint(1,6)
    imgg1=i[r]
      
    a1,a2=False,True
    but1.grid_forget() 
    but2.grid_forget()
  
    a=0
    x1=x1+r
    if x1 in d.keys():
        x1=d[x1]
    
    if x1>100:
        x1=x1-r
    elif x1==100:
        won=Button(root,text="Player 1 won ",bg="lightblue")
        won.grid(row=2,column=5)
        but2.grid_forget()
        but2=Button(root,image=imgg1,borderwidth=0,command=fun2,state=DISABLED).grid(row=1,column=9)

    for j in b:
        a+=1
        if a==x1:
            break
        
    but1=Button(root,image=imgg1, borderwidth=0,command=fun1)
    but2=Button(root,image=imgg2, borderwidth=0,command=fun2)
    if r==6 or x1==x2:
        a1,a2=True,False
        but2=Button(root,image=imgg2, borderwidth=0,command=fun2,state=DISABLED)
    if a1==False:
        but1=Button(root,image=imgg1,borderwidth=0,command=fun1,state=DISABLED)
    but1.grid(row=1,column=0)
    but2.grid(row=1,column=9)
    if x1==x2:
        x2=0 
        pos2=Button(root,text=f"Position: {x2}",bg="#FDBBBB")
        pos2.grid(row=2,column=9)
        b2.grid_forget()
        b2=Label(root,image=g2,justify=CENTER)
        b2.grid(row=2,column=9,sticky='e')

    pos1=Button(root,text=f"Position: {x1}",bg="lightblue")
    pos1.grid(row=2,column=0)
    b1.grid_forget()
    b1=Label(frame,image=g1,justify=CENTER)
    b1.grid(row=j[0],column=j[1])
      

def fun2():
    global x2,but2,i,g2,b2,d,a1,a2,imgg1,imgg2,but1,x1,b1
    r=randint(1,6)
    imgg2=i[r]
    a1,a2=True,False
    but1.grid_forget()
    but2.grid_forget() 
    a=0
    x2=x2+r
    if x2 in d.keys():
        x2=d[x2]
    
    if x2>100:
        x2=x2-r
    elif x2==100:
        won=Button(root,text="Player 2 Won ",bg="#FDBBBB")
        won.grid(row=2,column=5)
        but1.grid_forget()
        but1=Button(root,image=imgg2,borderwidth=0,command=fun1,state=DISABLED).grid(row=1,column=0)
         
    for j in b:
        a+=1
        if a==x2:
            break
    
    but1=Button(root,image=imgg1, borderwidth=0,command=fun1)
    but2=Button(root,image=imgg2, borderwidth=0,command=fun2)
    if r==6 or x1==x2:
        a1,a2=False,True
        but1=Button(root,image=imgg1, borderwidth=0,command=fun1,state=DISABLED)
    if a2==False:
        but2=Button(root,image=imgg2,borderwidth=0,command=fun2,state=DISABLED)
    but1.grid(row=1,column=0)
    but2.grid(row=1,column=9) 
    if x1==x2:
       x1=0
       pos1=Button(root,text=f"Position: {x1}",bg="lightblue")
       pos1.grid(row=2,column=0)
       b1.grid_forget()
       b1=Label(root,image=g1,justify=CENTER)
       b1.grid(row=2,column=0,sticky='w')

    pos2=Button(root,text=f"Position: {x2}",bg="#FDBBBB")
    pos2.grid(row=2,column=9)
    b2.grid_forget()
    b2=Label(frame,image=g2,justify=CENTER)
    b2.grid(row=j[0],column=j[1])
    
# for i in range(10):
#     for j in range(1,11):
#         s=str(i)+str(j)
#         if j==10:
#             s=int((i + (j /10) )*10) 
#         b=Button(root,text=s,state=DISABLED,padx=25,pady=25,border=3,relief=RAISED,font="sans 9 bold")
#         b.grid(row=i,column=j)

frame = Frame(root, width =600, height=600)
frame.grid(row=0,column=0,columnspan=10)
frame.propagate(0)

img=Image.open("snake_ladder.png")
img=img.resize((600,600))
imgg=ImageTk.PhotoImage(img)
lab=Label(frame, image=imgg)
lab.image=imgg
lab.grid(row=0,column=0,columnspan=10,rowspan=10)

img1=Image.open("dice.png")
img1=img1.resize((80,80))
imgg1=ImageTk.PhotoImage(img1)
but1=Button(root,image=imgg1, borderwidth=0,command=fun1)
but1.grid(row=1,column=0,sticky="w")

img2=Image.open("dice.png")
img2=img2.resize((80,80))
imgg2=ImageTk.PhotoImage(img2)
but2=Button(root,image=imgg2, borderwidth=0,command=fun2,state=DISABLED)
but2.grid(row=1,column=9,sticky="e")

goti1=Image.open("goti1.png")
goti1=goti1.resize((20,20))

g1=ImageTk.PhotoImage(goti1)
b1=Label(root,image=g1)
b1.grid(row=2,column=0,sticky="w")

goti2=Image.open("goti2.png")
goti2=goti2.resize((20,20))
g2=ImageTk.PhotoImage(goti2)
b2=Label(root,image=g2)
b2.grid(row=2,column=9,sticky="e")

root.mainloop()



