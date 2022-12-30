from tkinter import messagebox
import datetime as dt

def month_calendar():

    return {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }

def form_validator(
    start_day,
    end_day,
    start_month,
    end_month,
    start_year,
    end_year,
):
    
    try:
        start_date = dt.datetime(
            day=int(start_day),
            month=int(month_calendar()[start_month]),
            year=int(start_year),
        )
        end_date = dt.datetime(
            day=int(end_day), month=int(month_calendar()[end_month]), year=int(end_year)
        ) 
    except:
        messagebox.showinfo("showinfo", "You have selected an invalid date, please select again")
    
    
    if start_date > end_date:
       return messagebox.showinfo("showinfo", "You have selected an invalid date, start date cannot be ahead of end date!")
    
    else:
        return start_date, end_date
    
  