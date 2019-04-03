#!/usr/bin/env python3

#Import tax rates from seperate files
import State
#import Fed

Ptype = input('Do you get paid hourly or salary? ')
STnum = str(input('Do you live in the same state that you work in? '))

if STnum in ['Yes', 'yes']:
    STone = (input('What state do you live in? (Examples: IN, IL, AK) '))
else:
    STone = (input('What state do you live in? (Examples: IN, IL, AK) '))
    STtwo = (input('What state do you work in? (Examples: IN, IL, AK) '))

##Set variable per state
#Indiana
if STone in ['IN', 'in']:
    STone = (100-State.IN)/100
if STnum in ['No', 'no'] and STtwo in ['IN', 'in']:
    STone = (100-State.IN)/100
    STtwo = (100-State.IN)/100

#Will use this if you select "Hourly"
if Ptype in ['hourly', 'Hourly']:
    PayRate = float(input('How much do you make an hour?: '))
    Hours = float(input('How many hours do you work in one week?: (Overtime not calculated yet) '))
    if STnum in ['Yes', 'yes']:
        TotalPayW = (PayRate * Hours * STone) 
        TotalPayB = (PayRate * Hours * STone) * 2
        TotalPayM = (PayRate * Hours * STone) * 4
        TotalPayQ = (PayRate * Hours * STone) * 13
        TotalPaySA = (PayRate * Hours * STone) * 26
        TotalPayA = (PayRate * Hours * STone) * 52
        print('Total weekly pay is '+str(round(TotalPayW,2)))
        print('Total bi-weekly pay is '+str(round(TotalPayB,2)))
        print('Total monthly pay is '+str(round(TotalPayM,2))) 
        print('Total quarterly pay is '+str(round(TotalPayQ,2)))
        print('Total semi-annually pay is '+str(round(TotalPaySA,2)))
        print('Total annual pay is '+str(round(TotalPayA,2)))
        exit()
    elif STnum in ['No', 'no']:
        TotalPayW = (PayRate * Hours * (STone+STtwo)) 
        TotalPayB = (PayRate * Hours * (STone+STtwo)) * 2
        TotalPayM = (PayRate * Hours * (STone+STtwo)) * 4
        TotalPayQ = (PayRate * Hours * (STone+STtwo)) * 13
        TotalPaySA = (PayRate * Hours * (STone+STtwo)) * 26
        TotalPayA = (PayRate * Hours * (STone+STtwo)) * 52
        print('Total weekly pay is '+str(round(TotalPayW,2)))
        print('Total bi-weekly pay is '+str(round(TotalPayB,2)))
        print('Total monthly pay is '+str(round(TotalPayM,2)))
        print('Total quarterly pay is '+str(round(TotalPayQ,2)))
        print('Total semi-annually pay is '+str(round(TotalPaySA,2)))
        print('Total annual pay is '+str(round(TotalPayA,2)))
        exit()

#Will use this if you select "Salary"
if Ptype in ['Salary', 'salary']:
    PayRate = float(input('How much do you make per year?: '))

    #Calculate dependant on if you live in the same state as you work
    if STnum in ['Yes', 'yes']:
        TotalPayW = (PayRate * STone) / 52
        TotalPayB = (PayRate * STone) / 26
        TotalPayM = (PayRate * STone) / 12
        TotalPayQ = (PayRate * STone) / 4
        TotalPaySA = (PayRate * STone) / 2
        TotalPayA = (PayRate * STone)
        print('Total weekly pay is '+str(round(TotalPayW,2)))
        print('Total bi-weekly pay is '+str(round(TotalPayB,2)))
        print('Total monthly pay is '+str(round(TotalPayM,2))) 
        print('Total quarterly pay is '+str(round(TotalPayQ,2)))
        print('Total semi-annually pay is '+str(round(TotalPaySA,2)))
        print('Total annual pay is '+str(round(TotalPayA,2)))
        exit()
    elif STnum in ['No', 'no']:
        TotalPayW = (PayRate * (STone+STtwo)) / 52
        TotalPayB = (PayRate * (STone+STtwo)) / 26
        TotalPayM = (PayRate * (STone+STtwo)) / 12
        TotalPayQ = (PayRate * (STone+STtwo)) /4
        TotalPaySA = (PayRate * (STone+STtwo)) / 2
        TotalPayA = (PayRate * (STone+STtwo))
        print('Total weekly pay is '+str(round(TotalPayW,2)))
        print('Total bi-weekly pay is '+str(round(TotalPayB,2)))
        print('Total monthly pay is '+str(round(TotalPayM,2))) 
        print('Total quarterly pay is '+str(round(TotalPayQ,2)))
        print('Total semi-annually pay is '+str(round(TotalPaySA,2)))
        print('Total annual pay is '+str(round(TotalPayA,2)))
        exit()
