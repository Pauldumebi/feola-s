import tkinter as tkt

def label(window, text, x, y):
    label = tkt.Label(window, text=text, font=("Arial", 11))
    label.place(x=x, y=y)

    return label

def dropdown(window, val, options, x, y):

    dropDownMenu = tkt.OptionMenu(window, val, *options)
    dropDownMenu.place(x=x, y=y)

    return dropDownMenu

def label_option (frame, text, options,label_x, label_y, dropdown_x, dropdown_y):
    label(frame,text, x=label_x, y=label_y)
    option = tkt.StringVar(frame)
    option.set(options[0]) 
    dropdown(frame, option, options, x=dropdown_x, y=dropdown_y)
    return option