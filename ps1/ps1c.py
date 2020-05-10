# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:55:04 2020

@author: tgloves
"""

annual_salary = float(input('Enter your starting salary: '))
x = annual_salary
total_cost = 1000000
semi_annual_raise = 0.07
current_savings = 0
portion_down_payment = 0.25 * total_cost
months = 0
epsilon = 100
low = 0
high = 10000
steps = 0

while True:
    portion_saved = (low + high) / 2
    annual_salary = x
    current_savings = 0
    for mo in range(0, 36):
        monthly_salary = annual_salary / 12
        current_savings = current_savings + float((monthly_salary * portion_saved)/10000) + (current_savings * 0.04)/12
        if mo % 6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    if abs(current_savings - portion_down_payment) <= epsilon:
        print('Best savings rate:', '%.2f' % (portion_saved/100)+'%')#prints savings rate, truncates decimals, adds %
        print('Steps in bisection search:', steps)#prints number of steps
        break
    #lower the upper bound for portion saved because of too much savings
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings > portion_down_payment:
        high = portion_saved
    #raise the lower bound for portion saved because of too little savings
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings < portion_down_payment:
        low = portion_saved
    if low == high: #breaks loop if the lower bound and upper bound are the same, indicating annual salary is too low
        print('It is not possible to pay the down payment in three years.')
        break
    steps = steps + 1