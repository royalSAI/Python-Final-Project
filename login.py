from Tkinter import *
from sqlite3 import dbapi2 as sqlite

login=sqlite.connect("grocery.sqlite")
l=login.cursor()
WinStat = ''



def again():    #for login window-----------------------------------------------------------------------------LOGIN WINDOW
    global un, pwd, WinStat, root, application
    if WinStat=='application':
        application.destroy()
    root=Tk()
    root.title('INDIAN GROCERY STORE')
    Label(root,text='INDIAN GROCERY STORE').grid(row=0,column=0,columnspan=5)
    Label(root,text="1602 ,Chatham Hills, Springfield-62704, Illinois").grid(row=1,column=0,columnspan=5)
    Label(root,text='--------------------------------------------------------------').grid(row=2,column=0,columnspan=5)
    Label(root, text='Username').grid(row=3, column=1)
    un=Entry(root,width=10)
    un.grid(row=3, column=2)
    Label(root, text='Password').grid(row=4, column=1)
    pwd=Entry(root,width=10, show="*")
    pwd.grid(row=4, column=2)
    Label(root,text='').grid(row=5,column=0,columnspan=5)
    Button(root,width=6,text='Enter',command=check).grid(row=6, column=1)
    Button(root,width=6,text='Close',command=root.destroy).grid(row=6, column=2)
    root.mainloop()
    
def check():    #for enter button in login window
    global un, pwd, login, l, root
    u=un.get()
    p=pwd.get()
    l.execute("select * from logs")
    for i in l:     
        if i[0]==u and i[1]==p and u=='admin':
            root.destroy()
            open_win()
            print "admin here"
        elif i[0]==u and i[1]==p:
            root.destroy()
            # open_cus()
            print "Cus here"
        elif i[0]!=u or i[1]!=p:
            top=Tk()
            Label(top,width=30, text='Wrong Username or Password').grid(row=0, column=0)
            top.destroy()
            top.mainloop()
    login.commit()

def open_win(): #OPENS MAIN MENU----------------------------------------------------------------------------MAIN MENU
    global application, WinStat
    WinStat='application'
    application=Tk()
    application.title("INDIAN GROCERY STORE")
    Label(application, text="INDIAN GROCERY STORE").grid(row=0,column=0,columnspan=3)
    Label(application, text='*'*80).grid(row=1,column=0,columnspan=3)
    Label(application, text='-'*80).grid(row=3,column=0,columnspan=3) 

    Label(application, text="Stock Maintenance").grid(row=2,column=0)
    Button(application,text='Add product to Stock', width=25, command = stock).grid(row=5,column=0)
    Button(application,text='Delete product from Stock', width=25).grid(row=6,column=0)
    

    Label(application, text="Access Database").grid(row=2,column=1)
    Button(application,text='Modify',width=15).grid(row=4,column=1)
    Button(application,text='Search', width=15).grid(row=5,column=1)
    Button(application,text='Expiry Check', width=15).grid(row=6,column=1)

    Label(application, text="Handle Cash Flows").grid(row=2,column=2)
    Button(application,text="Check Today's Revenue", width=20).grid(row=5,column=2)
    Button(application,text='Billing', width=20).grid(row=4,column=2)

    Label(application, text='-'*80).grid(row=12,column=0,columnspan=3)    
    Button(application,text='Logout',command=again).grid(row=13, column=2)
    application.mainloop()

    
def stock():
    application.destroy()
    import stockdetails
    a = stockdetails.stock()
    print a
    
again()