import os
import tkinter
from tkinter import *
from tkinter import messagebox

from logic.calculator import Calculate
from logic.initializer import Initializer


class GuiApp:

    def __init__(self):
        self.initializer = Initializer()
        self.calculator = Calculate()
        self.ico_image = os.path.join(os.getcwd(), "images", "romanic.ico")

    def control_radio_button_labels(self, value_selected):
        label_entry["text"] = ""
        if value_selected.get() == 1:
            label_entry["text"] = "Romanic number"
            entry_value["state"] = tkinter.NORMAL
            entry_value.delete(0, tkinter.END)
            button_conversion["bg"] = "#10611A"
            button_romanic_to_decimal["bg"] = "#74C454"
            buton_decimal_to_romanic ["bg"] = "#A82232"
            label_result["text"] = ""
        elif value_selected.get() == 2:
            label_entry["text"] = "Decimal number"
            entry_value["state"] = tkinter.NORMAL
            entry_value.delete(0, tkinter.END)
            button_conversion["bg"] = "#10611A"
            button_romanic_to_decimal["bg"] = "#A82232"
            buton_decimal_to_romanic["bg"] = "#74C454"
            label_result["text"] =""
        else:
            label_entry["text"] = ""
            entry_value.delete(0, tkinter.END)
            entry_value["state"] = tkinter.DISABLED
            button_conversion["bg"] = "#A82232"
            button_romanic_to_decimal["bg"] = "#A82232"
            buton_decimal_to_romanic["bg"] = "#A82232"
            label_result["text"] = ""

    def calculate_conversion(self, value_selected):
        if value_selected.get() == 0:
            messagebox.showerror("NO SELECTION", "Please choose the type of conversion you want")
            return
        if entry_value.get() == "":
            if value_selected.get() == 1:
                messagebox.showerror("NO INPUT WRITTEN", "Please provide a romanic  number")
                return
            elif value_selected.get() == 2:
                messagebox.showerror("NO INPUT WRITTEN", "Please provide a decimal number")
                return
        #start calculating
        if value_selected.get() == 1:
            #romanic to decimal
            result = self.calculator.convert_romanic_number(entry_value.get())
            label_result["text"] = result[1]
        elif value_selected.get() == 2:
            #need to transform it in a int -> done in initializer
            if not entry_value.get().isnumeric():
                messagebox.showerror("NOT A NUMBER","You must introduce a number")
                return
            result = self.calculator.convert_decimal_number(int(entry_value.get()))
            label_result["text"] = result[1]






    def create_main_logic(self, window):
        global button_romanic_to_decimal
        global buton_decimal_to_romanic
        global button_romanic_to_decimal_var
        global button_decimal_to_romanic_var
        global label_entry
        global entry_value
        global button_conversion
        global label_result

        selection = IntVar()
        frame_title = LabelFrame(window, text="Romanic Converter", width=500, height=400, cursor="arrow", bg="#D6B17A",
                                 fg="#FFF9ED", relief="groove", font=("Georgia", 12, "bold"), labelanchor=tkinter.N)
        frame_title.place(x=50, y=55)

        label_welcome = Label(frame_title,
                              text="A romanic converter app\nPlease choose the type of conversion you want",
                              font=("Georgia", 10, "bold"), bg="#D6B17A", fg="#0A0700", relief="flat", cursor="arrow",
                              justify="center")
        label_welcome.place(x=75, y=20)
        # insert radiobuttons
        frame_checkboxes = LabelFrame(frame_title, text="Conversion method", width=400, height=100, cursor="arrow",
                                      bg="#D6B17A",
                                      fg="#FFF9ED", relief="ridge", font=("Georgia", 10, "bold"),
                                      labelanchor=tkinter.NW)
        frame_checkboxes.place(x=50, y=100)
        button_romanic_to_decimal = Checkbutton(frame_checkboxes, text="Romanic to decimal", variable=selection,
                                                onvalue=1, bg="#A82232", font=("Arial", 10, "italic"), fg="#0A0700",
                                                relief="raised",
                                                command=lambda: self.control_radio_button_labels(selection))

        button_romanic_to_decimal.place(x=25, y=30)
        button_romanic_to_decimal.deselect()
        buton_decimal_to_romanic = Checkbutton(frame_checkboxes, text="Decimal to romanic",
                                               variable=selection,
                                               onvalue=2, bg="#A82232",
                                               font=("Arial", 10, "italic"), fg="#0A0700", relief="raised",
                                               command=lambda: self.control_radio_button_labels(selection))
        buton_decimal_to_romanic.place(x=230, y=30)
        buton_decimal_to_romanic.deselect()

        # frame inserted text
        frame_entry = LabelFrame(frame_title, text="EntryBox", width=400, height=80, cursor="arrow", bg="#D6B17A",
                                 fg="#FFF9ED", relief="groove", font=("Georgia", 10, "bold"), labelanchor=tkinter.NW)
        frame_entry.place(x=50, y=200)
        label_entry = Label(frame_entry, text="", bg="#D6B17A", fg="#0A0700", relief="flat",
                            font=("Georgia", 10, "bold"), justify="center", bd=3)
        label_entry.place(x=20, y=10)
        # entry text
        entry_value = Entry(frame_entry, width=20, font=("Georgia", 10, "bold"), bg="#5F87B0", fg="#FFF9ED",
                            justify="center", state="disabled", relief="raised")
        entry_value.place(x=180, y=10)

        # frame result
        frame_result = LabelFrame(frame_title, text="ResultBox", width=400, height=90, cursor="arrow", bg="#D6B17A",
                                  fg="#FFF9ED", relief="groove", font=("Georgia", 10, "bold"), labelanchor=tkinter.NW)
        frame_result.place(x=50, y=280)
        button_conversion = Button(frame_result, text="Convert", bg="#A82232", bd=5, fg="#FFF9ED", relief="raised",
                                   justify="center", font=("Georgia", 10, "bold"), cursor="arrow",
                                   command = lambda : self.calculate_conversion(selection))
        button_conversion.grid(row=1, column=0, padx=159)
        label_result = Label(frame_result, text="", bg="#D6B17A", fg="#0A0700", relief="flat",
                            font=("Georgia", 12, "bold"), justify="center", bd=5)
        label_result.grid(row=0, column=0, padx=159)

    def create_main_gui(self):
        root = Tk()
        root.title("Romanic Converter")
        root.geometry("600x500")
        root.iconbitmap(self.ico_image)
        root["bg"] = "#5F87B0"
        self.create_main_logic(root)
        root.resizable(False, False)
        root.mainloop()
