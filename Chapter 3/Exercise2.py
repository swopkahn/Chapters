from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def update_order():
    coffee = coffee_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()
    messagebox.showinfo('Order', f"Your order is a {coffee} with {sugar} sugar and {milk} milk.")

#Main Frame

root = Tk()
root.title("Coffee Vending Machine")
root.resizable(False, False)
root.configure(bg="#EEC8A1")

# Frame
frame = Frame(root, bg="#EEC8A1")  # Set the background color for the frame
frame.pack(padx=0, pady=0)  # Set padx and pady to 0

# Title
title = Label(frame, text="Panda Cafe", fg="black", font=("Helvetica", 15, "bold"), bg="#EEC8A1")  # Set the background color for the label
title.pack(padx=0, pady=10)  # Set pady to 0

# Coffee
coffee_var = StringVar()

coffee_label = Label(frame, text="-----DRINKS-----", fg="black", font=("Helvetica", 12, "bold"), bg="#EEC8A1")  # Set the background color for the label
coffee_label.pack(padx=0, pady=10)  # Set pady to 0

# Espresso
img1 = Image.open("French Press.png")
espresso = ImageTk.PhotoImage(img1.resize((100, 100)))

espresso_label = Label(frame, image=espresso, bg="#EEC8A1")  # Set the background color for the label
espresso_label.pack(side="left", padx=0)

espresso_text = Radiobutton(frame, text="French Press", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var,
                            value="french press", bg="#EEC8A1")  # Set the background color for the radiobutton
espresso_text.pack(side="left", padx=0)

#Latte

img2 = Image.open("Espresso.png")
latte = ImageTk.PhotoImage(img2.resize((100,100)))

latte_label = Label(frame, image=latte, bg="#EEC8A1")
latte_label.pack(side="left", padx=10)

latte_text = Radiobutton(frame, text="Espresso", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="espresso", padx=10, bg="#EEC8A1")
latte_text.pack(side="left")

#Cappuccino

frame2 = Frame(root, bg="#EEC8A1")
frame2.pack(padx=10)

img3 = Image.open("Latte.png")
cap = ImageTk.PhotoImage(img3.resize((100,100)))

cap_label = Label(frame2, image=cap, bg="#EEC8A1")
cap_label.pack(side="left", padx=10)

cap_text = Radiobutton(frame2, text="Latte", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="latte", bg="#EEC8A1")
cap_text.pack(side="left")

#Mocha

img4 = Image.open("Chemex.png")
mocha = ImageTk.PhotoImage(img4.resize((100,100)))

mocha_label = Label(frame2, image=mocha, bg="#EEC8A1")
mocha_label.pack(side="left")

mocha_text = Radiobutton(frame2, text="Chemex", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="chemex", bg="#EEC8A1")
mocha_text.pack(side="left", padx=20)

#Sugar

frame3 = Frame(root, bg="#EEC8A1")
frame3.pack()

sugar_var = StringVar()

sugar_label = Label(frame3, text="-------SUGAR-------", fg="black", font=("Helvetica", 12, "bold"), padx=10, pady=10, bg="#EEC8A1")
sugar_label.pack(padx=142, pady=20)

zero = Radiobutton(frame3, text="0%", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="no", bg="#EEC8A1")
zero.pack(side="left", padx=20)

twenty_five = Radiobutton(frame3, text="25%", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="25%", bg="#EEC8A1")
twenty_five.pack(side="left", padx=20)

fifty = Radiobutton(frame3, text="50%", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="50%", bg="#EEC8A1")
fifty.pack(side="left", padx=20)

seventy_five = Radiobutton(frame3, text="75%", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="75%", bg="#EEC8A1")
seventy_five.pack(side="left", padx=20)

#Milk

frame4 = Frame(root, bg="#EEC8A1")
frame4.pack()

milk_var = StringVar()

milk_label = Label(frame4, text="-------MILK-------", fg="black", font=("Helvetica", 12, "bold"), padx=10, pady=10, bg="#EEC8A1")
milk_label.pack(padx=20, pady=20)

skimmed = Radiobutton(frame4, text="Whole", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="skimmed", bg="#EEC8A1")
skimmed.pack(side="left", padx=20)

almond = Radiobutton(frame4, text="Organic", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="almond", bg="#EEC8A1")
almond.pack(side="left", padx=12)

oat = Radiobutton(frame4, text="Lactose-Free", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="oat", bg="#EEC8A1")
oat.pack(side="left", padx=12)

low_fat = Radiobutton(frame4, text="Low Fat", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="low fat", bg="#EEC8A1")
low_fat.pack(side="left", padx=20)

#Order

frame5 = Frame(root, bg="#EEC8A1")
frame5.pack()

order_button = Button(frame5, text="ORDER", bg="#C4A484",fg="black", font=("Helvetica", 12, "bold"), padx= 10, pady=5, bd=0, command= update_order)
order_button.pack(padx=169, pady=10)

order_text = Label(frame5, text="", font=("Helvetica", 10), bg="#EEC8A1")
order_text.pack(pady=10)


root.mainloop()