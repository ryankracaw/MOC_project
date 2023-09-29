import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl
from tkcalendar import Calendar, DateEntry
import TKinterModernThemes as TKMT

rig_list = []
cat_list = []
master_list = []

def enter_data():
    list = []
    date = date_entry.get()
    rig_num = rig_num_entry.get()
    region = region_combobox.get()
    if o1_var.get() == 1:
        color = 'Orange'
        category = 'Exceeding 90% of the following rig equipment specifications: tubular tensile strength or weakest load path equipment'
    if o2_var.get() == 1:
        color = 'Orange'
        category = 'Operations with a drill line design factor down to 3.0'
    if o3_var.get() == 1:
        color = 'Orange'
        category = 'Deviations from executed contracts or bridging documents'
    if o4_var.get() == 1:
        color = 'Orange'
        category = 'Deviations from operations that require a JMR and/or OCR and formal documented procedures for rig crews to follow '
    if o5_var.get() == 1:
        color = 'Orange'
        category = 'Board audio AND visual communications not operational while drilling'
    if o6_var.get() == 1:
        color = 'Orange'
        category = 'VFD (secondary) BOP panel not fully functional (if applicable)'
    if o7_var.get() == 1:
        color = 'Orange'
        category = 'FOSV AND IBOP (floor valves) not present or fully functional for each connection type'
    if o8_var.get() == 1:
        color = 'Orange'
        category = 'Up to 2 critical PVT sensor failures'
    if o9_var.get() == 1:
        color = 'Orange'
        category = 'Reduction in accumulator recharge or storage capacity or failure of safety critical components WITHOUT redundancy '
    if o10_var.get() == 1:
        color = 'Orange'
        category = '16-30 bbls cumulative gain while tripping'
    if o11_var.get() == 1:
        color = 'Orange'
        category = '41-60 bbls static losses per hour '
    if o12_var.get() == 1:
        color = 'Orange'
        category = 'Dynamic losses - drilling without returns for 2-4 hours'
    if o13_var.get() == 1:
        color = 'Orange'
        category = 'Deviations from approved tripping methods in an underbalanced well'
    if o14_var.get() == 1:
        color = 'Orange'
        category = 'Opening BOP cavities after testing BOPs; decreased barrier redundancy'
    if o15_var.get() == 1:
        color = 'Orange'
        category = 'Damage or modifications that reduce egress from the mast or the rig floor '
    if o16_var.get() == 1:
        color = 'Orange'
        category = 'Using a flowline isolation valve (e.g., Orbit valve) to hold surface pressure on a well WITHOUT using an MPD choke '
    if o17_var.get() == 1:
        color = 'Orange'
        category = 'Deviations from policy'

    if r1_var.get() == 1:
        color = 'Red'
        category = 'Exceeding 95% of the following rig equipment specifications: tubular tensile strength or weakest load path equipment'
    if r2_var.get() == 1:
        color = 'Red'
        category = 'Operations with a drill line design factor less than 3.0'
    if r3_var.get() == 1:
        color = 'Red'
        category = 'Board audio AND visual communications not operational while tripping'
    if r4_var.get() == 1:
        color = 'Red'
        category = 'Loss of driller (primary) BOP remote shutin capability '
    if r5_var.get() == 1:
        color = 'Red'
        category = 'More than 2 critical PVT sensor failures '
    if r6_var.get() == 1:
        color = 'Red'
        category = 'Failed accumulator drawdown test'
    if r7_var.get() == 1:
        color = 'Red'
        category = '31 bbls or more cumulative gain while tripping'
    if r8_var.get() == 1:
        color = 'Red'
        category = '61 bbls or more static losses per hour '
    if r9_var.get() == 1:
        color = 'Red'
        category = 'Dynamic losses - drilling without returns for more than 4 hours'
    if r10_var.get() == 1:
        color = 'Red'
        category = 'Removing any BOPs on open hole or loss of barrier redundancy'
    if r11_var.get() == 1:
        color = 'Red'
        category = 'Operating any MPD system in excess of 1,000 psi unless following a pre-approved PTEN MPD Operations Matrix'
    
    

    filepath = r"C:\Users\ryan.kracaw\Desktop\Projects\test_output\ocr_data.xlsx"

    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ['Date', 'Color', 'Rig Number', 'Region', 'Category']
        sheet.append(heading)
        workbook.save(filepath)
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([date, color, rig_num, region, category])
    workbook.save(filepath)

    text = f'Rig {rig_num} submitted OCR for {category}'
    list.append(text)
    master_list.append(list)

    # Canvas
    canvas = tkinter.Text(frame, height = 40, width = 90)
    for i in master_list:
        text1 = f'\n {i}'
        canvas.insert('end', text1)
    canvas.grid(row=2, column=1, padx=20, pady=10)

    rig_num_entry.delete(0, 'end')
    o1_var.set(0)
    o2_var.set(0)
    o3_var.set(0)
    o4_var.set(0)
    o5_var.set(0)
    o6_var.set(0)
    o7_var.set(0)
    o8_var.set(0)
    o9_var.set(0)
    o10_var.set(0)
    o11_var.set(0)
    o12_var.set(0)
    o13_var.set(0)
    o14_var.set(0)
    o15_var.set(0)
    o16_var.set(0)
    o17_var.set(0)

    r1_var.set(0)
    r2_var.set(0)
    r3_var.set(0)
    r4_var.set(0)
    r5_var.set(0)
    r6_var.set(0)
    r7_var.set(0)
    r8_var.set(0)
    r9_var.set(0)
    r10_var.set(0)
    r11_var.set(0)

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
date_label.grid(row=0, column=0, padx=5, sticky="ew")
date_entry.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

