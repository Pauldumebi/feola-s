from stop_and_search.request import get_cases
from helpers.form_validator import month_calendar;
from tkinter import messagebox
import pandas as pd
from charts import horizontal_lollipop, pie_chart, donut_chart, scatter_plot

# This function counts all arrested age-ranges 
def get_age_count_of_arrested_by_month(data):
    ageCountFor10_17 = 0
    ageCountFor18_24 = 0
    ageCountFor25_34 = 0
    ageCountFor34 = 0
    for i in data:
        if i["age_range"] == "10-17" and i["outcome"] == "Arrest":
                ageCountFor10_17 += 1
        elif i["age_range"] == "18-24" and i["outcome"] == "Arrest":
                ageCountFor18_24 += 1
        elif i["age_range"] == "18-24" and i["outcome"] == "Arrest":
                ageCountFor25_34 += 1
        elif i["age_range"] == "over 34" and i["outcome"] == "Arrest":
                ageCountFor34 += 1
        else:
            continue
    
    return {"10-17" : ageCountFor10_17, "18-24": ageCountFor18_24, "25-34" : ageCountFor25_34, "over 34" : ageCountFor34}
 

def is_request_empty(month, year, selected_police_force):
    date = year + "-" + month_calendar()[month]
    # This list contains two items, the data and the length
    result = get_cases(selected_police_force, date)[1]
    if result == []:
        messagebox.showinfo("showinfo", "No data for this selected month")
    else: 
        return result
    
def plot_stop_and_search_by_months(month, year, selected_police_force):    
    stop_and_search_df = pd.DataFrame.from_dict(is_request_empty(month, year, selected_police_force))
    result = stop_and_search_df.groupby(['age_range'], as_index=False).count()
    title = "Stop and search by Age Range for " + selected_police_force + " in " + month + ", " + year
    donut_chart(title, result["involved_person"], result["age_range"])

def plot_compare_stop_and_search_results_for_two_areas(year, first_police_force, second_police_force):
    summer_months = ["June", "July", "August"]

    first_data_dict = {} 
    count = 0
    # loop through the summer months to fetch all cases 
    for month in summer_months:
        
        result = get_age_count_of_arrested_by_month(is_request_empty(month, year, first_police_force))
        first_data_dict[count] = [
            month,
            result["10-17"],
            result["18-24"],
            result["25-34"],
            result["over 34"],
        ]
        count += 1 

    stop_and_search_df_first = pd.DataFrame.from_dict(
        first_data_dict, orient="index", columns=["Month", "10-17", "18-24", "25-34", "over 34"]
    )
    
    second_data_dict = {}
    count = 0
    for month in summer_months:
        
        result = get_age_count_of_arrested_by_month(is_request_empty(month, year, second_police_force))
        second_data_dict[count] = [
            month,
            result["10-17"],
            result["18-24"],
            result["25-34"],
            result["over 34"],
        ]
        count += 1 

    stop_and_search_df_second = pd.DataFrame.from_dict(
        second_data_dict, orient="index", columns=["Month", "10-17", "18-24", "25-34", "over 34"]
    )
    
    title = "Arrest of 18-24 years between " + first_police_force + " \nand " + second_police_force + " in summer months of " + year
 
    horizontal_lollipop(
        title, 
        stop_and_search_df_first, 
        stop_and_search_df_first["18-24"], 
        stop_and_search_df_second["18-24"], 
        first_police_force, 
        second_police_force, 
        "Number of Arrest", 
        "Summer months", 
        stop_and_search_df_first["Month"])

def plot_ethnicity(month, year, selected_police_force):   
 
    stop_and_search_df = pd.DataFrame.from_dict(is_request_empty(month, year, selected_police_force))
    result = stop_and_search_df.groupby(["officer_defined_ethnicity"], as_index=False)[["involved_person"]].count()
    title = "Stop and Search Cases Breakdown by Ethnicity for " + selected_police_force + " in " + month + ", " + year
    scatter_plot(title, result["officer_defined_ethnicity"], result["involved_person"])

def plot_by_gender(month, year, selected_police_force):    

    stop_and_search_df = pd.DataFrame.from_dict(is_request_empty(month, year, selected_police_force))
    result = stop_and_search_df.groupby(['gender'], as_index=False).count()
    title = "Stop and search breakdown of by gender for " + selected_police_force + " in " + month + ", " + year
    pie_chart(title, result["involved_person"], result["gender"])