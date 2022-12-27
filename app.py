
import tkinter as tkt
from helpers.label import label
from helpers.dropdown import dropdown
from covid.func import plot_total_no_of_cases_each_day, plot_total_no_of_cases_each_month, plot_areas_with_highest_cases, plot_comparing_two_areas
from tkinter import ttk

root = tkt.Tk()
root.geometry("600x600")
root.title("C2007438-Element 2")

def destroy(val):
    # clear window
    if len(val.winfo_children()) > 0:
        for widget in val.winfo_children():
            widget.destroy()
            
frame_1 = tkt.Frame(root, width=400, height=330)
frame_1.place(x=140, y=150)

# frame_2 = tkt.Frame(root, width=400, height=330)
# frame_2.place(x=140, y=100)

days = list(range(1, 32))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = [2020]
    
def total_no_of_cases_each_day(): 
    destroy(frame_1)

    label(frame_1, "Start Day", x=20, y=50)
    start_day = tkt.StringVar(frame_1)
    
    # select a default value for the dropdown
    start_day.set(days[0]) 
    dropdown(frame_1, start_day, days, x=20, y=70)
    
    label(frame_1, "End Day", x=210, y=50)
    end_day = tkt.StringVar(frame_1)
    end_day.set(days[1])
    dropdown(frame_1, end_day, days, x=210, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Month", x=20, y=120)
    start_month = tkt.StringVar(frame_1)
    start_month.set(months[0])
    dropdown(frame_1, start_month, months, x=20, y=140)
    
    label(frame_1, "End Month", x=210, y=120)
    end_month = tkt.StringVar(frame_1)
    end_month.set(months[1])
    dropdown(frame_1, end_month, months, x=210, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Year", x=20, y=190)
    start_year = tkt.StringVar(frame_1)
    start_year.set(year[0])
    dropdown(frame_1, start_year, year, x=20, y=210)
    
    label(frame_1, "End Year", x=210, y=190)
    end_year = tkt.StringVar(frame_1)
    end_year.set(year[0])
    dropdown(frame_1, end_year, year, x=210, y=210)
    
    func = lambda: plot_total_no_of_cases_each_day(
        start_day.get(),
        end_day.get(),
        start_month.get(),
        end_month.get(),
        start_year.get(),
        end_year.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=120, y=280)
    
def total_no_of_cases_each_month():
    destroy(frame_1)
        
    start_month_arr = ["January"]
    end_month_arr = ["December"]
    
    label(frame_1, "Start Month", x=100, y=50)
    start_month = tkt.StringVar(frame_1)
    start_month.set(start_month_arr[0]) 
    dropdown(frame_1, start_month, start_month_arr, x=100, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    
    label(frame_1, "End Month", x=100, y=120)
    end_month = tkt.StringVar(frame_1)
    end_month.set(end_month_arr[0])
    dropdown(frame_1, end_month, end_month_arr, x=100, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    func = lambda: plot_total_no_of_cases_each_month(
        start_month.get(),
        end_month.get(),
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=100, y=200)

def areas_with_highest_cases():
    destroy(frame_1)
     
    label(frame_1, "Start Day", x=100, y=50)
    start_day = tkt.StringVar(frame_1)
    start_day.set(days[0]) 
    dropdown(frame_1, start_day, days, x=100, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        
    label(frame_1, "Start Month", x=100, y=120)
    start_month = tkt.StringVar(frame_1)
    start_month.set(months[0])
    dropdown(frame_1, start_month, months, x=100, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Year", x=100, y=190)
    start_year = tkt.StringVar(frame_1)
    start_year.set(year[0])
    dropdown(frame_1, start_year, year, x=100, y=210)
    
    func = lambda: plot_areas_with_highest_cases(
        start_day.get(),
        start_month.get(),
        start_year.get(),
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=100, y=260)
    

def comparing_two_areas():
    destroy(frame_1)
    
    label(frame_1, "Start Day", x=20, y=50)
    start_day = tkt.StringVar(frame_1)
    
    # select a default value for the dropdown
    start_day.set(days[0]) 
    dropdown(frame_1, start_day, days, x=20, y=70)
    
    label(frame_1, "End Day", x=210, y=50)
    end_day = tkt.StringVar(frame_1)
    end_day.set(days[1])
    dropdown(frame_1, end_day, days, x=210, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Month", x=20, y=120)
    start_month = tkt.StringVar(frame_1)
    start_month.set(months[0])
    dropdown(frame_1, start_month, months, x=20, y=140)
    
    label(frame_1, "End Month", x=210, y=120)
    end_month = tkt.StringVar(frame_1)
    end_month.set(months[1])
    dropdown(frame_1, end_month, months, x=210, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Year", x=20, y=190)
    start_year = tkt.StringVar(frame_1)
    start_year.set(year[0])
    dropdown(frame_1, start_year, year, x=20, y=210)
    
    label(frame_1, "End Year", x=210, y=190)
    end_year = tkt.StringVar(frame_1)
    end_year.set(year[0])
    dropdown(frame_1, end_year, year, x=210, y=210)
    
    func = lambda: plot_comparing_two_areas(
        start_day.get(),
        end_day.get(),
        start_month.get(),
        end_month.get(),
        start_year.get(),
        end_year.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=120, y=280)
    
# tab_control = ttk.Notebook(root)

# total_no_of_cases_each_day_tab = tkt.Frame(tab_control)
# total_no_of_cases_each_month_tab = tkt.Frame(tab_control)
# areas_with_highest_cases_tab = tkt.Frame(tab_control)
# comparing_two_areas_tab = tkt.Frame(tab_control)
    
def render_covid_btns():
    # destroy(covid)
    tkt.Button(root, text="Total number of cases each day" , command=total_no_of_cases_each_day).place(x=40, y=100)
    tkt.Button(root, text="Total number of cases each month" , command=total_no_of_cases_each_month).place(x=280, y=100)
    tkt.Button(root, text="Areas with highest cases each day" , command=areas_with_highest_cases).place(x=40, y=140)
    tkt.Button(root, text="Comparing two areas" , command=comparing_two_areas).place(x=290, y=140)
    
def render_stop_and_search_btns(): 
    # destroy(stop_and_search)
    print('hey')
    
    
# covid = tkt.Frame(root, width=400, height=500)
# covid.place(x=50, y=80)

# stop_and_search = tkt.Frame(root, width=400, height=500)
# stop_and_search.place(x=50, y=80)

tkt.Button(root, text="Covid dataset" , command=lambda: render_covid_btns()).place(x=160, y=40)
tkt.Button(root, text="Stop and Search", command= lambda: render_stop_and_search_btns()).place(x=290, y=40)

tkt.mainloop()
