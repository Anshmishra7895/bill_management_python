# Import tkinter module
from tkinter import *

# Make a window
window = Tk()

# Specify its size
window.geometry("800x600")

# Make the window non-resizable
window.resizable(False, False)

# Set the background color to black
window.configure(bg='black')

# Function to calculate the price of all the orders
def calculate():
    # Dictionary for storing the food quantity and price
    dic = {
        'aloo_paratha': [e1, 30],
        'samosa': [e2, 5],
        'pizza': [e3, 150],
        'chilli_potato': [e4, 50],
        'chowmein': [e5, 70],
        'gulab_jamun': [e6, 35]
    }
    total = 0
    for key, val in dic.items():
        if val[0].get() != "":
            total += int(val[0].get()) * val[1]

    label16 = Label(window, text="Your Total Bill is - " + str(total), font="times 18", fg='white', bg='black')

    # Position it
    label16.place(x=20, y=490)
    label16.after(1000, label16.destroy)
    window.after(1000, calculate)

label8 = Label(window, text="🍽 Shri Restaurant 🍽", font="times 28 bold", fg='white', bg='black')
label8.place(x=350, y=20, anchor="center")

label1 = Label(window, text="🍴 Menu 🍴", font="times 28 bold", fg='white', bg='black')
label1.place(x=520, y=70)

label2 = Label(window, text="🍱Aloo Paratha: Rs 30", font="times 18", fg='white', bg='black')
label2.place(x=450, y=120)

label3 = Label(window, text="🍙Samosa: Rs 5", font="times 18", fg='white', bg='black')
label3.place(x=450, y=150)

label4 = Label(window, text="🍕Pizza: Rs 150", font="times 18", fg='white', bg='black')
label4.place(x=450, y=180)

label5 = Label(window, text="🍔Burger: Rs 50", font="times 18", fg='white', bg='black')
label5.place(x=450, y=210)

label6 = Label(window, text="🍜Noodles: Rs 70", font="times 18", fg='white', bg='black')
label6.place(x=450, y=240)

label7 = Label(window, text="☕Coffee: Rs 35", font="times 18", fg='white', bg='black')
label7.place(x=450, y=270)

# Billing section
label9 = Label(window, text="Select the items", font="times 18", fg='white', bg='black')
label9.place(x=115, y=70)

label10 = Label(window, text="🍱Aloo Paratha", font="times 18", fg='white', bg='black')
label10.place(x=20, y=120)

e1 = Entry(window)
e1.place(x=20, y=150)

label11 = Label(window, text="🍙Samosa", font="times 18", fg='white', bg='black')
label11.place(x=20, y=200)

e2 = Entry(window)
e2.place(x=20, y=230)

label12 = Label(window, text="🍕Pizza", font="times 18", fg='white', bg='black')
label12.place(x=20, y=280)

e3 = Entry(window)
e3.place(x=20, y=310)

label13 = Label(window, text="🍔Burger", font="times 18", fg='white', bg='black')
label13.place(x=20, y=360)

e4 = Entry(window)
e4.place(x=20, y=390)

label14 = Label(window, text="🍜Noodles", font="times 18", fg='white', bg='black')
label14.place(x=250, y=120)

e5 = Entry(window)
e5.place(x=250, y=150)

label15 = Label(window, text="☕Coffee", font="times 18", fg='white', bg='black')
label15.place(x=250, y=200)

e6 = Entry(window)
e6.place(x=250, y=230)

# Center the window on the screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
x = screen_width // 2 - size[0] // 2
y = screen_height // 2 - size[1] // 2
window.geometry(f"{size[0]}x{size[1]}+{x}+{y}")

# Execute calculate function after 1 second
window.after(1000, calculate)

# Closing the main loop
window.mainloop()