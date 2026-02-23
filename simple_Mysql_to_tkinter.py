from tkinter import *
import mysql.connector

# Function to insert data
def save_data():

    con = mysql.connector.connect(
    host="localhost",
    user="anmoluser",
    password="Anmol@1234567890",
    database="college"
    )

    cur = con.cursor()
    # cur.execute("INSERT INTO student (name, age) VALUES (%s, %s)", (name, age))
    cur.execute("SELECT * FROM student")


    result = cur.fetchall()
    # con.commit()
    con.close()

    # print("Data Saved")
    return result

# GUI
root = Tk()
root.title("Student Form")
root.geometry("300x200")

a = save_data()
b = a[1]
Label(root,text=b).pack()

# Button(root, text="Save", command=save_data).pack(pady=10)

root.mainloop()