# Rig Number
rig_num_label = tkinter.Label(main_frame, text="Rig Number")
rig_num_entry = tkinter.Entry(main_frame)
rig_num_label.grid(row=0, column=1, padx=5, sticky="ew")
rig_num_entry.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

# Region
region_label = tkinter.Label(main_frame, text="Region")
region_combobox = ttk.Combobox(main_frame, values=['Appalachia', 'Mid-Con', 'North Dakota', 'Rockies', 'East Texas', 'West Texas', 'South Texas'])
region_label.grid(row=0, column=2, padx=5, sticky="ew")
region_combobox.grid(row=1, column=2, padx=5, pady=10, sticky="ew")

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data, background='#36FF00', height=2)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)



# Categories frame
OCR_frame = tkinter.LabelFrame(frame, text="Categories")
OCR_frame.grid(row= 2, column=0, padx=20, pady=10)

# Orange Frame
orange_frame = tkinter.LabelFrame(OCR_frame, text='Orange Category', background='#FFBC5B')
orange_frame.grid(row=0, column=0)

# Red Frame
red_frame = tkinter.LabelFrame(OCR_frame, text='Red Category', background='#FF9696')
red_frame.grid(row=0, column=1)

# ORANGE Operational Change Request Categories
o1_var = tkinter.IntVar()
o1_box = tkinter.Checkbutton(orange_frame, text = 'Exceeding 90% of the following rig equipment specifications: \n tubular tensile strength or weakest load path equipment', variable=o1_var, background='#FFBC5B', justify='left')
o1_box.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

sep1 = ttk.Separator(orange_frame, orient='horizontal')
sep1.grid(row=1, column=0, padx=5, sticky="ew")

o2_var = tkinter.IntVar()
o2_box = tkinter.Checkbutton(orange_frame, text = 'Operations with a drill line design factor down to 3.0', variable=o2_var, background='#FFBC5B', justify='left')
o2_box.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

sep2 = ttk.Separator(orange_frame, orient='horizontal')
sep2.grid(row=3, column=0, padx=5, sticky="ew")

o3_var = tkinter.IntVar()
o3_box = tkinter.Checkbutton(orange_frame, text = 'Deviations from executed contracts or bridging documents', variable=o3_var, background='#FFBC5B', justify='left')
o3_box.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

sep3 = ttk.Separator(orange_frame, orient='horizontal')
sep3.grid(row=5, column=0, padx=5, sticky="ew")

o4_var = tkinter.IntVar()
o4_box = tkinter.Checkbutton(orange_frame, text = 'Deviations from operations that require a JMR and/or OCR and formal \n documented procedures for rig crews to follow (e.g., bypassing safety \n controls, offline cementing, operating in encoder bypass, manually \n shifting drawwork, etc.)', variable=o4_var, background='#FFBC5B', justify='left')
o4_box.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

sep4 = ttk.Separator(orange_frame, orient='horizontal')
sep4.grid(row=7, column=0, padx=5, sticky="ew")

o5_var = tkinter.IntVar()
o5_box = tkinter.Checkbutton(orange_frame, text = '*Board audio AND visual communications not operational while drilling', variable=o5_var, background='#FFBC5B', justify='left')
o5_box.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

sep5 = ttk.Separator(orange_frame, orient='horizontal')
sep5.grid(row=9, column=0, padx=5, sticky="ew")

o6_var = tkinter.IntVar()
o6_box = tkinter.Checkbutton(orange_frame, text = '*VFD (secondary) BOP panel not fully functional (if applicable)', variable=o6_var, background='#FFBC5B', justify='left')
o6_box.grid(row=10, column=0, padx=5, pady=5, sticky="ew")

sep6 = ttk.Separator(orange_frame, orient='horizontal')
sep6.grid(row=11, column=0, padx=5, sticky="ew")

