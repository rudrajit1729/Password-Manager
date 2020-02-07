from tkinter import *
from tkinter import messagebox
import tkinter.messagebox

# Global Variables

objects = []
window= Tk()
window.withdraw()
window.title('Password Manager')

# Classes

class Changepass(object):

    loop = False
    attempts = 0

    def __init__(self, master):

        top = self.top = Toplevel(master)
        top.title('Change Pass')
        top.geometry('{}x{}'.format(250, 220))
        top.resizable(width=False, height=False)

        self.passw = Label(top, text="Initial Password:", font=('Courier', 14), justify=CENTER)
        self.passw.pack()
        self.epass = Entry(top, show="*", width=30)
        self.epass.pack(pady=7)
        self.npassw = Label(top, text="New Password:", font=('Courier', 14), justify=CENTER)
        self.npassw.pack()
        self.nepass = Entry(top, show="*", width=30)
        self.nepass.pack(pady=7)
        self.cpassw = Label(top, text="Confirm Password:", font=('Courier', 14), justify=CENTER)
        self.cpassw.pack()
        self.cepass = Entry(top, show="*", width=30)
        self.cepass.pack(pady=7)
        self.confirm = Button(top, text='Proceed', command=self.change, font=('Courier', 14))
        self.confirm.pack(padx=7)


    def change(self):

        # Access the initial password
        try:
            access = ""
            f = open('access.txt', 'r')
            text = f.read()
            # print(text) # test print
            f.close()
            for letter in text:
                if letter == ' ':
                    access += ' '
                else:
                    access += chr(ord(letter) - 5)
            # print(access) Test printing

        except: # Set initial password to 'rudy'
            access = 'rudy'
            f = open('access.txt', 'w')
            f.write('wzi~')
            f.close()

        self.initial = self.epass.get()
        self.final = self.nepass.get()
        self.cfinal = self.cepass.get()


        if self.initial == access and self.final == self.cfinal:
            f = open('access.txt','w')
            text = self.final
            accessnew = ""
            for letter in text:
                if letter == ' ':
                    accessnew += ' '
                else:
                    accessnew += chr(ord(letter) + 5)
            f.write(accessnew)
            f.close()
            self.loop = True
            messagebox.showinfo("Success","Password Updated Successfully!!")
            self.top.destroy()
            # window.deiconify() # directly opens a/c when u change pass successfully

        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.epass.delete(0, 'end')
            messagebox.showerror('Password Mismatch',
                                 'Password Mismatch Try again, attempts remaining: ' + str(5 - self.attempts))

class popupWin(object):

    loop = False
    attempts = 0

    def __init__(self, master):

        top = self.top = Toplevel(master)
        top.title('A/C Storage')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width=False, height=False)

        self.passw = Label(top, text="Password:", font=('Courier', 14), justify=CENTER)
        self.passw.pack()
        self.epass = Entry(top, show="*", width=30)
        self.epass.pack(pady=7)
        self.login = Button(top, text='Log In', command=self.cleanup, font=('Courier', 14))
        self.login.pack(padx=7,side =RIGHT)
        self.change = Button(top, text='Change Pass', command=self.changepass, font=('Courier', 14))
        self.change.pack(padx=7,side = LEFT)

    def changepass(self):

        # print("Yes") # Test print
        self.epass.delete(0, 'end')
        Changepass(self.top)

    def cleanup(self):

        self.value = self.epass.get()

        # Access the password Initially set as 'rudy'. Change in access.txt to change password.
        try:
            access = ""
            f = open('access.txt', 'r')
            text = f.read()
            f.close()
            for letter in text:
                if letter == ' ':
                    access += ' '
                else:
                    access += chr(ord(letter) - 5)

        except:
            access = 'rudy'
            f = open('access.txt','w')
            f.write('wzi~')
            f.close()

        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()

        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.epass.delete(0, 'end')
            messagebox.showerror('Incorrect Password',
                                 'Incorrect password, attempts remaining: ' + str(5 - self.attempts))


class entity_add:

    def __init__(self, master, n, p, e):

        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def write(self):

        f = open('emails.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()

class entity_display:

    def __init__(self, master, n, e, p, i):

        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.label_name = Label(self.window, text=dencryptedN, font=('Courier', 14))
        self.label_email = Label(self.window, text=dencryptedE, font=('Courier', 14))
        self.label_pass = Label(self.window, text=dencryptedP, font=('Courier', 14))
        self.deleteButton = Button(self.window, text='X', fg='red', command=self.delete)

    def display(self):

        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=1)
        self.label_pass.grid(row=6 + self.i, column=2, sticky=E)
        self.deleteButton.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):

        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):

        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()


# Functions

def onsubmit():

    m = email.get()
    p = password.get()
    n = name.get()
    e = entity_add(window, n, p, m)
    e.write()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: ' + n + '\nEmail: ' + m + '\nPassword: ' + p)
    readfile()

def clearfile():

    f = open('emails.txt', "w")
    f.close()


def readfile():

    try:
        f = open('emails.txt', 'r')

    except:
        f = open('emails.txt', 'w')
        f.close()
        f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()

# Graphics

m = popupWin(window)

entity_label = Label(window, text='Add Entity', font=('Courier', 18))
name_label = Label(window, text='Name: ', font=('Courier', 14))
email_label = Label(window, text='UserID: ', font=('Courier', 14))
pass_label = Label(window, text='Password: ', font=('Courier', 14))
name = Entry(window, font=('Courier', 14))
email = Entry(window, font=('Courier', 14))
password = Entry(window, show='*', font=('Courier', 14))
submit = Button(window, text='Add Account', command=onsubmit, font=('Courier', 14))

entity_label.grid(columnspan=3, row=0)
name_label.grid(row=1, sticky=E, padx=3)
email_label.grid(row=2, sticky=E, padx=3)
pass_label.grid(row=3, sticky=E, padx=3)

name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)

name_label2 = Label(window, text='Name: ', font=('Courier', 14))
email_label2 = Label(window, text='UserID: ', font=('Courier', 14))
pass_label2 = Label(window, text='Password: ', font=('Courier', 14))

name_label2.grid(row=5)
email_label2.grid(row=5, column=1)
pass_label2.grid(row=5, column=2)

readfile()

window.mainloop()