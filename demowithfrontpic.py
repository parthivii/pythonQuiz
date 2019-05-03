from Tkinter import *
root=Tk()
def wish():
    root.destroy()
    root1=Tk()
    Label(root1,text='Hi There Human!....\n',relief='ridge',font='times 25 bold italic',bg='white',width=16,bd=3).grid(row=0,column=0,columnspan=4)
    Label(root1,text='Please Enter Your Name....\n',relief='ridge',font='times 15 bold italic',bg='pink',width=20,bd=5).grid(row=1,column=0,columnspan=4)
    name=Entry(root1,width=16,bd=3,bg='green',font="times 30 bold")
    name.grid(row=2,column=0,columnspan=4)
    def first():
        root1.destroy()
        root2=Tk()
        Label(root2,text="What is the tip of shoelace called?").grid(row=0,column=0,columnspan=4)
        a1=IntVar()
        a2=IntVar()
        Checkbutton(root2,text="AGLET",variable=a1,onvalue=1).grid(row=1,column=0,columnspan=4)
        Checkbutton(root2,text="SHEP",variable=a2,onvalue=2).grid(row=2,column=0,columnspan=4)
        def second():
            root2.destroy()
            root3=Tk()
            Label(root3,text="What is the world's longest river?").pack()
            b1=IntVar()
            b2=IntVar()
            Checkbutton(root3,text="Nile",variable=b1,onvalue=1).pack()
            Checkbutton(root3,text="Amazon",variable=b2,onvalue=2).pack()
            def third():
                root3.destroy()
                root4=Tk()
                Label(root4,text="When did the cold war end?").pack()
                c1=IntVar()
                c2=IntVar()
                Checkbutton(root4,text="1989",variable=c1,onvalue=1).pack()
                Checkbutton(root4,text="1967",variable=c2,onvalue=2).pack()
                def fourth():
                    root4.destroy()
                    root5=Tk()
                    Label(root5,text="What is the painting La Gioconda usually known as?").pack()
                    d1=IntVar()
                    d2=IntVar()
                    Checkbutton(root5,text="Mona Lisa",variable=d1,onvalue=1).pack()
                    Checkbutton(root5,text="The Vancouver Fort",variable=d2,onvalue=2).pack()
                    def fifth():
                        root5.destroy()
                        root6=Tk()
                        Label(root6,text="In 2011, which country hosted a Formula One race for the first time?").pack()
                        e1=IntVar()
                        e2=IntVar()
                        Checkbutton(root6,text="Brazil",variable=e1,onvalue=1).pack()
                        Checkbutton(root6,text="India",variable=e2,onvalue=2).pack()
                        def result():
                            root6.destroy()
                            root7=Tk()
                            s=0
                            c=0
                            i=0
                            if int(a1.get())==1:
                                s=s+1
                                c=c+1
                            if int(a2.get())==2:
                                i=i+1
                            if int(b1.get())==1:
                                i=i+1
                            if int(b2.get())==2:
                                s=s+1
                                c=c+1
                            if int(c1.get())==1:
                                s=s+1
                                c=c+1
                            if int(c2.get())==2:
                                i=i+1
                            if int(d1.get())==1:
                                s=s+1
                                c=c+1
                            if int(d2.get())==2:
                                i=i+1
                            if int(e1.get())==1:
                                i=i+1
                            if int(e2.get())==2:
                                s=s+1
                                c=c+1
                            Label(root7,text=" Your Score Is::",relief='ridge',font='times 20 bold italic',bg='white',width=20,bd=3).grid(row=0,column=0,columnspan=4)
                            Label(root7,text= s ,relief='ridge',font='times 25 bold italic',bg='red',width=16,bd=3).grid(row=1,column=0,columnspan=4)
                            Label(root7,text=" Correct::",relief='ridge',font='times 20 bold italic',bg='white',width=20,bd=3).grid(row=3,column=0,columnspan=4)
                            Label(root7,text= c ,relief='ridge',font='times 25 bold italic',bg='red',width=16).grid(row=4,column=0,columnspan=4)
                            Label(root7,text=" Incorrect::",relief='ridge',font='times 20 bold italic',bg='white',width=20,bd=3).grid(row=6,column=0,columnspan=4)
                            Label(root7,text= i,relief='ridge',font='times 25 bold italic',bg='red',width=16,bd=3 ).grid(row=7,column=0,columnspan=4)
                            root7.mainloop()
                        Button(root6,text="Next!!",width=10,height=1,bg="yellow",command=result).pack()      
                        root6.mainloop()   
                    Button(root5,text="Next!!",width=10,height=1,bg="yellow",command=fifth).pack()            
                    root5.mainloop()        
                Button(root4,text="Next!!",width=10,height=1,bg="yellow",command=fourth).pack()            
                root4.mainloop()
            Button(root3,text="Next!!",width=10,height=1,bg="yellow",command=third).pack()
            root3.mainloop()
        Button(root2,text="Next!!",width=10,height=1,bg="yellow",command=second).grid(row=5,column=0,columnspan=4)            
        root2.mainloop()    
    Button(root1,text="Bring It On!!",width=16,height=4,bg="red",command=first,bd=3).grid(row=3,column=0,columnspan=4)
    root1.mainloop()
b=PhotoImage(file='namee.gif')
lb=Label(root,image=b)
lb.after(5000,wish)
lb.pack()    
root.mainloop()