o7_var = tkinter.IntVar()
o7_box = tkinter.Checkbutton(orange_frame, text = '*FOSV AND IBOP (floor valves) not present or fully functional for each connection type', variable=o7_var, background='#FFBC5B', justify='left')
o7_box.grid(row=12, column=0, padx=5, pady=5, sticky="ew")

sep7 = ttk.Separator(orange_frame, orient='horizontal')
sep7.grid(row=13, column=0, padx=5, sticky="ew")

o8_var = tkinter.IntVar()
o8_box = tkinter.Checkbutton(orange_frame, text = '*Up to 2 critical PVT sensor failures (e.g., flow, active tank, trip tank, or sand trap, if available)', variable=o8_var, background='#FFBC5B', justify='left')
o8_box.grid(row=14, column=0, padx=5, pady=5, sticky="ew")

sep8 = ttk.Separator(orange_frame, orient='horizontal')
sep8.grid(row=15, column=0, padx=5, sticky="ew")

o9_var = tkinter.IntVar()
o9_box = tkinter.Checkbutton(orange_frame, text = '*Reduction in accumulator recharge or storage capacity or failure \n of safety critical components WITHOUT redundancy \n (e.g., electric pump, 2 or more air pumps, bottle bank, etc.)', variable=o9_var, background='#FFBC5B', justify='left')
o9_box.grid(row=16, column=0, padx=5, pady=5, sticky="ew")

sep9 = ttk.Separator(orange_frame, orient='horizontal')
sep9.grid(row=17, column=0, padx=5, sticky="ew")

o10_var = tkinter.IntVar()
o10_box = tkinter.Checkbutton(orange_frame, text = '16-30 bbls cumulative gain while tripping', variable=o10_var, background='#FFBC5B', justify='left')
o10_box.grid(row=18, column=0, padx=5, pady=5, sticky="ew")

sep10 = ttk.Separator(orange_frame, orient='horizontal')
sep10.grid(row=19, column=0, padx=5, sticky="ew")

o11_var = tkinter.IntVar()
o11_box = tkinter.Checkbutton(orange_frame, text = '41-60 bbls static losses per hour (e.g., mud pumps off)', variable=o11_var, background='#FFBC5B', justify='left')
o11_box.grid(row=20, column=0, padx=5, pady=5, sticky="ew")

sep11 = ttk.Separator(orange_frame, orient='horizontal')
sep11.grid(row=21, column=0, padx=5, sticky="ew")

o12_var = tkinter.IntVar()
o12_box = tkinter.Checkbutton(orange_frame, text = 'Dynamic losses - drilling without returns for 2-4 hours', variable=o12_var, background='#FFBC5B', justify='left')
o12_box.grid(row=22, column=0, padx=5, pady=5, sticky="ew")

sep12 = ttk.Separator(orange_frame, orient='horizontal')
sep12.grid(row=23, column=0, padx=5, sticky="ew")

o13_var = tkinter.IntVar()
o13_box = tkinter.Checkbutton(orange_frame, text = 'Deviations from approved tripping methods in an underbalanced well', variable=o13_var, background='#FFBC5B', justify='left')
o13_box.grid(row=24, column=0, padx=5, pady=5, sticky="ew")

sep13 = ttk.Separator(orange_frame, orient='horizontal')
sep13.grid(row=25, column=0, padx=5, sticky="ew")

o14_var = tkinter.IntVar()
o14_box = tkinter.Checkbutton(orange_frame, text = 'Opening BOP cavities after testing BOPs; decreased barrier redundancy', variable=o14_var, background='#FFBC5B', justify='left')
o14_box.grid(row=26, column=0, padx=5, pady=5, sticky="ew")

sep14 = ttk.Separator(orange_frame, orient='horizontal')
sep14.grid(row=27, column=0, padx=5, sticky="ew")

o15_var = tkinter.IntVar()
o15_box = tkinter.Checkbutton(orange_frame, text = 'Damage or modifications that reduce egress from the mast or the rig floor \n (e.g., stair removal, slow descent device, etc.)', variable=o15_var, background='#FFBC5B', justify='left')
o15_box.grid(row=28, column=0, padx=5, pady=5, sticky="ew")

sep15 = ttk.Separator(orange_frame, orient='horizontal')
sep15.grid(row=29, column=0, padx=5, sticky="ew")

o16_var = tkinter.IntVar()
o16_box = tkinter.Checkbutton(orange_frame, text = 'Using a flowline isolation valve (e.g., Orbit valve) to hold surface pressure on a \n well WITHOUT using an MPD choke (e.g., during connections, tripping, well control, etc.)', variable=o16_var, background='#FFBC5B', justify='left')
o16_box.grid(row=30, column=0, padx=5, pady=5, sticky="ew")

sep16 = ttk.Separator(orange_frame, orient='horizontal')
sep16.grid(row=31, column=0, padx=5, sticky="ew")

