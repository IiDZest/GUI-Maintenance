import sqlite3

#Connection sqllite3
conn = sqlite3.connect('maintenance.sqlite3')

#Cursor = execute sqlite3
c = conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT,
                    name TEXT,
                    department TEXT,
                    machine TEXT,
                    problem TEXT,
                    number TEXT,
                    tel TEXT)""")
# insert
def insert_mtworkorder(tsid,name,department,machine,problem,number,tel):
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,name,department,machine,problem,number,tel))
    conn.commit()
    # print('saved')

# insert_mtworkorder('TS1003','EEE EEE','IT','Notebook','ปิดไม่ติด','11012','0123456711')

# select
def view_mtwordorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()
        # print(result)
    return result

# result = view_mtwordorder()
# print(result)
# print(result[1][1])

# update
def update_mtworkorder(tsid,field,newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command,(newvalue,tsid))
    conn.commit()
    # print('updated')

# update_mtworkorder('TS1002','name','XXX XXX')

# delete 
def delete_mtworkorder(tsid):
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid=(?)'
        c.execute(command,([tsid]))
    conn.commit()
    # print('deleted')