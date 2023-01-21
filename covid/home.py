import tkinter as tkt
from helpers.label import label
from helpers.dropdown import dropdown
from covid.func import plot_total_no_of_cases_each_day, plot_total_no_of_cases_each_month, plot_areas_with_highest_cases, plot_comparing_two_areas
from helpers.regions import region_list
from helpers.destroy import destroy

days = list(range(1, 32))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = [2020]

def label_option (frame, text, options,label_x, label_y, x, y):
    label(frame,text, x=label_x, y=label_y)
    option = tkt.StringVar(frame)
    option.set(options[0]) 
    dropdown(frame, option, options, x=x, y=y)
    return option

def total_no_of_cases_each_day(frame_1): 
    destroy(frame_1)
    
    start_day = label_option(frame_1, "Start Day", days, label_x = 20, label_y=50, x=20, y=70)
    start_day.set(days[0]) 
    end_day = label_option(frame_1, "End Day", days, label_x = 210, label_y=50, x=210, y=70)
    end_day.set(days[2]) 
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    start_month = label_option(frame_1, "Start Month", months, label_x = 20, label_y=120, x=20, y=140)
    start_month.set(months[0]) 
    end_month = label_option(frame_1, "End Month", months, label_x = 210, label_y=120, x=210, y=140)
    end_month.set(months[1]) 
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    start_year = label_option(frame_1, "Start Year", year, label_x = 20, label_y=190, x=20, y=210)
    start_year.set(year[0]) 
    end_year = label_option(frame_1, "End Year", year, label_x = 210, label_y=190, x=210, y=210)
    end_year.set(year[0]) 
    
    func = lambda: plot_total_no_of_cases_each_day(
        start_day.get(),
        end_day.get(),
        start_month.get(),
        end_month.get(),
        start_year.get(),
        end_year.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=120, y=280)
    
def total_no_of_cases_each_month(frame_1):
    destroy(frame_1)
        
    start_month_arr = ["January"]
    end_month_arr = ["December"]
    
    start_month = label_option(frame_1, "Start Month", start_month_arr, label_x = 100, label_y=50, x=100, y=70)
    start_month.set(start_month_arr[0]) 
    
    end_month = label_option(frame_1, "End Month", end_month_arr, label_x = 100, label_y=120, x=100, y=140)
    end_month.set(end_month_arr[0]) 
    
    func = lambda: plot_total_no_of_cases_each_month(
        start_month.get(),
        end_month.get(),
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=100, y=200)

def areas_with_highest_cases(frame_1):
    destroy(frame_1)
    
    start_day = label_option(frame_1, "Start Day", days, label_x = 100, label_y=50, x=100, y=70)
    start_day.set(days[0]) 
    
    start_month = label_option(frame_1, "Start Month", months, label_x = 100, label_y=120, x=100, y=140)
    start_month.set(months[0]) 
    
    start_year = label_option(frame_1, "Start Year", year, label_x = 100, label_y=190, x=100, y=210)
    start_year.set(year[0]) 
     
    
    func = lambda: plot_areas_with_highest_cases(
        start_day.get(),
        start_month.get(),
        start_year.get(),
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=100, y=260)
    

def comparing_two_areas(frame_1):
    destroy(frame_1)
    
    start_day = label_option(frame_1, "Start Day", days, label_x = 20, label_y=50, x=20, y=70)
    start_day.set(days[0]) 
    end_day = label_option(frame_1, "End Day", days, label_x = 210, label_y=50, x=210, y=70)
    end_day.set(days[2]) 
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    start_month = label_option(frame_1, "Start Month", months, label_x = 20, label_y=120, x=20, y=140)
    start_month.set(months[0]) 
    end_month = label_option(frame_1, "End Month", months, label_x = 210, label_y=120, x=210, y=140)
    end_month.set(months[1]) 
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    start_year = label_option(frame_1, "Start Year", year, label_x = 20, label_y=190, x=20, y=210)
    start_year.set(year[0]) 
    end_year = label_option(frame_1, "End Year", year, label_x = 210, label_y=190, x=210, y=210)
    end_year.set(year[0]) 
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    first_region = label_option(frame_1, "First Region", region_list(), label_x = 20, label_y=260, x=20, y=280)
    first_region.set(region_list()[0]) 
    second_region = label_option(frame_1, "Second Region", region_list(), label_x = 210, label_y=260, x=210, y=280)
    second_region.set(region_list()[1]) 
    
    func = lambda: plot_comparing_two_areas(
        start_day.get(),
        end_day.get(),
        start_month.get(),
        end_month.get(),
        start_year.get(),
        end_year.get(),
        first_region.get(),
        second_region.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=120, y=320)