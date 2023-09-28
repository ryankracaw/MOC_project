import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl
from tkcalendar import Calendar, DateEntry
import TKinterModernThemes as TKMT


def enter_data():
    date = date_entry.get()
    rig_num = rig_num_entry.get()
    region = region_combobox.get()
    incident_color = incident_color_combobox.get()

    print("Date: ", date)
    print("Region: ", region, "Rig Number: ", rig_num)
    print("Incident Color", incident_color)
    print("------------------------------------------")

    filepath = r"C:\Users\ryan.kracaw\Desktop\Projects\test_output\ocr_data.xlsx"

    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ['Date', 'Region', "Rig Number", "Incident Color"]
        sheet.append(heading)
        workbook.save(filepath)
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([date, region, rig_num, incident_color])
    workbook.save(filepath)

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Frame
main_frame = tkinter.LabelFrame(frame, text="Main Frame")
main_frame.grid(row= 0, column=0, padx=20, pady=10)

# Date
date_label = tkinter.Label(main_frame, text="Date")
date_entry = DateEntry(main_frame)
date_label.grid(row=0, column=0)
date_entry.grid(row=1, column=0)

# Rig Number
rig_num_label = tkinter.Label(main_frame, text="Rig Number")
rig_num_entry = tkinter.Entry(main_frame)
rig_num_label.grid(row=0, column=1)
rig_num_entry.grid(row=1, column=1)

# Region
region_label = tkinter.Label(main_frame, text="Region")
region_combobox = ttk.Combobox(main_frame, values=['West Texas', 'East Texas', 'Appalachia'])
region_label.grid(row=0, column=2)
region_combobox.grid(row=1, column=2)

# Incident Color
incident_color_label = tkinter.Label(main_frame, text="Incident Color")
incident_color_combobox = ttk.Combobox(main_frame, values=['Orange', 'Red'])
incident_color_label.grid(row=0, column=3)
incident_color_combobox.grid(row=1, column=3)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()