from tkinter import *
from tkinter import messagebox
# import csv
from datetime import datetime
from db_maintenance import *
from datetime import datetime
from tkinter import ttk #Theme GUI

# from songline import Sendline

# token = 'Eh99aZ7rMljTdGeSHB2JKWjPhscmrPj0mutNdgfW3yO'
# messenger = Sendline(token)

GUI = Tk()
GUI.title('GUI for Maintenance')
GUI.geometry('850x600+50+50')

FONT1 = ('tahoma',12)
FONT2 = ('tahoma',10)
# FONT3 = ('tahoma',10,'bold')

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1,text='ใบแจ้งซ่อม')
Tab.add(T2,text='ดูใบแจ้งซ่อม')
Tab.add(T3,text='สรุป')
Tab.pack(fill=BOTH,expand=1)



# T1
L = Label(T1,text='ใบแจ้งซ่อม',font=FONT1)
L.place(x=80,y=10)

L = Label(T1,text='ชื่อผู้แจ้ง',font=FONT2)
L.place(x=30,y=50)
v_name=StringVar()
E1 = ttk.Entry(T1,textvariable=v_name,font=FONT2)
E1.place(x=150,y=50)

L = Label(T1,text='แผนก',font=FONT2)
L.place(x=30,y=100)
v_department=StringVar()
E2 = ttk.Entry(T1,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)

L = Label(T1,text='อุปกรณ์/เครื่อง',font=FONT2)
L.place(x=30,y=150)
v_machine=StringVar()
E3 = ttk.Entry(T1,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)

L = Label(T1,text='อาการเสีย',font=FONT2)
L.place(x=30,y=200)
v_problem=StringVar()
E4 = ttk.Entry(T1,textvariable=v_problem,font=FONT2)
E4.place(x=150,y=200)

L = Label(T1,text='หมายเลข',font=FONT2)
L.place(x=30,y=250)
v_number=StringVar()
E5 = ttk.Entry(T1,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)

L = Label(T1,text='เบอร์โทร',font=FONT2)
L.place(x=30,y=300)
v_tel=StringVar()
E6 = ttk.Entry(T1,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)

# def writecsv(record_list):
#     with open('data.csv','a',newline='',encoding='utf8') as file:
#         fw = csv.writer(file)
#         fw.writerow(record_list)

def save():
    name =v_name.get()
    department =v_department.get()
    machine =v_machine.get()
    problem =v_problem.get()
    number =v_number.get()
    tel =v_tel.get()

    text='ชื่อผู้แจ้ง: '+name+'\n'
    text=text+'แผนก: '+department+'\n'
    text=text+'อุปกรณ์/เครื่อง: '+machine+'\n'
    text=text+'อาการเสีย: '+problem+'\n'
    text=text+'หมายเลข: '+number+'\n'
    text=text+'เบอร์โทร: '+tel+'\n'

    # dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # datalist = [dt,name,department,machine,problem,number,tel]
    # writecsv(datalist)

    #send message
    # messenger.sendtext(text)

    tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S')) + 114152147165)
    insert_mtworkorder(tsid,name,department,machine,problem,number,tel)

    update_table()
    reset()
    # messagebox.showinfo('กำลังบันทึกข้อมูล...!',text)

def reset():
    v_name.set("")
    v_department.set("")
    v_machine.set("")
    v_problem.set("")
    v_number.set("")
    v_tel.set("")

B = ttk.Button(T1,text=' บันทึกใบแจ้งซ่อม ',command=save)
B.place(x=30,y=350)
# B1 = ttk.Button(T1,text=' ล้างข้อมูล ',command=reset)
# B1.place(x=160,y=350)
# B2 = ttk.Button(T1,text=" ปิดหน้าต่าง ",command=GUI.destroy)
# B2.place(x=250,y=350)

#L.grid(row=1,column=1)
#L.place(x=20,y=50)
#L.pack()

# T2
L = Label(T2,text='ดูใบแจ้งซ่อม',font=FONT1)
L.pack()

header = ['TSID','ชื่อผู้แจ้ง','แผนก','อุปกรณ์/เครื่อง','อาการเสีย','หมายเลข','เบอร์โทร']
headerrw = [100,100,100,150,200,100,100]

mtwordorderlist = ttk.Treeview(T2,columns=header,show='headings',height=10)
mtwordorderlist.pack()

# mtwordorderlist.heading('TSID',text='TSID')
for h,w in zip(header,headerrw):
    mtwordorderlist.heading(h,text=h)
    mtwordorderlist.column(h,width=w,anchor='center')

mtwordorderlist.column('TSID',anchor='w')

def update_table():
    mtwordorderlist.delete(*mtwordorderlist.get_children()) #Clear TreeView
    data = view_mtwordorder()
    # print(data)

    for d in data:
        d = list(d)
        del d[0]
        mtwordorderlist.insert('','end',values=d)

update_table()

GUI.mainloop()