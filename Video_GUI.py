from tkinter import *
from tkinter import ttk
import Video_Editor


def merger():
    clipper1 = clip1.get()
    c1_start = clip1_start.get()
    c1_end = clip1_end.get()
    float(c1_start)
    float(c1_end)
    clipper2 = clip2.get()
    c2_start = clip2_start.get()
    c2_end = clip2_end.get()
    float(c2_start)
    float(c2_end)
    name1 = namer.get()
    Video_Editor.clip_merge(clipper1, clipper2, name1, c1_start, c1_end, c2_start, c2_end)


root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

# Clip 1
ttk.Label(frm, text="Enter Clip 1 path:").grid(column=0, row=0, padx=30, pady=30)
clip1 = ttk.Entry(frm)
clip1.grid(column=1, row=0, padx=30, pady=30)
ttk.Label(frm, text="Enter Clip 1 Start and End:").grid(column=2, row=0, padx=30, pady=30)
clip1_start = ttk.Entry(frm)
clip1_start.grid(column=3, row=0, padx=30, pady=30)
clip1_end = ttk.Entry(frm)
clip1_end.grid(column=4, row=0, padx=30, pady=30)


# Clip 2
ttk.Label(frm, text="Enter Clip 2 path:").grid(column=0, row=1, padx=30, pady=30)
clip2 = ttk.Entry(frm)
clip2.grid(column=1, row=1, padx=30, pady=30)
ttk.Label(frm, text="Enter Clip 2 Start and End:").grid(column=2, row=1, padx=30, pady=30)
clip2_start = ttk.Entry(frm)
clip2_start.grid(column=3, row=1, padx=30, pady=30)
clip2_end = ttk.Entry(frm)
clip2_end.grid(column=4, row=1, padx=30, pady=30)

# Name of Merged Product
ttk.Label(frm, text="Enter Name:").grid(column=0, row=2, padx=30, pady=30)
namer = ttk.Entry(frm)
namer.grid(column=1, row=2, padx=30, pady=30)

ttk.Button(frm, text="Merge!", command=merger).grid(row=3, padx=30, pady=30)

root.mainloop()
