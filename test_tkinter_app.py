from app import main_app
from helpers import dropdown, label, regions, form_validator
import unittest
import pytest
from covid.home import total_no_of_cases_each_day, areas_with_highest_cases, comparing_two_areas, total_no_of_cases_each_month
from stop_and_search.home import stop_and_search_by_months, compare_stop_and_search_results_for_two_areas, ethnicity, by_gender
import numpy as np
from stop_and_search.request import police_force
# from modules.covid.covidFunc import plotDailyCases, plotTopFiveRegionWithHighestCases, plotTwoRegions, plotByMonths
# from modules.stopSearch import requests
# from modules.stopSearch.stopSearchFunc import validateDate, ageRange, searchPurpose, ethnicity, outcome, gender
import pandas as pd

import warnings
     
class helpers_modules(unittest.TestCase): # Test all functions in the helper folder

    @pytest.mark.asyncio
    async def _start_app(self): # To start the tkinter window without launching it
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = main_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    def test_label(self):    # tests if a label widget is returned
        tk_label = label.label(self.main, "Test", 0, 0).winfo_class()
        self.assertEqual(tk_label, "Label")
        
    
    def test_dropdown(self): # tests if a Menubutton widget is returned
        dropDownMenu = dropdown.dropdown(self.main, 10, ["One", "Two"], 0, 0).winfo_class()
        expected = "Menubutton"
        self.assertEqual(dropDownMenu, expected)
        
        
    def test_month_calendar(self): # tests a dictionary with a length of 12 items is returned
        isMonthDict = form_validator.month_calendar()
        self.assertIsInstance(isMonthDict, dict)
        
        message = "Months in a calendar year should be 12"
        isMonthDict = len(form_validator.month_calendar())
        self.assertLessEqual(isMonthDict, 12, message)
        
        
    def test_region_list(self): # tests if region is a list of items
        all_region = regions.region_list()
        self.assertIsInstance(all_region, list)
        
    
    def test_form_validator(self): # tests if a tuple is returned and the length of the tuple is 2
        
        date = form_validator.form_validator("4", "10", "January", "March", "2020", "2020")
        self.assertIsInstance(date, tuple)
        
        date_length = len(date)
        self.assertEqual(date_length, 2)
        

class stop_and_search_modules(unittest.TestCase):

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = main_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    def length_of_widget(self, frame, expected):
        noOfFormElements = len(frame.winfo_children())
        self.assertEqual(noOfFormElements, expected)
        
    def test_stop_and_search_by_months(self): # tests if the widgets renders and the length matches
        frame = self.main.winfo_children()[-1]
        stop_and_search_by_months(frame)
        self.length_of_widget(frame, 7)
        
    def test_compare_stop_and_search_results_for_two_areas(self): # tests if the widgets renders and the length matches
        frame = self.main.winfo_children()[-1]
        compare_stop_and_search_results_for_two_areas(frame)
        self.length_of_widget(frame, 9)
        
    def test_ethnicity(self): # tests if the widgets renders and the length matches
        frame = self.main.winfo_children()[-1]
        ethnicity(frame)
        self.length_of_widget(frame, 7)
        
    def test_by_gender(self): # tests if the widgets renders and the length matches
        frame = self.main.winfo_children()[-1]
        by_gender(frame)
        self.length_of_widget(frame, 7)
    
    def test_police_force(self): # tests return variable is a dictionary
        police_list = police_force()
        self.assertIsInstance(police_list, dict)
         
class covid_modules(unittest.TestCase):

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = main_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    def length_of_widget(self, frame, expected):
        noOfFormElements = len(frame.winfo_children())
        self.assertEqual(noOfFormElements, expected)
        
        
    def test_total_no_of_cases_each_day(self): # tests if the widgets renders and the length matches
        frame = self.main.winfo_children()[-1]
        total_no_of_cases_each_day(frame)
        self.length_of_widget(frame, 13)
        
        
    def test_total_no_of_cases_each_month(self): # tests if the widgets renders and the length matches
        frame = self.main.winfo_children()[-1]
        total_no_of_cases_each_month(frame)
        self.length_of_widget(frame, 5)
          
        
    def test_areas_with_highest_cases(self): # tests if the widgets renders and the length matches
        frame = self.main.winfo_children()[-1]
        areas_with_highest_cases(frame)
        self.length_of_widget(frame, 7)
        
        
    def test_comparing_two_areas(self):  # tests if the widgets renders and the length matches
        frame = self.main.winfo_children()[-1]
        comparing_two_areas(frame)
        self.length_of_widget(frame, 17)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)