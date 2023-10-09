import tkinter as tk
from tkinter import ttk
import format as fm
import check_code as cc
import cr_dm_code as dm
from PIL import ImageTk, Image
import code_print as pr
import check_db as gc
import os
from tkinter.messagebox import askyesno
from datetime import datetime


# create window class
class Window:
    """
    Window is a class who creates the GUI for the program "QR_Code_Printer".
    The window contains entrys and dropdonwmenus for choosing the pcb number.
    by click on "Create" the dm-code is saved in the folder "qr_codes".
    by click on "Print" the last generated code will be printed from the folder "qr_codes".
    by click on "Reset" the window will be set to start condition if clicked after create a code,
    the code will be deleted from "qr_codes".

    Inputs:
    entry_matnum (Entry): enter Material Number;
    entry_fs (Entry): enter Function Stand;
    dropd_manu (OptionMenu): choose Manufacturer;
    dropd_year (OptionMenu): choose Manufacturer Year;
    dropd_month (OptionMenu): choose Manufacturer Month;
    entry_serialnum (Entry): enter Serial Number;
    entry_repetition (Entry): insert print repetition;
    checkbox (checkbox): check for automatically use the next serial number of this pcb

    Outputs:
    label_dmcode (Label): show created dm-code-img;
    label_inserted (Label): show entered dm-code;
    label_error (Label): show error messages
    """

    # init for class Application
    def __init__(self, root):
        self.root = root

        # set window size
        self.root.geometry("720x300+400+100")

        # set window title
        self.root.title("QR-Code Printer")

        # set window icon
        self.root.iconbitmap("RD_FILES\\RD_QR_CODE_PRINTER\\printer_blue_10877.ico")

        self.current_date = datetime.now()
        self.current_year = str(self.current_date.year)

        # call the function 'close_window' when closing the window.
        self.root.protocol('WM_DELETE_WINDOW', self.close_window)

        # initialize the variable 'print_double' with None for later use
        self.print_double = None
        self.code_str = ""
        self.created_codes = []

        # create and place labels on the window
        # material number label
        self.label_matnum = tk.Label(self.root, text="Material Number:")
        self.label_matnum.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        # function stand label
        self.label_fs = tk.Label(self.root, text="Function Stand:")
        self.label_fs.grid(row=2, column=1, padx=5, pady=5, sticky="e")

        # manufacturer label
        self.label_manu = tk.Label(self.root, text="Manufacturer:")
        self.label_manu.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        # date label
        self.label_date = tk.Label(self.root, text="Manufacturer Date:")
        self.label_date.grid(row=4, column=1, padx=5, pady=5, sticky="e")

        # serial number label
        self.label_serialnum = tk.Label(self.root, text="Serial Number:")
        self.label_serialnum.grid(row=5, column=1, padx=5, pady=5, sticky="e")

        # serial number label
        self.label_auto_serial = tk.Label(self.root, text="Automatic Serial Nr:")
        self.label_auto_serial.grid(row=6, column=1, padx=5, pady=5, sticky="e")

        # inserted code label
        self.label_inserted = tk.Label(self.root)
        self.label_inserted.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        # label to show errors
        self.label_error = tk.Label(self.root, width=20)
        self.label_error.grid(row=7, column=4, sticky="w", padx=5, pady=5)

        # label to show the created dm code
        self.code_std = ImageTk.PhotoImage(Image.open(f"RD_FILES\\RD_QR_CODE_PRINTER\\dm_code_label.jpg"))
        self.label_dmcode = tk.Label(self.root, image=self.code_std)
        self.label_dmcode.grid(row=2, column=4, rowspan=4, columnspan=2, padx=5, pady=5, sticky="w")

        # placeholder label
        self.label_placeh = tk.Label(self.root, text="    ")
        self.label_placeh.grid(row=0, column=0)

        # placeholder label
        self.label_repetition = tk.Label(self.root, text="Print repetition:")
        self.label_repetition.grid(row=8, column=2, columnspan=2, sticky="w")

        # create and place entrys on the window
        # entry to insert the material number
        self.entry_matnum = tk.Entry(self.root)
        self.entry_matnum.grid(row=1, column=2, padx=5, pady=5, columnspan=2, sticky="w")

        # entry to insert the function stand
        self.entry_fs = tk.Entry(self.root)
        self.entry_fs.grid(row=2, column=2, padx=5, pady=5, columnspan=2, sticky="w")

        # entry to inserting the serial number
        self.entry_serialnum = tk.Entry(self.root)
        self.entry_serialnum.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky="w")

        # entry to inserting the print repetition
        self.entry_repetition = tk.Entry(self.root, width=4)
        self.entry_repetition.grid(row=8, column=2, padx=5, pady=5, columnspan=2, sticky="e")
        self.entry_repetition.insert(0, "1")

        # create and place dropdown menus on the window
        # dropdownmenu to choose the manufacturer
        # define a list which contains the choices
        self.manufacturer = ["SKL", "SBPO", "SFDT", "SRD"]
        # devine variable for selection and set default value
        self.selected_manufacturer = tk.StringVar(root)
        self.selected_manufacturer.set(self.manufacturer[0])
        # create dropdownmenu and place on the window
        self.dropd_manu = tk.OptionMenu(root, self.selected_manufacturer, *self.manufacturer)
        self.dropd_manu.grid(row=3, column=2,columnspan=2, sticky="w")

        # dropdownmenu to choose the manufacturer_year
        # define a list which contains the choices
        self.year = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021",
                     "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029"]
        # devine variable for selection and set default value
        self.selected_year = tk.StringVar(root)
        self.selected_year.set(self.current_year)
        # create dropdownmenu and place on the window
        self.dropd_year = tk.OptionMenu(root, self.selected_year, *self.year)
        self.dropd_year.grid(row=4, column=2, sticky="w")

        # dropdownmenu to choose the manufacturer_month
        # define a list which contains the choices
        self.month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        # devine variable for selection and set default value
        self.selected_month = tk.StringVar(root)
        self.selected_month.set(self.month[0])
        # create dropdownmenu and place on the window
        self.dropd_month = tk.OptionMenu(root, self.selected_month, *self.month)
        self.dropd_month.grid(row=4, column=3, sticky="w")

        # list for the most needed pcbs
        self.pcb_list = ["ZTCCU-CM_IN inside contr. module pcba","ZTCCU-CB_IN inside conn. board pcba",
                         "ZTCCU-CAP_IN inside cap. module pcba","ZTCCU-CM_OUT outside contr. module pcba",
                         "ZTCCU-CB_OUT outside conn. board pcba","ZTSCU-CB Connection Board assem.","PCBA ZTSCU",
                         "PCBA forcer_Z-axis_Mozart","PCBA Light Barrier Z-Down Mozart assem.","Mozart KE Rotor PCBA",
                         "Mozart KE Stator PCBA","Mozart KD Rotor PCBA","Mozart KD Stator PCBA",
                         "Intermediate Adapter Mozart PCBA","RCU-CME Controller Module cpl.","RCU-PME_XXX(CS) PCBA",
                         "RCU-PME_SH50_SH15(PS) PCBA","RCU-PME_DH10(PS) PCBA","RCU-PME_TG75(CS) PCBA",
                         "RCU-PME_TG75(PS) PCBA","Link Aggregator PCBA","Universal Head Interface London PCBA",
                         "Universal Head Adapter London PCBA"]

        # dropdownmenu to choose the pcb
        self.dropd_pcb = ttk.Combobox(root, values=self.pcb_list, width=50, state="readonly")
        self.dropd_pcb.grid(row=1, column=4, sticky="w", padx=5, pady=5)
        self.dropd_pcb.bind("<<ComboboxSelected>>", self.select_pcb)

        # create buttons and place them on the window
        # button to create the dm code
        self.button_create = tk.Button(root, text="Create", width=10, command=self.create)
        self.button_create.grid(row=8, column=1, sticky="w", padx=5, pady=5, columnspan=5)

        # button to print the dm code
        self.button_print = tk.Button(root, text="Print", width=10, state="disabled", command=self.print)
        self.button_print.grid(row=8, column=1, columnspan=5, sticky="s", padx=5, pady=5)

        # button to reset the window
        self.button_reset = tk.Button(root, text="Reset", width=10, command=self.reset)
        self.button_reset.grid(row=8, column=1, sticky="e", padx=5, pady=5, columnspan=5)

        # checkbox for the automatic serial number assignment
        self.checkbox_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(root, variable=self.checkbox_var)  # , command=self.checkbox_clicked)
        self.checkbox.grid(row=6, column=2, sticky="w")

    # function to create the dm-code
    def create(self):
        """
        creates a dm-code based on the user input.It checks for errors in the input and displays them on the
        "label_error". if no errors are found, it creates a dm code img and display it on "label_dmcode".
        updates button states.

        Args:
        None

        Returns:
        None
        """

        # reset the label color
        self.label_matnum.config(fg="black")
        self.label_matnum.update()
        self.label_fs.config(fg="black")
        self.label_fs.update()
        self.label_serialnum.config(fg="black")
        self.label_serialnum.update()


        # transforming date into 2-digit code by calling format_date function
        date = fm.format_date(f"{self.selected_year.get()}{self.selected_month.get()}")

        # create list with code values
        self.code = [self.entry_matnum.get(), self.entry_fs.get(), self.selected_manufacturer.get(),
                     date, self.entry_serialnum.get()]

        # write checkbox return value into variable
        self.checkbox_variable = self.checkbox_var.get()

        # check if auto serial number checkbox is activated
        if self.checkbox_variable:

            # overwrite "self.code" with the new automatically generated code
            self.code[4] = gc.auto_serialnum([self.code[0], self.code[1], self.code[2][1:], self.selected_year.get(),
                                             self.selected_month.get()])

            # set the "self.entry_serialnum" to the new auto generated serial number
            self.entry_serialnum.delete(0, tk.END)
            self.entry_serialnum.insert(0, f"{self.code[4]}")

        # delete the content of the "self.created_codes" list
        self.created_codes.clear()

        # check and write the wished repetitions, into the variable "repetition"
        repetition = cc.check_repetition(self.entry_repetition.get())

        # create strings for the
        self.dbcode = f"{self.code[0]}-{self.code[1]}-{self.code[2]}-{self.code[3]}-{self.code[4]}"
        self.code_str = f"1P{self.code[0]}-{self.code[1]}-{self.code[2]}-{self.code[3]}-{self.code[4]}"

        # loop to create all needed QR codes
        for number in range(repetition):
            # check the code format before transform into a dm-code-img
            errors = self.code.copy()
            errors = cc.check_code(errors)



            # error material number
            if errors[0] is not None:
                # print error description on error label set material-number-label-color to red
                self.label_error.config(fg="red", text=f"{errors[0]}")
                self.label_error.update()
                self.label_matnum.config(fg="red")
                self.label_matnum.update()
                break

            # error function stand
            elif errors[1] is not None:
                # print error description on error label set function-stand-label-color to red
                self.label_error.config(fg="red", text=f"{errors[1]}")
                self.label_error.update()
                self.label_fs.config(fg="red")
                self.label_fs.update()
                break

                # error serial number
            elif errors[4] is not None:
                # print error description on error label set serial-number-label-color to red
                self.label_error.config(fg="red", text=f"{errors[4]}")
                self.label_error.update()
                self.label_serialnum.config(fg="red")
                self.label_serialnum.update()
                break

            else:
                # call the function "dm_code_gen" to create the dm-code-img
                dm.dm_code_gen(self.code_str)
                self.created_codes.append(self.code_str)

                # set the button state for the next step, where the dm-code is ready to get printed
                self.button_create.config(state="disabled")
                self.button_print.config(state="normal")

                # paste img in the dm_code label on the window
                self.code_img = ImageTk.PhotoImage(Image.open(f"NEW_QR_CODES\\{self.code_str}.jpg"))
                self.label_dmcode.config(image=self.code_img)
                self.label_dmcode.update()

                # write the dm-code in the "inserted"-label for showing the entered code
                self.label_inserted.config(fg="green",text=f"{self.code_str}")
                self.label_inserted.update()

                # print out "created" in the error label with green color
                self.label_error.config(fg="green", text=f"Created")
                self.label_error.update()

                # set the checkbox and the entry state for the next step
                self.checkbox.config(state="disabled")
                self.checkbox.update()
                self.entry_repetition.config(state="disabled")
                self.entry_repetition.update()
                self.dropd_pcb.config(state="disabled")
                self.dropd_pcb.update()

            # in the last loop the if
            if not (number == (repetition - 1)):
                self.code_str = cc.next_serial(self.code_str)

    # function to print the dm-code
    def print(self):
        """
        This function checks the database for an existing PCB. If the searched PCB does not exist, the created DM-code
        image will be printed. If the code is already in the database, an error message is shown on the "label_error"
        and the saved DM-code image will be deleted.

        Args:
        None

        Returns:
        None
        """

        # loop for repetition of the printing function
        for element in self.created_codes:

            # call the function "GetQRCodeFromDB" to check if the entered code already exists in the database
            if not gc.GetQRCodeFromDB(f"{self.code[0]}_{self.code[1]}_{self.code[2]}_{self.code[3]}_{element[-4:]}"):

                # call function "codeprint" to print the created qr-code-img
                pr.codeprint(element)

        # if code already exists in database
            else:
                # set error label to "PCB already exist" and color to red
                self.label_error.config(fg="red", text="PCB already exist")
                self.label_error.update()

                # write the dm-code in the "inserted"-label for showing the entered code in red
                self.label_inserted.config(fg="red",text=f"{element}")
                self.label_inserted.update()

                # open funktion to create a popup window for duplicated codes
                self.popupwindow()

                # if "Yes" in the popup window, the code is going to get printed
                if self.print_double is not None:
                    pr.codeprint(element)

        # set button state for next-state
        self.button_print.config(state="disabled")
        self.button_print.update()
        self.button_create.config(state="normal")
        self.button_create.update()
        self.checkbox.config(state="normal")
        self.checkbox.update()
        self.entry_repetition.config(state="normal")
        self.entry_repetition.update()
        self.dropd_pcb.config(state="normal")
        self.dropd_pcb.update()

    # function to reset the inputs
    def reset(self):
        """
        This function try to delete the last generated dm_code image from the folder "qr_codes".
        if there is no, after the last start of the program, created dm_code image the program goes on.
        next step is to call the "delete_widgets" function.

        Args:
        None

        Returns:
        None
        """
        try:
            for element in self.created_codes:
                # delete the qr-code-img
                os.remove(f"NEW_QR_CODES\\{element}.jpg")
        except:
            pass

        # call function "delete_widgets" to bring the window to its initial state
        self.delete_widgets()

        # set button-states for next usage
        self.button_print.config(state="disabled")
        self.button_print.update()
        self.button_create.config(state="normal")
        self.button_create.update()
        self.checkbox.config(state="normal")
        self.checkbox.update()
        self.entry_repetition.config(state="normal")
        self.entry_repetition.update()
        self.dropd_pcb.config(state="normal")

    # function to delete the window widgets
    def delete_widgets(self):
        """
          This function try to delete the active widgets and call the __init__() method
           to recreate the window and start new.

          Args:
          None

          Returns:
          None
          """

        # reset widgets
        self.label_error.config(text="")
        self.label_error.update()
        self.label_matnum.config(fg="black")
        self.label_matnum.update()
        self.label_fs.config(fg="black")
        self.label_fs.update()
        self.label_serialnum.config(fg="black")
        self.label_serialnum.update()
        self.label_dmcode.config(image=self.code_std)
        self.label_dmcode.update()

        # delete the entrys
        self.entry_fs.delete(0, "end")
        self.entry_matnum.delete(0, "end")
        self.entry_serialnum.delete(0, "end")

        # reset the dropdownmenus
        self.selected_year.set(self.current_year)
        self.selected_month.set(self.month[0])
        self.selected_manufacturer.set(self.manufacturer[0])


    def popupwindow(self):
        """
        Displays a popup window that informs the user that a particular PCB code already exists in the database.
        If the user clicks the "Yes" button, the PCB code is set to be printed.
        If the user clicks the "No" button, the PCB code is not printed, the popup window is closed.

        Args:
        None

        Returns:
        None
        """

        # create a toplevel window named "popup" and lock the main window
        popup = tk.Toplevel()
        popup.grab_set()

        # set popup window position depend on the main window
        x = self.root.winfo_x()-40
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 30
        popup.geometry(f"500x100+{x}+{y}")

        # function for button "Yes"
        def button_yes():
            """
            if button "Yes" was pressed, the variable "print_double" is set to "1". The main Window is unlocked and
            the function "delete_popup" is called

            args:
            None

            return:
            None
            """

            # set "print_double" to "1"
            self.print_double = 1

            # call function "delete_popup"
            delete_popup()


        def button_no():
            """
            If the "No" button is pressed, the "print_double" variable is set to None, the main window is unlocked,
            and the "delete_popup" function is called.

            args:
            None

            return:
            None
            """
            # set "print_double" to None
            self.root.print_double = None

            # call function "delete_popup"
            delete_popup()


        def delete_popup():
            """
            This function is called to delete the popup window, remove all its contents from the GUI and
            unlocks the main window.

            Args:
            None

            Returns:
            None.
            """

            # unlock the main window
            popup.grab_release()

            # forget widgets on the popup window
            self.label_popup.grid_forget()
            button_yes.grid_forget()
            button_no.grid_forget()

            # destroy popup window
            popup.destroy()

        # create the widgets on the popup window
        # create and place the information text label on the window
        self.label_popup = tk.Label(popup, text="The entered PCB code already exists in the database. \n"
                                                     "Please press 'No' and try again.\n"
                                                     "If you want to reprint an already scanned code, please press "
                                                     "'Yes' to continue")
        self.label_popup.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        # create and place a placeholder label on the window
        self.label_placeh = tk.Label(popup, text="       ")
        self.label_placeh.grid(row=0, column=0,  padx=5, pady=5)

        # create and place the "Yes" button on the window
        button_yes = tk.Button(popup, text="Yes", command= button_yes, width=20)
        button_yes.grid(row=1, column=1, padx=5, pady=5)

        # create and place the "No" button on the window
        button_no = tk.Button(popup, text="No", command= button_no, width=20)
        button_no.grid(row=1, column=2, padx=5, pady=5)

        # wait for a interaction to return the programm
        popup.wait_window()

    def close_window(self):
        """
        Asks the user if they want to close the PCB database application. If the user selects "Yes",
        the application window is destroyed.

        Args:
        None

        Returns:
        None
        """

        # if the value is yes/True the window will close
        if askyesno(title='Close Pcb Database', message='Are you sure want to close the Database Application?'):

            # this destroys the window
            self.root.destroy()

    def select_pcb(self, event=None):
        """
        this function is called by choosing a pcb in th dropdown menu. material number and function stand are
        automatically inserted into their entry's.
        """
        # get the selected pcb name
        selected_pcb = self.dropd_pcb.get()

        # check for the correct material and function stand
        if selected_pcb == self.pcb_list[0]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03238103")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[1]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03238108")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[2]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03261577")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[3]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03238105")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[4]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03238110")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[5]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03246456")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[6]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03241626")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[7]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03223610")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "05")

        if selected_pcb == self.pcb_list[8]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03246481")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[9]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03281095")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[10]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03281097")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[11]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03281102")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[12]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03281104")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[13]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03261573")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[14]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03277672")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[15]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03255710")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "02")

        if selected_pcb == self.pcb_list[16]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03254102")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[17]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03254076")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[18]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03275553")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[19]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03253676")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[20]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03273551")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[21]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03280481")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")

        if selected_pcb == self.pcb_list[22]:
            self.entry_matnum.delete(0, tk.END)
            self.entry_matnum.insert(tk.END, "03262900")
            self.entry_fs.delete(0, tk.END)
            self.entry_fs.insert(tk.END, "01")
