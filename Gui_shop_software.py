from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk

root = Tk()
root.config(bg='#f3ca28')


item_dis = Label(font=('Calibri', 13), bg='orange', fg='gray17', width=20)
rights = Label(root, text="Copyright © 2021. All rights reserved by Md. Ishtiuk Ahammed.", font=('calibri', 8), bg='#f3ca28', fg='gray17')

shop = Image.open('shop.png')
shop_dis = ImageTk.PhotoImage(shop)
shop_pic = Label(image=shop_dis, bg='#f3ca28')
shop_txt = Label(text="FOOD Mart", bg='gray17', fg='cyan', font=('Calibri', 16), width=15)

img1 = Image.open('burger.png')
img2 = Image.open('candy.png')
img3 = Image.open('drink.png')
img4 = Image.open('potato.png')
img5 = Image.open('pizza.png')
img6 = Image.open('cola.png')

img1_dis = ImageTk.PhotoImage(img1)
img2_dis = ImageTk.PhotoImage(img2)
img3_dis = ImageTk.PhotoImage(img3)
img4_dis = ImageTk.PhotoImage(img4)
img5_dis = ImageTk.PhotoImage(img5)
img6_dis = ImageTk.PhotoImage(img6)


image1 = Label(image=img1_dis, bg='#f3ca28')
image2 = Label(image=img2_dis, bg='#f3ca28')
image3 = Label(image=img3_dis, bg='#f3ca28')
image4 = Label(image=img4_dis, bg='#f3ca28')
image5 = Label(image=img5_dis, bg='#f3ca28')
image6 = Label(image=img6_dis, bg='#f3ca28')


shop_button = Image.open('buy.png')
cart = Image.open('cart.png')
cart_disp = ImageTk.PhotoImage(cart)
cart_pic = Label(image=cart_disp, bg='#f3ca28')
entry_nm = Label(text="Product Name : ", font=('Calibri', 10), bg='gray17', fg='white', width=12)
entry_qua = Label(text="Quantity : ", font=('Calibri', 10), bg='gray17', fg='white', width=12)
entry_item = Entry(bd=2, font=('Calibri', 11))
entry_quantity = Entry(bd=2, font=('Calibri', 11))
text_payment = Label(text="Pay Here: $", font=('Calibri', 11), bg='gray17', fg='white', width=12)
payment_input = Entry(bd=2, width=20, font=('Calibri', 11), fg='black')
reday_button_shop = ImageTk.PhotoImage(shop_button)
amount = Label(root, font=('Calibri', 13), bg='gray17', fg='white', width=29, height=5)
cart_customer = Label(root, font=('Calibri', 13), bg='gray17', fg='white', width=29, height=5)
changers_customrer = Label(root, font=('Calibri', 12), bg='grey', fg='white', width=33)

