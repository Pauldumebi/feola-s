import tkinter as tkt
from helpers.label_option import label_option
from stop_and_search.func import plot_stop_and_search_by_months, plot_compare_stop_and_search_results_for_two_areas, plot_ethnicity, plot_by_gender
from helpers.destroy import destroy
from stop_and_search.request import police_force

days = list(range(1, 32))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
stop_and_search_year_list = ["2020", "2021", "2022"]

def stop_and_search_by_months(frame_1):
    destroy(frame_1)
    
    month = label_option(frame_1, "Month", months, label_x = 50, label_y=50, dropdown_x=50, dropdown_y=70)
    year = label_option(frame_1, "Year", stop_and_search_year_list, label_x = 50, label_y=120, dropdown_x=50, dropdown_y=140) 
    all_police_forces = list(police_force().keys())
    police_force_list = label_option(frame_1, "Police Force", all_police_forces, label_x = 50, label_y=190, dropdown_x=50, dropdown_y=210)
    
    func = lambda: plot_stop_and_search_by_months(
        month.get(),
        year.get(),
        police_force_list.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=50, y=260)
    
def compare_stop_and_search_results_for_two_areas(frame_1):
    destroy(frame_1)
    
    year = label_option(frame_1, "Year", stop_and_search_year_list, label_x = 50, label_y=50, dropdown_x=50, dropdown_y=70) 
    all_police_forces = list(police_force().keys())
    first_police_force_list = label_option(frame_1, "First Police Force", all_police_forces, label_x = 50, label_y=120, dropdown_x=50, dropdown_y=140) 
    all_police_forces = list(police_force().keys())
    second_police_force_list = label_option(frame_1, "Second Police Force", all_police_forces, label_x = 50, label_y=190, dropdown_x=50, dropdown_y=210) 
    
    func = lambda: plot_compare_stop_and_search_results_for_two_areas(
        year.get(),
        first_police_force_list.get(),
        second_police_force_list.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=50, y=260)
    
def ethnicity(frame_1):
    destroy(frame_1)
    
    months_list = label_option(frame_1, "Month", months, label_x = 50, label_y=50, dropdown_x=50, dropdown_y=70)
    year = label_option(frame_1, "Year", stop_and_search_year_list, label_x = 50, label_y=120, dropdown_x=50, dropdown_y=140) 
    all_police_forces = list(police_force().keys())
    police_force_list = label_option(frame_1, "Police Force", all_police_forces, label_x = 50, label_y=190, dropdown_x=50, dropdown_y=210)
    
    func = lambda: plot_ethnicity(
        months_list.get(),
        year.get(),
        police_force_list.get(),
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=50, y=260)
    
def by_gender(frame_1):
    destroy(frame_1)
    
    month_list = label_option(frame_1, "Month", months, label_x = 50, label_y=50, dropdown_x=50, dropdown_y=70)
    year = label_option(frame_1, "Year", stop_and_search_year_list, label_x = 50, label_y=120, dropdown_x=50, dropdown_y=140) 
    all_police_forces = list(police_force().keys())
    police_force_list = label_option(frame_1, "Police Force", all_police_forces, label_x = 50, label_y=190, dropdown_x=50, dropdown_y=210)
    
    func = lambda: plot_by_gender(
        month_list.get(),
        year.get(),
        police_force_list.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=50, y=260)