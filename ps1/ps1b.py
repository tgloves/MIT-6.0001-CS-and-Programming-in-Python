# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:47:39 2020

@author: tgloves
"""


#Problem Set B Answer. My answers are coming up a month short for 2/3 of the test cases
annual_salary = float(input("Enter starting annual salary:"))
portion_saved = float(input("Enter portion of salary to be saved:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("The semi-annual salary raise:"))

portion_down_payment = total_cost*.25 #down payment is 25% of house cost
monthly_salary = annual_salary/12 
current_savings = float(0) #current savings amount defined as float
total_number_months = int(0) #month counter

while current_savings < portion_down_payment: #run loop until the savings exceeds 25% down payment
    total_number_months = total_number_months+1 #count the total number of months, adding 1 month each loop
    if total_number_months%6==0:
        monthly_salary = monthly_salary+(monthly_salary*semi_annual_raise)
        current_savings += (portion_saved*monthly_salary)+(current_savings*.04/12)#savings increases by amount saved and 4% APY 
    else:
        current_savings += (portion_saved*monthly_salary)+(current_savings*.04/12)
    if current_savings >= portion_down_payment:
        print("Enter your annual salary:", int(annual_salary))
        print("Enter the percent of your salary to save, as a decimal:", portion_saved)
        print("Enter the cost of your dream home:", int(total_cost))
        print("Number of months:", total_number_months)
        break 