class Shop_management_Structure_Software:
    def __init__(self, prducts_lst, product_X_price, product_with_Stock):
        self.products = prducts_lst
        self.products_price = product_X_price
        self.products_Stock = product_with_Stock
        self.customer_cart = []

        self.total_cost = 0

    def buy(self, product_nm, quantity):
        self.product_nm = product_nm
        self.quantity = quantity

        if self.quantity == 'str_invalid':
            self.output = "Invalid Quantity!\nQuantity must me Number"

        elif self.product_nm in self.products and self.quantity <= self.products_Stock[self.product_nm]:            
            self.total_cost = self.products_price[self.product_nm] * self.quantity
            if self.total_cost > 0:
                self.output = f"Please pay: {self.total_cost} USD"
            else:
                self.output = "No Payment\nSelect Quantity to buy"  
            text_payment.place(x=213, y=410)
            payment_input.place(x=322, y=410)
            pay_now_butt.place(x=260, y=443)
            clear_button = Button(text="Clear All", font=('Calibri', 13), bg='green', fg='white', bd=5, width=28, command=Shop.clear_All).place(x=220, y=652)

        elif len(self.product_nm) == 0:
            self.output = "Please input Product Name"

        elif self.product_nm in self.products and self.quantity > self.products_Stock[self.product_nm]:
            self.output = "Sorry Sir. We are out of Stock!\nPlease wait for 5 seconds\n\nRestocking..."
            self.restocker()

        else:
            self.output = 'Sorry, Sir.\nThis product is currently\nunavailble!'
                                   
        amount.config(text=self.output)
        amount.place(x=220, y=280)

    def check_out(self, payment):

        if self.total_cost == 0:
            self.output_pay = "Sorry\nYou didn't buy anything\nNo payment is required."
        elif payment == 'string_invalid':
            self.output_pay = f"Sorry, Sir\nPlease pay correctly."
        elif payment >= self.total_cost:
            self.products_Stock[self.product_nm] -= self.quantity
            self.customer_cart.append(self.product_nm)
            self.output_pay = f"Successfully Paid, Sir.\n\nYou've got: {self.quantity} {self.customer_cart}"
            if payment > self.total_cost:
                self.changes = payment - self.total_cost
                self.change_out = f"Here's your return: {round(self.changes, 2)} USD"
                changers_customrer.config(text=self.change_out)
                changers_customrer.place(x=220, y=620)
            self.total_cost = 0

        elif payment < self.total_cost:
            self.output_pay = f"Sorry, Sir\nPlease pay: {self.total_cost} USD\nAnd try again."
        elif payment == 'string_invalid':
            self.output_pay = "Payment Must be Number"
        else:
            self.output_pay = "Unexpected Error\nPlease try again"
        cart_customer.config(text=self.output_pay)
        cart_customer.place(x=220, y=500)
        cart_pic.place(x=520, y=495)
        self.customer_cart = []

    def restocker(self):
        for products in self.products_Stock:
            crnt_stk = self.products_Stock[products]

            if crnt_stk == 0:
                self.products_Stock[products] += 15
                print('Restocking..! Stock Updated')

    def displayer(self):
        self.lsting = '''Product List:
 _____________________\n'''

        for key in self.products_price:
            self.lsting += f"{key} || Price: {self.products_price[key]} USD\n"

        item_dis.config(text=self.lsting)

    def clear_All(self):
        amount.config(text='')
        cart_customer.config(text='')
        changers_customrer.config(text='')


products = ['candy', 'chips', 'juice', 'pizza', 'burger', 'cake', 'cola']
products_price = {'candy': 2, 'chips': 10, 'juice': 18, 'pizza': 70, 'burger': 30, 'cake': 60, 'cola': 25}
products_stock = {'candy': 50, 'chips': 20, 'juice': 20, 'pizza': 25, 'burger': 35, 'cake': 15, 'cola': 30}

Shop = Shop_management_Structure_Software(products, products_price, products_stock)

def passing_to_buy():
    nm = entry_item.get().lower()
    quan = entry_quantity.get()
    try:
        quan = int(quan)
    except:
        quan = 'str_invalid'
        pass
    Shop.buy(nm, quan)

next_button = Button(text='NEXT', font=('Calibri', 11), bg='green', fg='white', bd=5, width=19, command=passing_to_buy)

def inp():
    entry_nm.place(x=240, y=174)
    entry_item.place(x=327, y=173)
    entry_qua.place(x=240, y=200)
    entry_quantity.place(x=327, y=199)
    next_button.place(x=270, y=230)

    image1.place(x=510, y=180)
    image2.place(x=510, y=250)
    image6.place(x=510, y=320)
    image3.place(x=620, y=180)
    image4.place(x=620, y=250)
    image5.place(x=620, y=320)

def check_out():
    amount = payment_input.get()
    try:
        amount = float(amount)
    except:
        amount = 'string_invalid'
        pass
    Shop.check_out(amount)

button_shop = Button(image=reday_button_shop, bg='yellow', bd=8, command=inp)

butt = Button(text='Display Products', font=('Calibri', 13), bg='red', fg='white', bd=5, width=19, command=Shop.displayer)
pay_now_butt = Button(text='Pay Now', font=('Calibri', 13), bg='green', fg='white', bd=5, width=19, command=check_out)

try:
    timing = Label(root, font=("DS-digital", 20), bg='gray17', fg='red', width=10)
    def time_update():
        tm = datetime.now().strftime("%I: %M: %S %p")
        timing.config(text=tm)
        timing.after(900, time_update)

    timing.place(x=30, y=5)
except:
    pass

exit_button = Button(text='EXIT', font=('Calibri', 13), bg='#f73838', fg='white', bd=5, width=13, command=root.destroy).place(x=550, y=651)
shop_pic.place(x=520, y=5)
shop_txt.place(x=480, y=120)
butt.place(x=20, y=100)
button_shop.place(x=315, y=60)
item_dis.place(x=20, y=140)
rights.place(x=450, y=700)


time_update()
root.geometry('760x720')
root.mainloop()