o17_var = tkinter.IntVar()
o17_box = tkinter.Checkbutton(orange_frame, text = "Deviations from policy (e.g., forklift off location, catwalk tubular under 4', etc.)", variable=o17_var, background='#FFBC5B', justify='left')
o17_box.grid(row=32, column=0, padx=5, pady=5, sticky="ew")

#################################################################################################################################################

# RED Operational Change Request Categories
r1_var = tkinter.IntVar()
r1_box = tkinter.Checkbutton(red_frame, text = 'Exceeding 95% of the following rig equipment specifications: \n tubular tensile strength or weakest load path equipment', variable=r1_var, background='#FF9696', justify='left')
r1_box.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

sep17 = ttk.Separator(red_frame, orient='horizontal')
sep17.grid(row=1, column=0, padx=5, sticky="ew")

r2_var = tkinter.IntVar()
r2_box = tkinter.Checkbutton(red_frame, text = 'Operations with a drill line design factor less than 3.0', variable=r2_var, background='#FF9696', justify='left')
r2_box.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

sep18 = ttk.Separator(red_frame, orient='horizontal')
sep18.grid(row=3, column=0, padx=5, sticky="ew")

r3_var = tkinter.IntVar()
r3_box = tkinter.Checkbutton(red_frame, text = '*Board audio AND visual communications not operational while tripping', variable=r3_var, background='#FF9696', justify='left')
r3_box.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

sep19 = ttk.Separator(red_frame, orient='horizontal')
sep19.grid(row=5, column=0, padx=5, sticky="ew")

r4_var = tkinter.IntVar()
r4_box = tkinter.Checkbutton(red_frame, text = '*Loss of driller (primary) BOP remote shutin capability ', variable=r4_var, background='#FF9696', justify='left')
r4_box.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

sep20 = ttk.Separator(red_frame, orient='horizontal')
sep20.grid(row=7, column=0, padx=5, sticky="ew")

r5_var = tkinter.IntVar()
r5_box = tkinter.Checkbutton(red_frame, text = '*More than 2 critical PVT sensor failures (e.g., flow, active tank, trip tank, \n or sand trap, if available)', variable=r5_var, background='#FF9696', justify='left')
r5_box.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

sep21 = ttk.Separator(red_frame, orient='horizontal')
sep21.grid(row=9, column=0, padx=5, sticky="ew")

r6_var = tkinter.IntVar()
r6_box = tkinter.Checkbutton(red_frame, text = '*Failed accumulator drawdown test', variable=r6_var, background='#FF9696', justify='left')
r6_box.grid(row=10, column=0, padx=5, pady=5, sticky="ew")

sep22 = ttk.Separator(red_frame, orient='horizontal')
sep22.grid(row=11, column=0, padx=5, sticky="ew")

r7_var = tkinter.IntVar()
r7_box = tkinter.Checkbutton(red_frame, text = '31 bbls or more cumulative gain while tripping', variable=r7_var, background='#FF9696', justify='left')
r7_box.grid(row=12, column=0, padx=5, pady=5, sticky="ew")

sep23 = ttk.Separator(red_frame, orient='horizontal')
sep23.grid(row=13, column=0, padx=5, sticky="ew")

r8_var = tkinter.IntVar()
r8_box = tkinter.Checkbutton(red_frame, text = '61 bbls or more static losses per hour (e.g., mud pumps off)', variable=r8_var, background='#FF9696', justify='left')
r8_box.grid(row=14, column=0, padx=5, pady=5, sticky="ew")

sep24 = ttk.Separator(red_frame, orient='horizontal')
sep24.grid(row=15, column=0, padx=5, sticky="ew")

r9_var = tkinter.IntVar()
r9_box = tkinter.Checkbutton(red_frame, text = 'Dynamic losses - drilling without returns for more than 4 hours', variable=r9_var, background='#FF9696', justify='left')
r9_box.grid(row=16, column=0, padx=5, pady=5, sticky="ew")

sep25 = ttk.Separator(red_frame, orient='horizontal')
sep25.grid(row=17, column=0, padx=5, sticky="ew")

r10_var = tkinter.IntVar()
r10_box = tkinter.Checkbutton(red_frame, text = 'Removing any BOPs on open hole or loss of barrier redundancy', variable=r10_var, background='#FF9696', justify='left')
r10_box.grid(row=18, column=0, padx=5, pady=5, sticky="ew")

sep26 = ttk.Separator(red_frame, orient='horizontal')
sep26.grid(row=19, column=0, padx=5, sticky="ew")

r11_var = tkinter.IntVar()
r11_box = tkinter.Checkbutton(red_frame, text = 'Operating any MPD system in excess of 1,000 psi unless following \n a pre-approved PTEN MPD Operations Matrix', variable=r11_var, background='#FF9696', justify='left')
r11_box.grid(row=20, column=0, padx=5, pady=5, sticky="ew")


window.mainloop()