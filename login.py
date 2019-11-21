import tkinter as tk
from tkinter import END
from Encryptors import Encrypt_Cezar

'''

Loign 1.0 

to update : 
    - password no duplicates 
    - password encryption mode 2 == AES ( XOR bitwise encryption) 
    - interface , add picture, background color 
    - add default icon 
    
'''

def main_window():
    #====================== MAIN WINDOW =======================#
    main_window = tk.Tk()
    main_window.geometry("400x400")
    main_window.title("login system")
    #====================== +++++++++++ =======================#

    #----BUTTONS----#

    button1 = tk.Button(text = "Login", height = 3 , width = 10, command = Login_window)
    button1.grid(column = 1, row = 1 )

    button2 = tk.Button(text = "Register", height = 3 , width = 10, command = Register_window)
    button2.grid(column = 1, row = 3)

    #----LABELS----#

    title = tk.Label(text = "\n\nWelcome in my login system\n\n", font = ("Arial", 12))
    title.grid(column = 1, row = 0)

    # --------window format--------#

    empty = tk.Label(text="                          ")
    empty.grid(column=0, row=0)

    empty2 = tk.Label(text="\n")
    empty2.grid(column=1, row=2)

    main_window.mainloop()

#-------------------------------------------- WINDOWS -----------------------------------------------------#

def login_succeeded(user_name):

    # =================== login succeeded WINDOW =======================#
    looged_window = tk.Tk()
    looged_window.geometry("500x500")
    looged_window.title("Hello")
    # =================== +++++++++++++++++++++++ =======================#

    # ----LABELS----#
    tk.Label(looged_window, text ="\n\n\n Hello " + user_name + " \n login successful" , font = "Arial, 20", fg = "red").pack()

def Register_window():
    # ====================== Register WINDOW =======================#
    global register_window
    register_window = tk.Tk()
    register_window.geometry("400x200")
    register_window.title("User Registration")
    # ====================== ++++++++++++++++ =======================#

    # ----Variables----#
    username = tk.StringVar()
    password = tk.StringVar()

    # ----LABELS----#
    title = tk.Label(register_window, text="\nPlease enter details below to register\n")
    title.grid(column=1, row=0)

    label1 = tk.Label(register_window, text="Enter login")
    label1.grid(column=0, row=1)

    label2 = tk.Label(register_window, text="Enter Password")
    label2.grid(column=0, row=2)

    # ----Entries----#
    global ent1_register
    ent1_register  = tk.Entry(register_window, textvariable = username)
    ent1_register.grid(column=1, row=1)

    global ent2_register
    ent2_register = tk.Entry(register_window, textvariable = password)
    ent2_register.grid(column=1, row=2)

    # ----Buttons----#
    button1 = tk.Button(register_window, text="Register", command = user_registration)
    button1.grid(column=1, row =3 )

    register_window.mainloop()
def Login_window():

    # ====================== Login WINDOW =======================#
    global login_window
    login_window = tk.Tk()
    login_window.geometry("400x200")
    login_window.title("User login")
    # ====================== ++++++++++++ =======================#

    # ----Variables----#
    username = tk.StringVar()
    password = tk.StringVar()

    # ----LABELS----#
    title = tk.Label(login_window, text = "\nPlease enter details below to login\n")
    title.grid(column = 1, row = 0)

    label1 = tk.Label(login_window, text = "Enter login")
    label1.grid(column = 0, row = 1)

    label2 = tk.Label(login_window, text ="Enter Password")
    label2.grid(column = 0, row = 2)

    # ----Entries----#
    global ent1_login
    ent1_login = tk.Entry(login_window, textvariable = username)
    ent1_login.grid(column = 1, row = 1)

    global ent2_login
    ent2_login = tk.Entry(login_window, textvariable = password)
    ent2_login.grid(column = 1, row = 2)

    # ----Buttons----#
    button1 = tk.Button(login_window, text = "Login", command = login_verification)
    button1.grid(column = 0, row = 3)


#-------------------------------------------- FUNCTIONS -----------------------------------------------------#

def login_verification():
    '''this method validates user n psswd'''

    # store strings from login window in variables
    username_string = ent1_login.get()
    password_string = ent2_login.get()



    # read data from file
    stream = open("shadow1.txt", "rt")
    lines = stream.readlines()

    data = ''

    # exam: data_file vs data_entered
    for line in lines:
        # check username
        if line[0:len(username_string)] == username_string:
            # encrypt username to data and compare with data from shadow
            data = line
            key_index = data.find('$')
            key = data[key_index+1:]

            cezar_enc = Encrypt_Cezar(password_string, int(key))
            password_string = str(cezar_enc[0])
            password_string = password_string + '$' + key
            print("password im comapring with", password_string)

            if line[len(username_string) + 1:].strip() == password_string.strip():
                print("password correct")
                login_succeeded(username_string)
            else:
                incorrect_password = tk.Label(login_window, text="wrong password")
                incorrect_password.grid()
        else:
            print("incorrect user")
            incorrect_user = tk.Label(login_window, text="Wrong user")
            incorrect_user.grid()

    stream.close()

def user_registration():
    '''this method performs user registration'''

    # store strings from register window in variables
    username_string = ent1_register.get()
    password_string = ent2_register.get()

    # encrypt password (cezar encryption)
    cezar_enc = Encrypt_Cezar(password_string)
    password_string = str(cezar_enc[0])

    #rot#
    key0 = str(cezar_enc[1])
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ testing
    print('user registered= ', username_string)
    print('password registered= ', password_string)
    print('key registered= ', key0)

    # write data into "shadow" file
    file = open("shadow1.txt", "at")
    file.write(username_string + ":")
    file.write(password_string + "$")
    file.write(key0 + "\n")
    file.close()
    #00001 bug if there is nothing for password it wont jump to next line -- fix later

    # display registration message
    label = tk.Label(register_window, text ="Registration Successfull", fg="red")
    label.grid(column = 1 , row = 4 )

    # clear entry fields
    ent1_register.delete(0,END)
    ent2_register.delete(0,END)

if __name__ == '__main__':
    main_window()
else:
    pass
