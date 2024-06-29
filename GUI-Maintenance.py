from tkinter import *
from tkinter import messagebox
# import csv
from datetime import datetime
from db_maintenance import *
from tkinter import ttk #Theme GUI

# from songline import Sendline

# token = 'Eh99aZ7rMljTdGeSHB2JKWjPhscmrPj0mutNdgfW3yO'
# messenger = Sendline(token)

GUI = Tk()
GUI.title('GUI for Maintenance')
GUI.geometry('1000x600+50+50')

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

# save 
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

# Style TreeView
style = ttk.Style()
style.configure('Treeview.Heading',padding=(10,10),font=('tahome',10,'bold'))
style.configure('Treeview',rowheight=25,font=('tahome',9))

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
        d = list(d) #Convert Tuple to List
        del d[0]
        mtwordorderlist.insert('','end',values=d)

# Edit TreeView
def EditPage_mtworkorder(event=None):
    select = mtwordorderlist.selection()
    output = mtwordorderlist.item(select) #Dictionary = List
    # print(output['values'])

    op = output['values']
    t_tsid = op[0]
    t_name = op[1]
    t_department = op[2]
    t_machine = op[3]
    t_problem = op[4]
    t_number = op[5]
    t_tel = '0{}'.format(op[6])

    # Form Edit Data
    GUI2 = Toplevel()
    GUI2.title('แก้ไขข้อมูลใบแจ้งซ่อม')
    GUI2.geometry('500x500')

    L = Label(GUI2,text='ใบแจ้งซ่อม',font=FONT1)
    L.place(x=80,y=10)

    L = Label(GUI2,text='ชื่อผู้แจ้ง',font=FONT2)
    L.place(x=30,y=50)
    v_name2=StringVar()
    v_name2.set(t_name)
    E1 = ttk.Entry(GUI2,textvariable=v_name2,font=FONT2)
    E1.place(x=150,y=50)

    L = Label(GUI2,text='แผนก',font=FONT2)
    L.place(x=30,y=100)
    v_department2=StringVar()
    v_department2.set(t_department)
    E2 = ttk.Entry(GUI2,textvariable=v_department2,font=FONT2)
    E2.place(x=150,y=100)

    L = Label(GUI2,text='อุปกรณ์/เครื่อง',font=FONT2)
    L.place(x=30,y=150)
    v_machine2=StringVar()
    v_machine2.set(t_machine)
    E3 = ttk.Entry(GUI2,textvariable=v_machine2,font=FONT2)
    E3.place(x=150,y=150)

    L = Label(GUI2,text='อาการเสีย',font=FONT2)
    L.place(x=30,y=200)
    v_problem2=StringVar()
    v_problem2.set(t_problem)
    E4 = ttk.Entry(GUI2,textvariable=v_problem2,font=FONT2)
    E4.place(x=150,y=200)

    L = Label(GUI2,text='หมายเลข',font=FONT2)
    L.place(x=30,y=250)
    v_number2=StringVar()
    v_number2.set(t_number)
    E5 = ttk.Entry(GUI2,textvariable=v_number2,font=FONT2)
    E5.place(x=150,y=250)

    L = Label(GUI2,text='เบอร์โทร',font=FONT2)
    L.place(x=30,y=300)
    v_tel2=StringVar()
    v_tel2.set(t_tel)
    E6 = ttk.Entry(GUI2,textvariable=v_tel2,font=FONT2)
    E6.place(x=150,y=300)

    def save():
        name =v_name2.get()
        department =v_department2.get()
        machine =v_machine2.get()
        problem =v_problem2.get()
        number =v_number2.get()
        tel =v_tel2.get()
        # print(number)

        # dt = datetime.now().strftime('%y%m%d%H%M%S')

        update_mtworkorder(t_tsid,'name',name)
        update_mtworkorder(t_tsid,'department',department)
        update_mtworkorder(t_tsid,'machine',machine)
        update_mtworkorder(t_tsid,'problem',problem)
        update_mtworkorder(t_tsid,'number',number)
        update_mtworkorder(t_tsid,'tel',tel)

        update_table()
        GUI2.destroy()

    def reset():
        v_name.set("")
        v_department.set("")
        v_machine.set("")
        v_problem.set("")
        v_number.set("")
        v_tel.set("")

    B = ttk.Button(GUI2,text=' บันทึกใบแจ้งซ่อม ',command=save)
    B.place(x=30,y=350)

    GUI2.mainloop()

mtwordorderlist.bind('<Double-1>',EditPage_mtworkorder)

def Delete_mtworkorder(Event=None):
    select = mtwordorderlist.selection()
    output = mtwordorderlist.item(select) #Dictionary = List
    # print(output['values'])

    op = output['values']
    tsid = op[0]
    print(tsid)

    check = messagebox.askyesno('ยื่นยันการลบข้อมูล','คุณต้องการลบข้อมูลหรือไม่...?')
    # print(check)
    if check == True:
        delete_mtworkorder(tsid) 
        update_table()  

mtwordorderlist.bind('<Delete>',Delete_mtworkorder)
    
update_table()

GUI.mainloop()