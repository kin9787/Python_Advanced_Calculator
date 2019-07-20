from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x580+0+0")

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = " "
        self.input_value =True
        self.check_sum =False
        self.op = " "
        self.result = False

    def number_enter(self, num):
        self.result = False
        first_num = text_display.get()
        second_num = str(num)
        if self.input_value:
            self.current = second_num
            self.input_value = False

        else:
            if second_num == ".":
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(text_display.get())

    def display(self, value):
        text_display.delete(0, END)
        text_display.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value =True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def maths_pm(self):
        self.result =  False
        self.current = -(float(text_display.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(text_display.get())))

    def cosh(self):
        self.result = False
        self.current = math.cos(math.radians(float(text_display.get())))

    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(text_display.get()))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(text_display.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(text_display.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(text_display.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(text_display.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(text_display.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(text_display.get()))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(text_display.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(text_display.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(text_display.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(text_display.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(text_display.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(text_display.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(text_display.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(text_display.get()))
        self.display(self.current)

added_value = Calc()



text_display = Entry(calc, font=('arial', 20, 'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
text_display.grid(row=0, column=0, columnspan=4, pady=1)
text_display.insert(0, "0")

numberpad = "789456123"
i = 0
button = []
for x in range(2, 5):
     for y in range(3):
         button.append(Button(calc, width=6, height=2, font=("arial", 20, "bold"), bd=4, text=numberpad[i]))
         button[i].grid(row=x, column=y, pady=1)
         button[i]["command"] = lambda x = numberpad[i]: added_value.number_enter(x)
         i += 1

#--------------------------------------------------- Standard ---------------------------------------------------------#

clear_button = Button(calc, text=chr(67), width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=added_value.clear_entry).grid(row=1, column=0, pady=1)

clear_all_button = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=added_value.all_clear_entry).grid(row=1, column=1, pady=1)

sqrt_button = Button(calc, text="√", width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=added_value.sqrt).grid(row=1, column=2, pady=1)

add_button = Button(calc, text="+", width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=lambda:added_value.operation("add")).grid(row=1, column=3, pady=1)

subtract_button = Button(calc, text="-", width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=lambda:added_value.operation("sub")).grid(row=2, column=3, pady=1)

mulitply_button = Button(calc, text="*", width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=lambda:added_value.operation("multi")).grid(row=3, column=3, pady=1)

divide_button = Button(calc, text=chr(247), width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=lambda:added_value.operation("divide")).grid(row=4, column=3, pady=1)

zero_button = Button(calc, text="0", width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=lambda:added_value.number_enter(0)).grid(row=5, column=0, pady=1)

dot_button = Button(calc, text=".", width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=lambda:added_value.number_enter(".")).grid(row=5, column=1, pady=1)

plus_minus_button = Button(calc, text=chr(177), width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=added_value.maths_pm).grid(row=5, column=2, pady=1)

equals_button = Button(calc, text="=", width=6, height=2, font=("arial", 20, "bold"), bd=4,
                      bg="powder blue", command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

#------------------------------------------------- Scientific ---------------------------------------------------------#


pi_button = Button(calc, text="n", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.pi).grid(row=1,
            column=4, pady=1)

cos_button = Button(calc, text="cos", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.cos).grid(row=1,
            column=5, pady=1)

tan_button = Button(calc, text="tan", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.tan).grid(row=1,
            column=6, pady=1)

sin_button = Button(calc, text="sin", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.sin).grid(row=1,
            column=7, pady=1)

pi_2_button = Button(calc, text="2n", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.tau).grid(row=2,
            column=7, pady=1)

cosh_button = Button(calc, text="cosh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.cosh).grid(row=2,
            column=4, pady=1)

tanh_button = Button(calc, text="tanh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="white", command=added_value.tanh).grid(row=2,
            column=5, pady=1)

sinh_button = Button(calc, text="sinh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="white", command=added_value.sinh).grid(row=2,
            column=6, pady=1)

log_button = Button(calc, text="log", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.log).grid(row=3,
            column=4, pady=1)

Exp_button = Button(calc, text="Exp", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="white",command=added_value.exp).grid(row=3,
            column=5, pady=1)

Mod_button = Button(calc, text="Mod", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="white", command=lambda:added_value.operation("mod")).grid(row=3,
            column=6, pady=1)

e_button = Button(calc, text="e", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.e).grid(row=3,
            column=7, pady=1)

log2_button = Button(calc, text="log2", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.log2).grid(row=4,
            column=4, pady=1)

deg_button = Button(calc, text="deg", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="white", command=added_value.degrees).grid(row=4,
            column=5, pady=1)

acosh_button = Button(calc, text="acosh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="white", command=added_value.acosh).grid(row=4,
            column=6, pady=1)

asinh_button = Button(calc, text="asinh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.asinh).grid(row=4,
            column=7, pady=1)

log10_button = Button(calc, text="log10", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.log10).grid(row=5,
            column=4, pady=1)

log1p_button = Button(calc, text="log1p", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="white", command=added_value.log1p).grid(row=5,
            column=5, pady=1)

expm1_button = Button(calc, text="expm1", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="white", command=added_value.expm1).grid(row=5,
            column=6, pady=1)

lgamma_button = Button(calc, text="Igamma", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue", command=added_value.lgamma).grid(row=5,
            column=7, pady=1)

label_display = Label(calc, text="Scientific Calculator", font=("arial", 30, "bold"), justify=CENTER)
label_display.grid(row=0, column=4, columnspan=4)

#---------------------------------------------------- MENU ------------------------------------------------------------#


def exit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confrim?")
    if iExit > 0:
        root.destroy()
        return


def standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")


def scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=standard)
filemenu.add_command(label="Scientific", command=scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy")
editmenu.add_command(label="Cut")
editmenu.add_separator()
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=helpmenu)
helpmenu.add_command(label="View Help")

for x in range(2, 5):
    print(x)

root.config(menu=menubar)
root.mainloop()

