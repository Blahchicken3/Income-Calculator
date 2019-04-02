#!/usr/bin/env python3

import State
#import Fed

Ptype = input('Do you get paid hourly or salary? ')
STnum = str(input('Do you live in the same state that you work in? '))

if STnum in ['Yes', 'yes']:
    STone = (input('What state do you live in? (Examples: IN, IL, AK) '))
#else:
#    STone = (input('What state do you live in? (Examples: IN, IL, AK) '))
#    STtwo = (input('What state do you work in? (Examples: IN, IL, AK) '))

#TESTING IF IT WORKS WITH INDIANA
if STone == 'IN':
    STone = (100-State.IN)/100
    print(STone)

#if Ptype in ['hourly', 'Hourly']:

if Ptype in ['Salary', 'salary']:
    PayRate = float(input('How much do you make per year?: '))

    if STnum in ['Yes', 'yes']:
        TotalPayW = (PayRate * STone) / 52
        TotalPayB = (PayRate * STone) / 26
        TotalPayM = (PayRate * STone) / 12
        TotalPayBY = (PayRate * STone)
        print('Total weekly pay is '+str(round(TotalPayW,2)))
        print('Total bi-weekly pay is '+str(round(TotalPayB,2)))
        print('Total monthly pay is '+str(round(TotalPayM,2))) 
        exit()
#    else:
  