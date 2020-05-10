# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:01:17 2020

@author: tgloves
"""


# #Problem Set A Answer
annual_salary = float(input("Enter starting annual salary:"))
portion_saved = float(input("Enter portion of salary to be saved:"))
total_cost = float(input("Enter the cost of your dream home:"))

portion_down_payment = total_cost*.25 #down payment is 25% of house cost
monthly_salary = annual_salary/12 
current_savings = float(0) #current savings amount defined as float
total_number_months = int(0) #month counter

while current_savings < portion_down_payment: #run loop until the savings exceeds 25% down payment
    total_number_months = total_number_months+1 #count the total number of months, adding 1 month each loop
    current_savings += (portion_saved*monthly_salary)+(current_savings*.04/12)#savings increases by amount saved and 4% APY 
    if current_savings >= portion_down_payment:
        print("Enter your annual salary:", int(annual_salary))
        print("Enter the percent of your salary to save, as a decimal:", portion_saved)
        print("Enter the cost of your dream home:", int(total_cost))
        print (total_number_months)
        break     
