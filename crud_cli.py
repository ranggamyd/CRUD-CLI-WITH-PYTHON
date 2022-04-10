import psycopg2 as db
import os

con = None,
connected = None,
cursor = None


def connect():
    global connected, con, cursor

    try:
        con = db.connect(
            host="localhost",
            database="blog_db",
            port=5432,
            user="ranggamyd",
            password="ranggamyd"
        )
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor


def disconnect():
    global connected, con, cursor

    if(connected == True):
        cursor.close()
        con.close()
    else:
        con = None
        connected = False


def show():
    global connected, con, cursor

    a = connect()
    a.execute("SELECT * FROM blogs LIMIT 100")
    records = a.fetchall()

    print(records)
    print('List of My Blogs!')


def store():
    global connected, con, cursor

    title = input("Title: ")
    body = input("Body: ")
    author = input("Author: ")
    a = connect()
    sql = "INSERT INTO blogs (title, body, author) values ('" + \
        title+"','"+body+"','"+author+"')"
    a.execute(sql)
    con.commit()
    print('Data has been added successfully!')


def find():
    global connected, con, cursor

    keywords = input('Keywords: ')
    a = connect()
    sql = "SELECT * FROM blogs WHERE title LIKE '%" + \
        keywords+"%' OR body LIKE '%"+keywords+"%'"
    a.execute(sql)
    records = a.fetchall()

    if a.rowcount < 0:
        print("No data available")
    else:
        print(records)


def update():
    global connected, con, cursor

    show()
    id = input("Select ID > ")
    title = input("New Title: ")
    body = input("New Body: ")
    author = input("New Author: ")

    a = connect()
    sql = "UPDATE blogs SET title='"+title+"',body='" + \
        body+"',author='"+author+"' WHERE id='"+id+"'"
    a.execute(sql)
    con.commit()
    print('Data has been updated successfully!')


def destroy():
    global connected, con, cursor

    show()
    id = input("Select ID > ")
    confirm = input('Are you sure? (y/n)')
    if(confirm.upper() == "Y"):
        a = connect()
        sql = "DELETE FROM blogs WHERE id='"+id+"'"
        a.execute(sql)
        con.commit()
        print('Data has been deleted successfully!')
    else:
        print('Action canceled')


def index():
    os.system("clear")
    print("=== CRUD APP WITH CLI PYTHON ===")
    print("\n")
    print("1. Show Records")
    print("2. Insert Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. Exit")
    print("\n")
    menu = input("Select Menu > ")

    os.system("clear")

    if menu == "1":
        show()
    elif menu == "2":
        store()
    elif menu == "3":
        update()
    elif menu == "4":
        destroy()
    elif menu == "5":
        find()
    elif menu == "0":
        exit()
    else:
        print("Wrong number!")
        print("Please select between 0-5!")


if __name__ == "__main__":
    while(True):
        index()
